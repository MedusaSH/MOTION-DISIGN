# Site intel: from a URL to a brand dossier

`scripts/site-intel.py <url> <project> [--pages 6] [--no-video] [--no-mobile]` (called by `setup-kinetic.sh --url`).

## What it does
1. Opens the site in headless Chromium (desktop 1440×900, French locale), clicks the cookie banner, scrolls the page
   to trigger lazy content and scroll animations.
2. Extracts the home page: title, meta / Open Graph, language, H1-H3 with the paragraph that follows, paragraphs,
   buttons (text + color), links, images (size, position), videos (direct files and YouTube/Vimeo/Loom embeds),
   JSON-LD, favicon / apple-touch-icon, the header logo (inline SVG or image), computed colors (area-weighted
   backgrounds, text-weighted text colors, button backgrounds) and computed font families (headings vs text).
3. Visits the best internal pages (features / product / pricing / demo / customers / about / security…, never login,
   legal, cart, blog posts) and extracts the same.
4. Screenshots: `home-hero.png`, `home-full.png`, `home-01…14.png` (viewport slices), `mobile-hero.png`,
   `mobile-full.png` (390×844 @2x), `pages/<slug>-1/2.png`. Downloads logos, og:image, direct demo videos (≤ 200 MB).
5. Writes `brand/BRAND.md`, `brand/site.json`, `brand/palette.json` (accent = the most used saturated button color,
   else text, else background; fonts mapped to a free equivalent on npm @fontsource when proprietary).

## How to use the dossier
- BRAND.md is raw material, not truth: proofs are verbatim with their URL; ask the user which ones may be quoted.
  No number in the film that is not in BRAND.md and confirmed.
- LOOK at the screenshots before writing: they show the product, its UI, its tone. The most useful shots for the film:
  the product UI (dashboards, apps, chats), the hero, the pricing, the mobile view.
- Demo video found → it is the best UI material: stills every 0.5 s (`ffmpeg -i video-01.mp4 -vf fps=2,scale=1440:-1
  assets/ui/demo/vn-%02d.jpg`), swapped discretely in a 3D glass frame (never redrawn).
- Palette: `theme.py --from-site` applies it; check the printed contrasts (accent on night ≥ 3:1, on paper ≥ 2.6:1);
  if the site has no saturated color (black/white brand), use `--preset mono` and pick the accent with the user.
- Fonts: the site's display family is used when free on npm, else its free equivalent (Helvetica/SF → Inter,
  Circular → Plus Jakarta Sans, Tiempos → Fraunces…). Override with `--display/--serif`.

## Fallback when the site is unreachable (exit code 3, blocked network, bot protection)
1. Use the WebFetch tool on the home page and on /features, /pricing, /about (or the real paths from its links);
   write the same sections of BRAND.md by hand from what it returns (quotes verbatim + URL).
2. Ask the user for: 5-10 screenshots of the product and the site (desktop + mobile), the logo (SVG), the brand color
   (hex), and ideally a 1-3 min screen recording of the product. Put them in `assets/ui/site/` and `assets/brand/`.
3. `theme.py <project> --accent "#hex" [--display "<Family>"]`.
Never invent screenshots or numbers to fill the gap.
