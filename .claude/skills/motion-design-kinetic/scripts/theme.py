#!/usr/bin/env python3
"""Apply a brand theme (palette + fonts) to a kinetic project, in one command.

Rewrites, in <project>:
  - reference/fx.html      the THEME block (CSS variables read by the whole FX kit) + @font-face of custom fonts
  - assemble.sh            ACCENT, ACCENT_LIGHT, ACCENT_GLOW, PAPER (orchestrator flash / paper bed)
  - frame.md               the colors: block (accent family, night, paper)
  - theme.json             what was applied (the frame agents and you can read it)

Usage:
  python3 theme.py <project> --accent "#2F6BFF"                       # derive the whole family from one color
  python3 theme.py <project> --from-site                              # accent + fonts from brand/palette.json (site-intel.py)
  python3 theme.py <project> --accent "#16A34A" --preset foret        # grounds preset
  python3 theme.py <project> --accent "#7C3AED" --display "Inter" --serif "Fraunces"   # fonts from npm @fontsource
  python3 theme.py --list-presets
Fonts: any family published as @fontsource-variable/<slug> or @fontsource/<slug> (Google Fonts, SIL OFL) is fetched
with `npm pack` (works where font CDNs are blocked). Default fonts: Geist / Instrument Serif / Geist Mono.
"""
import argparse
import colorsys
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

PRESETS = {
    # name: (night, night_mid, paper, ink_dark, mute)  -- the night tint and paper blobs are derived from the accent
    "nuit-papier": ("#050507", "#0b0b0e", "#f6f1ea", "#0c0c0f", "#9a948c"),   # warm paper (Synapze v2)
    "encre": ("#04060d", "#0a0d18", "#f3f5fa", "#0a0e1a", "#8f96a8"),         # cold blue night, cool paper (tech, fintech)
    "foret": ("#040a07", "#0a120d", "#f2f4ee", "#0b120d", "#8d978f"),         # green-black, sage paper (health, green)
    "mono": ("#000000", "#0a0a0a", "#ffffff", "#000000", "#8a8a8a"),          # pure black / white (luxury, editorial)
    "creme": ("#0d0a07", "#16110c", "#fbf6ee", "#17120c", "#9c9183"),         # brown night, cream (food, craft, retail)
}


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        sys.exit(f"theme: invalid color '{h}'")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#" + "".join(f"{max(0, min(255, round(c))):02x}" for c in rgb)


def mix(a, b, t):
    """t=0 -> a, t=1 -> b"""
    ra, rb = hex_to_rgb(a), hex_to_rgb(b)
    return rgb_to_hex(tuple(x + (y - x) * t for x, y in zip(ra, rb)))


def hls_shift(h, dl=0.0, ds=0.0, dh=0.0):
    r, g, b = (c / 255 for c in hex_to_rgb(h))
    hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
    r, g, b = colorsys.hls_to_rgb((hh + dh) % 1, min(1, max(0, ll + dl)), min(1, max(0, ss + ds)))
    return rgb_to_hex((r * 255, g * 255, b * 255))


def luminance(h):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = hex_to_rgb(h)
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def derive(accent, preset):
    night, night_mid, paper, ink_dark, mute = PRESETS[preset]
    # an accent too dark to glow on night, or too pale to read on paper, is pushed into the usable band
    acc = accent
    for _ in range(12):
        if contrast(acc, night) < 3.2:
            acc = hls_shift(acc, dl=+0.04)
        elif contrast(acc, paper) < 2.6:
            acc = hls_shift(acc, dl=-0.04)
        else:
            break
    return {
        "night": night, "night-mid": night_mid, "night-tint": mix(night, acc, 0.10),
        "paper": paper, "blob-1": mix(paper, acc, 0.26), "blob-2": mix(paper, acc, 0.38),
        "ink": paper, "ink-dark": ink_dark, "mute": mute,
        "accent": acc, "accent-hot": hls_shift(acc, dl=+0.07, ds=+0.05), "accent-light": mix(acc, "#ffffff", 0.45),
        "accent-deep": hls_shift(acc, dl=-0.16), "accent-pale": mix(acc, "#ffffff", 0.70),
        "accent-rgb": " ".join(str(c) for c in hex_to_rgb(acc)),
        "accent-input": accent,
    }


