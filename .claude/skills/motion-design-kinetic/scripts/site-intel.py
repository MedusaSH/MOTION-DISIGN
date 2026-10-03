#!/usr/bin/env python3
"""Site intel: turn a website URL into a brand dossier for a motion design film.

  python3 site-intel.py <url> <project> [--pages 6] [--no-video] [--no-mobile]

Visits the site with headless Chromium (Playwright), accepts the cookie banner, then the home page and the most
useful internal pages (features, product, pricing, about, customers, demo…). Writes into <project>/:

  brand/BRAND.md          the dossier to write the script from: promise, features, proofs (verbatim + source URL),
                          testimonials, prices, CTAs, tone, palette, fonts, visual material, open questions
  brand/site.json         everything raw (texts per page, links, images, videos, meta, JSON-LD)
  brand/palette.json      measured colors (area- and text-weighted) + chosen accent + fonts + free equivalents
  assets/ui/site/         screenshots: desktop full page, viewport slices (1440x900), mobile (390x844), sub-pages
  assets/brand/           logo candidates (inline SVG, header image, favicon, apple-touch-icon, og:image)
  assets/ui/site/video/   videos embedded as direct files (product demos), when allowed (--no-video to skip)

Exit 3 when the site is unreachable from this machine (blocked network): fall back to WebFetch + user screenshots
(see references/site-intel.md). Nothing is ever posted to the site; only GET navigation.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter

PRIORITY = [
    (r"fonctionnalit|feature|produit|product|solution|plateforme|platform|how-it-works|comment", 10),
    (r"tarif|pricing|prix|price|plans?\b|offre", 9),
    (r"demo|démo|essai|trial|video", 8),
    (r"client|customer|case|temoignage|témoignage|testimonial|success|etude|étude", 7),
    (r"about|a-propos|à-propos|qui-sommes|equipe|équipe|team|mission|histoire|story", 6),
    (r"securit|security|rgpd|gdpr|conformit|compliance|integration|intégration", 5),
]
SKIP = r"login|signin|sign-in|connexion|register|signup|inscription|account|compte|cart|panier|checkout|legal|mention|cgu|cgv|privacy|confidentialit|cookie|terms|careers|jobs|recrut|blog/.+/.+|wp-|feed|\.pdf$|\.zip$|mailto:|tel:"
COOKIE_WORDS = ["tout accepter", "accepter", "accept all", "accept", "j'accepte", "ok", "agree", "allow all", "autoriser", "continuer sans accepter", "got it"]
FREE_FONTS = {  # proprietary / common families -> close free (SIL OFL) family available on npm @fontsource
    "helvetica": "Inter", "helvetica neue": "Inter", "arial": "Inter", "sf pro": "Inter", "sf pro display": "Inter",
    "-apple-system": "Inter", "system-ui": "Inter", "segoe ui": "Inter", "circular": "Plus Jakarta Sans",
    "circular std": "Plus Jakarta Sans", "gt walsheim": "Plus Jakarta Sans", "graphik": "Inter", "aeonik": "Manrope",
    "sohne": "Inter", "söhne": "Inter", "neue haas grotesk": "Inter", "avenir": "Nunito Sans", "avenir next": "Nunito Sans",
    "proxima nova": "Montserrat", "gilroy": "Plus Jakarta Sans", "futura": "Jost", "gotham": "Montserrat",
    "brandon grotesque": "Josefin Sans", "tiempos": "Source Serif 4", "tiempos headline": "Fraunces", "gt sectra": "Fraunces",
    "canela": "Fraunces", "recoleta": "Fraunces", "georgia": "Source Serif 4", "times new roman": "Source Serif 4",
    "eina": "Manrope", "satoshi": "Manrope", "general sans": "Manrope", "clash display": "Space Grotesk",
}


def norm_url(u):
    p = urllib.parse.urlsplit(u)
    path = re.sub(r"/+$", "", p.path) or "/"
    return urllib.parse.urlunsplit((p.scheme, p.netloc.lower(), path, "", ""))


def same_site(a, b):
    ha, hb = urllib.parse.urlsplit(a).netloc.lower(), urllib.parse.urlsplit(b).netloc.lower()
    strip = lambda h: h[4:] if h.startswith("www.") else h
    return strip(ha) == strip(hb)


def rgb_to_hex(s):
    m = re.match(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:[,\s/]+([\d.]+))?", s or "")
    if not m:
        return None
    if m.group(4) is not None and float(m.group(4)) < 0.6:
        return None
    return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))


def sat_light(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2
    s = 0 if mx == mn else (mx - mn) / (1 - abs(2 * l - 1))
    return s, l


EXTRACT_JS = r"""
() => {
  const vis = (el) => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
    return r.width > 2 && r.height > 2 && cs.visibility !== 'hidden' && cs.display !== 'none' && parseFloat(cs.opacity) > 0.05; };
  const txt = (el) => (el.innerText || el.textContent || '').replace(/\s+/g, ' ').trim();
  const abs = (u) => { try { return new URL(u, location.href).href; } catch (e) { return null; } };
  const meta = {};
  document.querySelectorAll('meta[name], meta[property]').forEach(m => { const k = m.getAttribute('name') || m.getAttribute('property'); meta[k] = m.getAttribute('content'); });
  const headings = [...document.querySelectorAll('h1,h2,h3')].filter(vis).map(h => {
    let next = h.nextElementSibling, para = '';
    for (let i = 0; i < 4 && next && !para; i++, next = next.nextElementSibling) { const t = txt(next); if (t.length > 30 && !/^H[1-3]$/.test(next.tagName)) para = t.slice(0, 400); }
    if (!para && h.parentElement) { const p = h.parentElement.querySelector('p'); if (p && txt(p).length > 30) para = txt(p).slice(0, 400); }
    return { level: +h.tagName[1], text: txt(h).slice(0, 200), y: Math.round(h.getBoundingClientRect().top + scrollY), para };
  }).filter(h => h.text);
  const paragraphs = [...document.querySelectorAll('p, li')].filter(vis).map(txt).filter(t => t.length > 40 && t.length < 600);
  const ctas = [...document.querySelectorAll('a, button')].filter(vis).filter(el => {
    const cs = getComputedStyle(el); const bg = cs.backgroundColor; const cls = (el.className || '') + '';
    return /btn|button|cta/i.test(cls) || el.tagName === 'BUTTON' || (bg && !/rgba?\(0, 0, 0, 0\)|transparent/.test(bg) && txt(el).length < 40);
  }).map(el => ({ text: txt(el).slice(0, 60), href: el.href || null, bg: getComputedStyle(el).backgroundColor, color: getComputedStyle(el).color })).filter(c => c.text);
  const links = [...document.querySelectorAll('a[href]')].map(a => ({ href: abs(a.getAttribute('href')), text: txt(a).slice(0, 80), nav: !!a.closest('nav, header') }));
  const imgs = [...document.querySelectorAll('img')].filter(vis).map(i => { const r = i.getBoundingClientRect();
    return { src: abs(i.currentSrc || i.src), alt: i.alt || '', w: i.naturalWidth, h: i.naturalHeight, area: Math.round(r.width * r.height), y: Math.round(r.top + scrollY), header: !!i.closest('header, nav') }; });
  const videos = [];
  document.querySelectorAll('video').forEach(v => { const s = v.currentSrc || v.src || (v.querySelector('source') || {}).src; if (s) videos.push({ src: abs(s), poster: v.poster ? abs(v.poster) : null }); });
  document.querySelectorAll('iframe[src]').forEach(f => { if (/youtube|youtu\.be|vimeo|loom|wistia|vidyard/.test(f.src)) videos.push({ src: f.src, embed: true }); });
  const jsonld = [...document.querySelectorAll('script[type="application/ld+json"]')].map(s => { try { return JSON.parse(s.textContent); } catch (e) { return null; } }).filter(Boolean);
  const icons = [...document.querySelectorAll('link[rel*="icon"]')].map(l => ({ rel: l.rel, href: abs(l.getAttribute('href')), sizes: l.getAttribute('sizes') }));
  let logoSvg = null; const hdr = document.querySelector('header') || document.querySelector('nav');
  if (hdr) { const svg = hdr.querySelector('a svg, svg'); if (svg && svg.getBoundingClientRect().width > 24) logoSvg = svg.outerHTML.slice(0, 200000); }
  const logoImg = hdr ? [...hdr.querySelectorAll('img')].filter(vis).map(i => abs(i.currentSrc || i.src))[0] || null : null;
  // colors: area-weighted backgrounds, text-weighted text colors, CTA backgrounds
  const bg = {}, fg = {}, fonts = {};
  const all = [...document.querySelectorAll('body *')].slice(0, 6000);
  for (const el of all) { if (!vis(el)) continue; const cs = getComputedStyle(el); const r = el.getBoundingClientRect();
    const a = Math.min(r.width * r.height, 1920 * 1400); if (cs.backgroundColor) bg[cs.backgroundColor] = (bg[cs.backgroundColor] || 0) + a;
    const own = [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(''); if (own.length) {
      fg[cs.color] = (fg[cs.color] || 0) + own.length; const fam = cs.fontFamily.split(',')[0].replace(/["']/g, '').trim();
      const key = fam + '|' + (/^H[1-3]$/.test(el.tagName) ? 'heading' : 'text'); fonts[key] = (fonts[key] || 0) + own.length; } }
  const bodyBg = getComputedStyle(document.body).backgroundColor;
  const lang = document.documentElement.lang || '';
  const text = document.body.innerText.slice(0, 60000);
  return { url: location.href, title: document.title, lang, meta, headings, paragraphs, ctas, links, imgs, videos, jsonld, icons, logoSvg, logoImg, bg, fg, fonts, bodyBg, text,
           height: document.documentElement.scrollHeight };
}
"""


def accept_cookies(page):
    for frame in [page.main_frame] + page.frames[1:4]:
        for w in COOKIE_WORDS:
            try:
                b = frame.get_by_role("button", name=re.compile(rf"^\s*{re.escape(w)}\s*$", re.I))
                if b.count():
                    b.first.click(timeout=1500)
                    page.wait_for_timeout(600)
                    return w
            except Exception:
                pass
    return None


def settle(page):
    """Scroll down and back so lazy content and scroll animations reveal, then wait for the network."""
    try:
        h = page.evaluate("document.documentElement.scrollHeight")
        y = 0
        while y < min(h, 15000):
            y += 700
            page.evaluate(f"window.scrollTo(0, {y})")
            page.wait_for_timeout(120)
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_load_state("networkidle", timeout=8000)
    except Exception:
        pass
    page.wait_for_timeout(500)


def download(url, path, limit=200 * 1024 * 1024):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (motion-design site-intel)"})
        with urllib.request.urlopen(req, timeout=40) as r, open(path, "wb") as f:
            n = 0
            while True:
                b = r.read(1 << 16)
                if not b:
                    break
                n += len(b)
                if n > limit:
                    raise IOError("too big")
                f.write(b)
        return True
    except Exception:
        if os.path.exists(path):
            os.remove(path)
        return False


def score_link(href, text):
    s = (href + " " + text).lower()
    if re.search(SKIP, s):
        return -1
    for pat, w in PRIORITY:
        if re.search(pat, s):
            return w
    return 0


PROOF = re.compile(r"[^.!?\n]{0,90}(?:\d[\d\s.,]*\s?(?:%|€|\$|k€|M€|x\b|×|heures?|h\b|min|minutes?|jours?|clients?|utilisateurs?|users?|courtiers?|entreprises?|companies|customers|fois)|\b(?:x|×)\s?\d+)[^.!?\n]{0,90}[.!?]?", re.I)
PRICE = re.compile(r"[^.\n]{0,60}(?:\d+[.,]?\d*\s?(?:€|\$|£)\s?(?:HT|TTC)?\s?(?:/|par)\s?(?:mois|an|month|year|user|utilisateur)|(?:€|\$|£)\s?\d+[.,]?\d*\s?(?:/|per)\s?(?:mo|month|year))[^.\n]{0,40}", re.I)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("project")
    ap.add_argument("--pages", type=int, default=6, help="internal pages to visit besides the home page")
    ap.add_argument("--no-video", action="store_true")
    ap.add_argument("--no-mobile", action="store_true")
    a = ap.parse_args()
    url = a.url if re.match(r"https?://", a.url) else "https://" + a.url
    P = os.path.abspath(a.project)
    if not os.path.isdir(P):
        sys.exit(f"site-intel: project folder {P} not found")
    B, UI, BR = os.path.join(P, "brand"), os.path.join(P, "assets", "ui", "site"), os.path.join(P, "assets", "brand")
    for d in (B, UI, BR, os.path.join(UI, "pages")):
        os.makedirs(d, exist_ok=True)

    from playwright.sync_api import sync_playwright
    launch = {"headless": True}
    for exe in ("/opt/pw-browsers/chromium", os.environ.get("SITE_INTEL_CHROMIUM", "")):
        if exe and os.path.isfile(exe):
            launch["executable_path"] = exe
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    host = urllib.parse.urlsplit(url).hostname or ""
    no_proxy = [x.strip().lstrip("*").lstrip(".") for x in (os.environ.get("NO_PROXY") or os.environ.get("no_proxy") or "").split(",") if x.strip()]
    local = host in ("localhost", "::1") or host.startswith("127.") or any(n and "/" not in n and (host == n or host.endswith("." + n)) for n in no_proxy)
    if proxy and not local and not os.environ.get("SITE_INTEL_NO_PROXY"):
        launch["proxy"] = {"server": proxy, "bypass": os.environ.get("NO_PROXY") or os.environ.get("no_proxy") or ""}
    pages_out, shots = [], []
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch(**launch)
        except Exception as e:
            launch.pop("executable_path", None)
            browser = pw.chromium.launch(**launch)
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1, locale="fr-FR", ignore_https_errors=True,
                                  user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36")
        page = ctx.new_page()
        try:
            resp = page.goto(url, wait_until="domcontentloaded", timeout=45000)
        except Exception as e:
            print(f"site-intel: cannot reach {url} from this machine ({str(e).splitlines()[0]})", file=sys.stderr)
            print("fallback: use WebFetch on the URL (and its /features, /pricing pages) and ask the user for screenshots"
                  " or a screen recording; see references/site-intel.md", file=sys.stderr)
            sys.exit(3)
        if resp is not None and resp.status >= 400:
            print(f"site-intel: {url} answered HTTP {resp.status}", file=sys.stderr)
            if resp.status in (401, 403, 407, 451, 503):
                sys.exit(3)
        cookie = accept_cookies(page)
        settle(page)
        home = page.evaluate(EXTRACT_JS)
        home["cookie_clicked"] = cookie
        pages_out.append(home)

        # screenshots of the home page: full page (capped), viewport slices, hero
        hpx = min(home.get("height") or 900, 14000)
        page.screenshot(path=os.path.join(UI, "home-hero.png"))
        shots.append("assets/ui/site/home-hero.png")
        try:
            page.screenshot(path=os.path.join(UI, "home-full.png"), full_page=True, clip={"x": 0, "y": 0, "width": 1440, "height": hpx})
            shots.append("assets/ui/site/home-full.png")
        except Exception:
            pass
        for i, y in enumerate(range(0, hpx, 900)):
            if i >= 14:
                break
            page.evaluate(f"window.scrollTo(0, {y})")
            page.wait_for_timeout(350)
            f = f"home-{i + 1:02d}.png"
            page.screenshot(path=os.path.join(UI, f))
            shots.append(f"assets/ui/site/{f}")
        page.evaluate("window.scrollTo(0, 0)")

        # logo candidates
        logos = []
        if home.get("logoSvg"):
            open(os.path.join(BR, "logo-header.svg"), "w", encoding="utf-8").write(home["logoSvg"])
            logos.append("assets/brand/logo-header.svg")
        cands = [("logo-header", home.get("logoImg")), ("og-image", (home.get("meta") or {}).get("og:image"))]
        for ic in home.get("icons", []):
            cands.append(("apple-touch-icon" if "apple" in " ".join(ic.get("rel") or []) else "favicon", ic.get("href")))
        seen = set()
        for name, u in cands:
            if not u or u in seen or u.startswith("data:"):
                continue
            u = urllib.parse.urljoin(home["url"], u)
            seen.add(u)
            ext = os.path.splitext(urllib.parse.urlsplit(u).path)[1][:5] or ".png"
            f = os.path.join(BR, f"{name}{ext}")
            if os.path.exists(f):
                f = os.path.join(BR, f"{name}-{len(seen)}{ext}")
            if download(u, f, 20 * 1024 * 1024):
                logos.append(os.path.relpath(f, P))

        # mobile
        if not a.no_mobile:
            m = browser.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True, locale="fr-FR", ignore_https_errors=True)
            mp = m.new_page()
            try:
                mp.goto(url, wait_until="domcontentloaded", timeout=45000)
                accept_cookies(mp)
                settle(mp)
                mp.screenshot(path=os.path.join(UI, "mobile-hero.png"))
                mh = min(mp.evaluate("document.documentElement.scrollHeight"), 9000)
                mp.screenshot(path=os.path.join(UI, "mobile-full.png"), full_page=True, clip={"x": 0, "y": 0, "width": 390, "height": mh})
                shots += ["assets/ui/site/mobile-hero.png", "assets/ui/site/mobile-full.png"]
            except Exception:
                pass
            m.close()

        # internal pages, best first
        cand = {}
        for l in home.get("links", []):
            h = l.get("href")
            if not h or not h.startswith("http") or not same_site(h, url):
                continue
            n = norm_url(h)
            if n == norm_url(url) or "#" in h and norm_url(h.split("#")[0]) == norm_url(url):
                continue
            sc = score_link(n, l.get("text", ""))
            if sc < 0:
                continue
            sc += 2 if l.get("nav") else 0
            if sc >= 0:
                cand[n] = max(cand.get(n, -1), sc)
        for n, sc in sorted(cand.items(), key=lambda kv: -kv[1])[:a.pages]:
            try:
                r = page.goto(n, wait_until="domcontentloaded", timeout=30000)
                if r is not None and r.status >= 400:
                    print(f"  skipped {n}: HTTP {r.status}")
                    continue
                accept_cookies(page)
                settle(page)
                d = page.evaluate(EXTRACT_JS)
                d.pop("links", None)
                slugp = re.sub(r"[^a-z0-9]+", "-", urllib.parse.urlsplit(n).path.lower()).strip("-")[:50] or "page"
                page.screenshot(path=os.path.join(UI, "pages", f"{slugp}-1.png"))
                page.evaluate("window.scrollTo(0, 900)")
                page.wait_for_timeout(350)
                page.screenshot(path=os.path.join(UI, "pages", f"{slugp}-2.png"))
                shots += [f"assets/ui/site/pages/{slugp}-1.png", f"assets/ui/site/pages/{slugp}-2.png"]
                d["score"] = sc
                pages_out.append(d)
            except Exception as e:
                print(f"  skipped {n}: {str(e).splitlines()[0]}")
        browser.close()

    # videos (direct files only; embeds are listed)
    vids = []
    for p in pages_out:
        for v in p.get("videos", []):
            if v["src"] in [x["src"] for x in vids]:
                continue
            item = dict(v)
            if not v.get("embed") and not a.no_video and re.search(r"\.(mp4|webm|mov)(\?|$)", v["src"], re.I):
                os.makedirs(os.path.join(UI, "video"), exist_ok=True)
                f = os.path.join(UI, "video", f"video-{len(vids) + 1:02d}" + re.search(r"\.(mp4|webm|mov)", v["src"], re.I).group(0).lower())
                if download(v["src"], f):
                    item["file"] = os.path.relpath(f, P)
            vids.append(item)

    # palette
    bg, fg, ctabg, fonts = Counter(), Counter(), Counter(), Counter()
    for p in pages_out:
        if rgb_to_hex(p.get("bodyBg")):
            bg[rgb_to_hex(p["bodyBg"])] += 1920 * 3000
        elif p.get("bodyBg"):
            bg["#ffffff"] += 1920 * 3000
        for k, v in (p.get("bg") or {}).items():
            h = rgb_to_hex(k)
            if h:
                bg[h] += v
        for k, v in (p.get("fg") or {}).items():
            h = rgb_to_hex(k)
            if h:
                fg[h] += v
        for c in p.get("ctas", []):
            h = rgb_to_hex(c.get("bg"))
            if h:
                ctabg[h] += 1
        for k, v in (p.get("fonts") or {}).items():
            fonts[k] += v
    chroma = lambda h: sat_light(h)[0] > 0.35 and 0.18 < sat_light(h)[1] < 0.82
    accent = None
    for pool in (ctabg, fg, bg):
        for h, _ in pool.most_common():
            if chroma(h):
                accent = h
                break
        if accent:
            break
    heading = [k.split("|")[0] for k, _ in fonts.most_common() if k.endswith("|heading")]
    texts = [k.split("|")[0] for k, _ in fonts.most_common() if k.endswith("|text")]
    disp = heading[0] if heading else (texts[0] if texts else None)
    free = lambda fam: (FREE_FONTS.get((fam or "").lower(), fam) if fam else None)
    serif_guess = next((f for f in heading + texts if re.search(r"serif|garamond|playfair|fraunces|tiempos|canela|recoleta|georgia|times|lora|merriweather", f, re.I)
                        and not re.search(r"sans", f, re.I)), None)
    palette = {
        "accent": accent, "background": [h for h, _ in bg.most_common(6)], "text": [h for h, _ in fg.most_common(6)],
        "cta": [h for h, _ in ctabg.most_common(4)],
        "fonts": {"display_site": disp, "display_free": free(disp), "text_site": texts[0] if texts else None,
                  "serif_site": serif_guess, "serif_free": free(serif_guess) if serif_guess else None},
    }
    json.dump(palette, open(os.path.join(B, "palette.json"), "w"), indent=2, ensure_ascii=False)
    json.dump({"url": url, "fetched": time.strftime("%Y-%m-%d %H:%M"), "pages": pages_out, "videos": vids, "logos": logos,
               "screenshots": shots}, open(os.path.join(B, "site.json"), "w"), indent=1, ensure_ascii=False)

    # dossier
    home = pages_out[0]
    meta = home.get("meta") or {}
    name = (meta.get("og:site_name") or re.split(r"\s[|\-–—·:]\s", home.get("title") or "")[0] or urllib.parse.urlsplit(url).netloc).strip()
    L = [f"# Dossier marque : {name}", "", f"Source : {url} (visité le {time.strftime('%Y-%m-%d')}, {len(pages_out)} pages). "
         "Tout ce qui est entre guillemets est copié du site, mot pour mot : c'est la seule matière autorisée pour les chiffres.", ""]
    L += ["## Identité", f"- Nom : {name}", f"- Titre de la page : {home.get('title')}", f"- Description : {meta.get('description') or meta.get('og:description') or '—'}",
          f"- Langue : {home.get('lang') or '—'}", ""]
    h1 = [h for h in home.get("headings", []) if h["level"] == 1]
    L += ["## Promesse (haut de la page d'accueil)"]
    for h in (h1 or home.get("headings", [])[:1])[:2]:
        L.append(f"- H1 : « {h['text']} »" + (f"\n  - sous-titre : « {h['para']} »" if h.get("para") else ""))
    L.append("")
    L += ["## Sections et fonctionnalités (titres H2/H3 + texte qui suit, par page)"]
    for p in pages_out:
        hs = [h for h in p.get("headings", []) if h["level"] in (2, 3)][:18]
        if not hs:
            continue
        L.append(f"### {p.get('title') or p['url']}  \n{p['url']}")
        for h in hs:
            L.append(f"- {'##' if h['level'] == 2 else '###'} « {h['text']} »" + (f" — « {h['para'][:220]} »" if h.get("para") else ""))
    L.append("")
    proofs, prices = [], []
    for p in pages_out:
        for m in PROOF.finditer(p.get("text") or ""):
            s = re.sub(r"\s+", " ", m.group(0)).strip()
            if 12 < len(s) < 200 and s not in [x[0] for x in proofs]:
                proofs.append((s, p["url"]))
        for m in PRICE.finditer(p.get("text") or ""):
            s = re.sub(r"\s+", " ", m.group(0)).strip()
            if s not in [x[0] for x in prices]:
                prices.append((s, p["url"]))
    L += ["## Preuves chiffrées (verbatim, à vérifier avec le client avant de les mettre dans le film)"]
    L += [f"- « {s} » ({u})" for s, u in proofs[:25]] or ["- aucune trouvée : ne mettre aucun chiffre dans le film"]
    L += ["", "## Tarifs repérés"] + ([f"- « {s} » ({u})" for s, u in prices[:10]] or ["- aucun"])
    quotes = []
    for p in pages_out:
        for t in p.get("paragraphs", []):
            if re.search(r"^[«\"“]|[»\"”]$|témoign|testimon", t, re.I) and len(t) < 400 and t not in quotes:
                quotes.append(t)
    L += ["", "## Témoignages / citations"] + ([f"- « {q} »" for q in quotes[:8]] or ["- aucun repéré"])
    ctas = Counter(c["text"] for p in pages_out for c in p.get("ctas", []) if 2 < len(c["text"]) < 40)
    L += ["", "## Appels à l'action (boutons, par fréquence)"] + [f"- « {t} » ×{n}" for t, n in ctas.most_common(8)]
    alltext = " ".join(p.get("text") or "" for p in pages_out)
    vous, tu = len(re.findall(r"\bvous\b", alltext, re.I)), len(re.findall(r"\b(tu|ton|ta|tes)\b", alltext, re.I))
    L += ["", "## Ton", f"- Adresse : {'vouvoiement' if vous >= tu else 'tutoiement'} (vous ×{vous}, tu ×{tu})",
          f"- Longueur moyenne des titres : {round(sum(len(h['text'].split()) for p in pages_out for h in p.get('headings', [])) / max(1, sum(len(p.get('headings', [])) for p in pages_out)), 1)} mots"]
    L += ["", "## Palette mesurée (theme.py --from-site l'applique)",
          f"- Accent retenu : {accent or 'aucune couleur vive trouvée : choisir avec le client'}",
          f"- Couleurs des boutons : {', '.join(palette['cta']) or '—'}",
          f"- Fonds dominants : {', '.join(palette['background'][:5])}", f"- Textes dominants : {', '.join(palette['text'][:4])}",
          "", "## Typographie",
          f"- Titres du site : {disp or '—'} → équivalent libre : {free(disp) or '—'}",
          f"- Texte du site : {palette['fonts']['text_site'] or '—'}",
          f"- Serif repérée : {serif_guess or 'aucune'}"]
    L += ["", "## Matière visuelle récupérée", f"- Logos : {', '.join(logos) or 'aucun (demander un SVG)'}",
          f"- Captures : {len(shots)} fichiers dans assets/ui/site/ (home-hero, home-01…, mobile-*, pages/*)",
          "- Vidéos : " + (", ".join((v.get("file") or v["src"]) for v in vids) if vids else "aucune (demander un enregistrement d'écran du produit)")]
    imgs = sorted({i["src"]: i for p in pages_out for i in p.get("imgs", []) if i.get("w", 0) >= 800 and not i.get("header")}.values(),
                  key=lambda i: -i.get("area", 0))[:12]
    if imgs:
        L += ["- Grandes images du site (souvent des captures du produit) :"] + [f"  - {i['src']} ({i['w']}×{i['h']}) {i.get('alt') or ''}" for i in imgs]
    L += ["", "## Questions ouvertes pour le client",
          "- Qui exactement regarde le film, et quelle est sa douleur n°1 dans ses mots ?",
          "- Quels chiffres ci-dessus peut-on citer (preuve à l'appui) ?",
          "- Le logo en SVG, la prononciation du nom, la date de diffusion, le format (16:9 site / 9:16 réseaux).",
          "- Un enregistrement d'écran récent du produit (1-3 min) : c'est la meilleure matière du film."]
    open(os.path.join(B, "BRAND.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"site-intel: {len(pages_out)} pages, {len(shots)} screenshots, {len(logos)} logo files, {len(vids)} videos")
    print(f"  accent {accent}, display font {disp} -> {free(disp)}")
    print(f"  dossier: {os.path.join(B, 'BRAND.md')}")


if __name__ == "__main__":
    main()
