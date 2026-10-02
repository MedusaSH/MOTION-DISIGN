"""Board of the 9 direction styleframes -> styleframes/png/directions.png"""
import pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent
D = [("A", "Le bureau du soir", "recommandée · storyboard déjà écrit", [("A1", "6.30 s · le gag : 22:47, fiche vide"), ("A2", "15.50 s · fiche de conseil, case par case"), ("A3", "25.50 s · le vrai écran Synapze se remplit")]),
     ("B", "Le fil de la soirée", "une ligne du temps qui devient la voix", [("B1", "0.80 s · 19:00 sur le fil"), ("B2", "11.50 s · la soirée hachurée, les fiches"), ("B3", "25.50 s · le fil devient l'onde")]),
     ("C", "Tout dans le téléphone", "voice-first, WhatsApp au centre", [("C1", "0.80 s · l'écran verrouillé, 19:00"), ("C2", "17.50 s · samedi 21:14, sans réponse"), ("C3", "31.00 s · WhatsApp répond, 03:12")])]
rows = "".join(f'<section><h2><b>{l}</b> « {n} » <span>{s}</span></h2><div class="g">' + "".join(f'<figure><img src="png/{k}.png"><figcaption><b>{k}</b> {c}</figcaption></figure>' for k, c in im) + '</div></section>' for l, n, s, im in D)
(HERE / "directions.html").write_text(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:DMS;src:url(../assets/fonts/DMSans-500.woff2)}}@font-face{{font-family:DMM;src:url(../assets/fonts/DMMono-400.woff2)}}@font-face{{font-family:Ser;src:url(../assets/fonts/DMSerifDisplay-400.woff2)}}
body{{margin:0;background:#0A0F1A;color:#F1EBDE;font-family:DMS;width:2400px;padding:50px 60px;box-sizing:border-box}}
h1{{font:400 56px Ser;margin:0 0 40px}}h1 span,b{{color:#F24E1E}}h2{{font:400 42px Ser;margin:0 0 18px}}h2 span{{font:20px DMM;color:#9AA3B4;margin-left:16px}}
section{{margin-bottom:50px}}.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}}figure{{margin:0}}img{{width:100%;display:block;border-radius:6px}}
figcaption{{margin-top:10px;font-size:22px}}figcaption b{{font:500 22px DMM;margin-right:8px}}
</style></head><body><h1><span>•</span> Synapze <span>•</span> Trois directions</h1>{rows}</body></html>''', encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 2400, "height": 1000})
    pg.goto((HERE / "directions.html").resolve().as_uri()); pg.wait_for_timeout(500)
    pg.screenshot(path=str(HERE / "png" / "directions.png"), full_page=True); b.close()