def slug(family):
    return re.sub(r"[^a-z0-9]+", "-", family.lower()).strip("-")


def fetch_font(family, dst_fonts, italic_too=False):
    """Fetch a font family from npm (@fontsource-variable, else @fontsource). Returns @font-face CSS or None."""
    s = slug(family)
    os.makedirs(dst_fonts, exist_ok=True)
    tmp = tempfile.mkdtemp()
    try:
        for pkg, variable in ((f"@fontsource-variable/{s}", True), (f"@fontsource/{s}", False)):
            r = subprocess.run(["npm", "pack", "-q", pkg], cwd=tmp, capture_output=True, text=True)
            tgz = [f for f in os.listdir(tmp) if f.endswith(".tgz")]
            if r.returncode != 0 or not tgz:
                continue
            subprocess.run(["tar", "-xzf", tgz[0]], cwd=tmp, check=True)
            files = os.path.join(tmp, "package", "files")
            css = []
            if variable:
                cands = sorted((f for f in os.listdir(files) if f.endswith(".woff2") and "-latin-" in f and "-ext-" not in f),
                               key=lambda f: (0 if "-wght-" in f else 1 if "-standard-" in f else 2, f))
                done = set()
                for f in cands:
                    style = "italic" if "italic" in f else "normal"
                    if style in done or (style == "italic" and not italic_too):
                        continue
                    done.add(style)
                    out = f"{s}-var-{style}.woff2"
                    shutil.copy(os.path.join(files, f), os.path.join(dst_fonts, out))
                    css.append(f'@font-face {{ font-family: "{family}"; src: url("../assets/fonts/{out}") format("woff2"); font-weight: 100 900; font-style: {style}; }}')
            else:
                for w in (400, 500, 600, 700, 800, 900):
                    for style in ("normal", "italic") if italic_too else ("normal",):
                        f = f"{s}-latin-{w}-{style}.woff2"
                        if os.path.exists(os.path.join(files, f)):
                            out = f"{s}-{w}-{style}.woff2"
                            shutil.copy(os.path.join(files, f), os.path.join(dst_fonts, out))
                            css.append(f'@font-face {{ font-family: "{family}"; src: url("../assets/fonts/{out}") format("woff2"); font-weight: {w}; font-style: {style}; }}')
            if css:
                return "\n".join(css)
        return None
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project", nargs="?")
    ap.add_argument("--accent")
    ap.add_argument("--preset", default="nuit-papier", choices=sorted(PRESETS))
    ap.add_argument("--from-site", action="store_true", help="read brand/palette.json written by site-intel.py")
    ap.add_argument("--display", help="display font family (kinetic type, captions, UI)")
    ap.add_argument("--serif", help="emotion font family (one word per beat, italic if available)")
    ap.add_argument("--mono", help="label font family")
    ap.add_argument("--list-presets", action="store_true")
    a = ap.parse_args()
    if a.list_presets:
        for k, v in PRESETS.items():
            print(f"{k:12s} night {v[0]}  paper {v[2]}")
        return
    if not a.project:
        ap.error("project required")
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    P = a.project if os.path.isabs(a.project) else os.path.join(os.getcwd(), a.project)
    if not os.path.isdir(P):
        P = os.path.join(root, a.project)
    fx = os.path.join(P, "reference", "fx.html")
    if not os.path.exists(fx):
        sys.exit(f"theme: {fx} missing (run setup-kinetic.sh first)")

    accent, display, serif, mono = a.accent, a.display, a.serif, a.mono
    if a.from_site:
        pal_f = os.path.join(P, "brand", "palette.json")
        if not os.path.exists(pal_f):
            sys.exit("theme: brand/palette.json missing (run site-intel.py first)")
        pal = json.load(open(pal_f, encoding="utf-8"))
        accent = accent or pal.get("accent")
        fonts = pal.get("fonts", {})
        display = display or fonts.get("display_free")
        serif = serif or fonts.get("serif_free")
    if not accent:
        sys.exit("theme: give --accent '#RRGGBB' (or --from-site)")

    t = derive(accent, a.preset)
    faces = []
    fam = {"display": "Geist", "serif": "Instrument Serif", "mono": "Geist Mono"}
    for role, family, italic in (("display", display, False), ("serif", serif, True), ("mono", mono, False)):
        if family and family not in ("Geist", "Instrument Serif", "Geist Mono"):
            css = fetch_font(family, os.path.join(P, "assets", "fonts"), italic_too=italic)
            if css:
                faces.append(css)
                fam[role] = family
                print(f"font {role}: {family} (npm @fontsource)")
            else:
                print(f"font {role}: '{family}' not found on npm @fontsource, keeping {fam[role]}")

    block = ("/* THEME:start (scripts/theme.py rewrites this block: palette + fonts of the brand) */\n"
             + ("\n".join(faces) + "\n" if faces else "")
             + ".fx-stage {\n"
             f"  --fx-night: {t['night']}; --fx-night-mid: {t['night-mid']}; --fx-night-tint: {t['night-tint']};\n"
             f"  --fx-paper: {t['paper']}; --fx-blob-1: {t['blob-1']}; --fx-blob-2: {t['blob-2']};\n"
             f"  --fx-ink: {t['ink']}; --fx-ink-dark: {t['ink-dark']}; --fx-mute: {t['mute']};\n"
             f"  --fx-accent: {t['accent']}; --fx-accent-hot: {t['accent-hot']}; --fx-accent-light: {t['accent-light']}; --fx-accent-deep: {t['accent-deep']}; --fx-accent-pale: {t['accent-pale']};\n"
             f"  --fx-accent-rgb: {t['accent-rgb']};\n"
             f"  --fx-font-display: \"{fam['display']}\"; --fx-font-serif: \"{fam['serif']}\"; --fx-font-mono: \"{fam['mono']}\";\n"
             "}\n/* THEME:end */")
    s = open(fx, encoding="utf-8").read()
    s2, n = re.subn(r"/\* THEME:start.*?/\* THEME:end \*/", lambda m: block, s, flags=re.S)
    if n != 1:
        sys.exit("theme: THEME block not found in reference/fx.html (old kit? re-run setup-kinetic.sh)")
    open(fx, "w", encoding="utf-8").write(s2)

    asm = os.path.join(P, "assemble.sh")
    if os.path.exists(asm):
        s = open(asm, encoding="utf-8").read()
        for k, v in (("ACCENT", t["accent"]), ("ACCENT_LIGHT", t["accent-light"]), ("ACCENT_GLOW", t["accent-pale"]), ("PAPER", t["paper"])):
            s = re.sub(rf'(?m)^{k}="[^"]*"', f'{k}="{v}"', s)
        open(asm, "w", encoding="utf-8").write(s)

    fm = os.path.join(P, "frame.md")
    if os.path.exists(fm):
        s = open(fm, encoding="utf-8").read()
        for k, v in (("night", t["night"]), ("paper", t["paper"]), ("ink-dark", t["ink-dark"]), ("mute", t["mute"]),
                     ("accent", t["accent"]), ("accent-hot", t["accent-hot"]), ("accent-light", t["accent-light"]), ("accent-deep", t["accent-deep"])):
            s = re.sub(rf'(?m)^(  {re.escape(k)}: )"[^"]*"', rf'\g<1>"{v}"', s)
        s = s.replace("{{DISPLAY_FONT}}", fam["display"]).replace("{{SERIF_FONT}}", fam["serif"]).replace("{{MONO_FONT}}", fam["mono"])
        s = s.replace('"{{ACCENT}}"', f'"{t["accent"]}"').replace('"{{ACCENT_HOT}}"', f'"{t["accent-hot"]}"')
        s = s.replace('"{{ACCENT_LIGHT}}"', f'"{t["accent-light"]}"').replace('"{{ACCENT_DEEP}}"', f'"{t["accent-deep"]}"')
        open(fm, "w", encoding="utf-8").write(s)

    json.dump({"preset": a.preset, "palette": t, "fonts": fam}, open(os.path.join(P, "theme.json"), "w"), indent=2)
    print(f"theme applied to {P}: accent {t['accent']} (asked {accent}), preset {a.preset}, fonts {fam}")
    print(f"contrast accent/night {contrast(t['accent'], t['night']):.1f}:1, accent/paper {contrast(t['accent'], t['paper']):.1f}:1, "
          f"ink/night {contrast(t['ink'], t['night']):.1f}:1")


if __name__ == "__main__":
    main()
