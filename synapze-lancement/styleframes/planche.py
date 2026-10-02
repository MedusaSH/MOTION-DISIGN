"""Contact board of the styleframes: python3 styleframes/planche.py (from the project folder) -> styleframes/png/planche.png"""
import html, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent
P = [("P01","0.00 → 1.50","Mardi, 19 h : l'agenda, le téléphone à 19:00"),
("P02","1.50 → 3.70","Le RDV de 18:00 se coche et part hors champ"),
("P03","3.70 → 5.50","L'ordinateur s'allume sur une fiche vide"),
("P04","5.50 → 7.40","GAG muet : 19:00 → 22:47, la tasse se vide"),
("P05","7.40 → 9.30","Les notes du RDV : « → conseil »"),
("P06","9.30 → 10.20","« Pas la saisie » : les touches s'enfoncent"),
("P07","10.20 → 13.20","Il retape ses notes, les fiches s'empilent"),
("P08","13.20 → 16.20","Fiche de conseil Word, cochée case par case"),
("P09","16.20 → 18.50","Samedi 21:14 : le prospect écrit"),
("P10","18.50 → 19.50","La date roule jusqu'à lundi, sans réponse"),
("P11","19.50 → 21.95","PIVOT sur noir ; le caret efface la phrase"),
("P12","21.95 → 23.75","Flash : le caret devient la note vocale"),
("P13","23.75 → 26.70","Vrai écran Synapze : la fiche se remplit (IA)"),
("P14","26.70 → 29.65","La fiche de conseil se coche seule, tampon d'audit"),
("P15","29.65 → 32.95","WhatsApp : l'assistant répond à 21:14"),
("P16","32.95 → 36.45","Le bureau rangé, 19:05 ; implosion"),
("P17","36.45 → 37.35","Le logo • Synapze • s'assemble"),
("P18","37.35 → 39.75","La promesse, comme le haut du site"),
("P19","39.75 → 43.80","Clic sur « Demander une démo », iris")]
acts = {"P01":"ACCROCHE","P04":"GAG","P05":"DOULEURS","P11":"PIVOT","P12":"SOLUTION","P17":"FIN"}
cells = "".join(f'<figure><img src="png/{k}.png"><figcaption><b>{k}</b><span>{t} s</span>{"<em>"+acts[k]+"</em>" if k in acts else ""}<p>{html.escape(d)}</p></figcaption></figure>' for k, t, d in P)
(HERE / "planche.html").write_text(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:DMS;src:url(../assets/fonts/DMSans-500.woff2)}}@font-face{{font-family:DMM;src:url(../assets/fonts/DMMono-400.woff2)}}@font-face{{font-family:Ser;src:url(../assets/fonts/DMSerifDisplay-400.woff2)}}
body{{margin:0;background:#0A0F1A;color:#F1EBDE;font-family:DMS;width:2400px;padding:50px 60px;box-sizing:border-box}}
h1{{font:400 56px Ser;margin:0 0 6px}}h1 span{{color:#F24E1E}}.s{{font:20px DMM;color:#9AA3B4;margin-bottom:40px;letter-spacing:1px}}
.g{{display:grid;grid-template-columns:repeat(4,1fr);gap:34px 30px}}figure{{margin:0}}img{{width:100%;display:block;border-radius:6px}}
figcaption{{margin-top:12px;font-size:21px;line-height:1.35}}b{{color:#F24E1E;font:500 22px DMM;margin-right:12px}}span{{font:18px DMM;color:#9AA3B4}}
em{{font:500 15px DMM;font-style:normal;margin-left:12px;padding:3px 8px;border:1px solid #F24E1E;color:#F24E1E;border-radius:4px}}p{{margin:6px 0 0}}
</style></head><body><h1><span>•</span> Synapze <span>•</span> Storyboard · planche</h1><div class="s">19 PLANS · 43,8 S · 16:9 · VOIX YANN · IMAGE CLÉ DE CHAQUE PLAN · P13 = VRAIE INTERFACE · WHATSAPP À REMPLACER PAR UNE CAPTURE</div><div class="g">{cells}</div></body></html>''', encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 2400, "height": 1000})
    pg.goto((HERE / "planche.html").resolve().as_uri()); pg.wait_for_timeout(500)
    pg.screenshot(path=str(HERE / "png" / "planche.png"), full_page=True); b.close()
