"""Generate one styleframe HTML per shot (P01 to P19) of STORYBOARD.md, at its key-image time.
Run: python3 styleframes/build.py, then render-styleframes.py synapze-lancement, then the board (planche)."""
import pathlib

OUT = pathlib.Path(__file__).parent


def at(x, y, s=1.0, r=0, cls="", extra=""):
    return f'class="o {cls}" style="left:{x}px;top:{y}px;transform:scale({s}) rotate({r}deg);transform-origin:0 0;{extra}"'


def page(world, body, sub=""):
    lamp = " lamp" if world == "dark" else ""
    s = f'<div class="scrim"></div><div class="sub">{sub}</div>' if sub else ""
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><link rel="stylesheet" href="sf.css"></head>
<body><div class="stage {world}{lamp}">{body}{s}</div></body></html>"""


def agenda(x, y, s=1, checked=False, tab=True, tabx=0, cls=""):
    rows = ""
    for h, t in [("14:00", "Point portefeuille"), ("15:30", "Signature Martin · auto"),
                 ("16:30", "Appel assureur"), ("18:00", None)]:
        if t is None:
            ck = '<div class="ck on"></div>' if checked else '<div class="ck"></div>'
            label = (f'<div class="tab" style="transform:translateX({tabx}px) rotate({-8 if tabx else 0}deg);'
                     f'{"filter:blur(10px);opacity:.8" if tabx else ""}">RDV M. Lebrun · mutuelle famille</div>'
                     if tab else "")
            rows += f'<div class="row"><div class="h">{h}</div>{ck}{label}</div>'
        else:
            rows += f'<div class="row"><div class="h">{h}</div><div class="ck on" style="opacity:.45"></div><span style="opacity:.55">{t}</span></div>'
    return f'<div {at(x, y, s, 0, "agenda sh " + cls)}><h1>Mardi</h1><div class="date">MARDI 12 · SEMAINE 42</div>{rows}</div>'


def phone(x, y, s=1, content="", r=0, cls=""):
    return f'<div {at(x, y, s, r, "phone sh " + cls)}><div class="scr">{content}</div></div>'


def lock(date, time, notif="", grey=False):
    n = ""
    if notif:
        n = (f'<div class="notif{" grey" if grey else ""}" style="top:300px"><div class="app"><i></i>WHATSAPP · {"lun." if grey else "21:14"}</div>'
             f'<b>Camille R.</b><br>Bonjour, je cherche une mutuelle pour ma famille. Vous pouvez me faire un devis ?</div>')
    return f'<div class="lock" style="height:100%"><div class="d">{date}</div><div class="t">{time}</div>{n}</div>'


def crm(fields, note=False, wave=False, title="Nouveau prospect", caret_on=None, brand=False):
    f = ""
    for i, (k, v) in enumerate(fields):
        car = '<span class="caret"></span>' if caret_on == i else ""
        f += f'<div class="field"><div class="k">{k}</div><div class="v{" on" if car else ""}">{v}{car}</div></div>'
    side = ('<div class="side"><div class="lg">Synapze</div>' if brand else '<div class="side"><div style="font:500 16px DM Mono;letter-spacing:2px;color:#9AA3B4;margin-bottom:8px">MON CRM</div>') + '<i class="on"></i><i></i><i></i><i></i><i></i></div>'
    if note:
        bars = "".join(f'<i style="height:{20 + (i * 37 % 70)}px"></i>' for i in range(30))
        left = (f'<div style="width:420px;margin-right:40px"><div class="lbl">Note vocale · après le RDV</div>'
                f'<h2 style="margin-top:8px">Une note vocale suffit.</h2><div class="panel" style="margin-top:24px">'
                f'<div class="wave" style="height:110px">{bars}</div><div style="margin-top:18px;font:500 18px DM Mono;color:#5B6578">● 0:48</div></div></div>')
        return (f'<div class="crm">{side}<div class="main" style="display:flex">{left}<div style="flex:1">'
                f'<div class="lbl">Fiche prospect</div><h2>{title}</h2>{f}</div></div></div>')
    return f'<div class="crm">{side}<div class="main"><div class="lbl">Fiche prospect</div><h2>{title}</h2>{f}</div></div>'


def laptop(x, y, s=1, content="", cls=""):
    return f'<div {at(x, y, s, 0, "laptop sh " + cls)}><div class="scr">{content}</div></div>'


EMPTY = [("Nom", ""), ("Date de naissance", ""), ("Ville", ""), ("Besoin", "")]


def carnet(x, y, s=1, lines=4, r=-2, cls=""):
    L = ["Louis Lebrun · 18:00", "né le 10/10/1978,", "Paris 15e", "mutuelle santé famille",
         '<span class="arrow">→ conseil : garanties renforcées</span>']
    return f'<div {at(x, y, s, r, "carnet sh " + cls)}>{"<br>".join(L[:lines])}</div>'


def dda(x, y, s=1, n=3, light=False, cursor=False, stamp=False, cls=""):
    rows = ["Besoins exprimés", "Situation familiale", "Budget", "Garanties proposées", "Justification du conseil"]
    chip = '<span style="font:500 14px DM Mono;color:#F24E1E;background:#FBE3D9;padding:3px 8px;border-radius:4px;margin-left:auto">IA</span>' if light else ""
    r = "".join(f'<div class="ln"><div class="ck{" on" if i < n else ""}"></div>{t}{chip if i < n else ""}</div>' for i, t in enumerate(rows))
    if light:
        bar = f'<div style="margin-top:28px;font:500 16px DM Mono;letter-spacing:2px;color:#5B6578">COMPLÉTUDE</div><div style="height:14px;border-radius:7px;background:#E8E0D0;margin-top:10px"><div style="height:100%;width:100%;border-radius:7px;background:#F24E1E"></div></div>'
        head = '<h3>Fiche de conseil · Santé Individuel</h3><div class="s">Louis Lebrun · remplie automatiquement</div>'
    else:
        bar = ""
        head = '<h3>Fiche de conseil · Mutuelle santé</h3><div class="s">Modèle_DDA_v3.docx</div>'
    st = f'<div class="o stamp" style="right:60px;top:150px;transform:rotate(-6deg)">PISTE D\'AUDIT · HORODATÉE</div>' if stamp else ""
    cur = '<div class="cursor" style="left:96px;top:520px"></div>' if cursor else ""
    return f'<div {at(x, y, s, 0, "doc sh " + cls, "position:absolute")}>{head}{r}{bar}{st}{cur}</div>'


def wa(msgs):
    return f'<div class="wa"><div class="hd"><div class="av"></div>Camille R.</div>{msgs}</div>'


CAM = '<div class="bub">Bonjour, je cherche une mutuelle pour ma famille. Vous pouvez me faire un devis ?<span class="tm">21:14</span></div>'
REP = '<div class="bub me">Bonjour Camille, je suis l\'assistant IA du cabinet. Pour préparer votre devis : combien de personnes à couvrir ?<span class="tm">21:14<span class="tk">✓✓</span></span></div>'

S = {}
S["P01"] = page("dark",
    agenda(300, 50, .8) + phone(1330, 120, .95, lock("mardi 12", "19:00")) +
    f'<div {at(-200, 980, 1.2, -12, "pen blur12")}></div>',
    'Mardi, <span class="box">dix-neuf heures.</span>')
S["P02"] = page("dark",
    agenda(260, -260, 1.25, checked=True, tabx=-300) + phone(1500, -380, .9, lock("mardi 12", "19:00"), cls="blur8"),
    'Votre dernier rendez-vous vient de <span class="box">partir.</span>')
S["P03"] = page("dark",
    laptop(310, 40, 1.0, crm(EMPTY, caret_on=0)) +
    '<div class="o cup blur12" style="left:-90px;top:780px;transform:scale(1.2)"></div>',
    'Et votre <span class="box">deuxième journée</span> commence.')
S["P04"] = page("dark",
    laptop(560, 170, .72, crm(EMPTY, caret_on=0)) + phone(130, 120, .8, lock("mardi 12", "22:47")) +
    '<div class="o cup empty" style="left:1560px;top:700px"></div>')
S["P05"] = page("dark",
    carnet(520, 30, 1.0, lines=5) + f'<div {at(1130, 860, 1.2, -28, "pen blur8")}></div>' +
    laptop(1640, 120, .8, crm(EMPTY), cls="blur8"),
    'Votre métier, c\'est <span class="box">le conseil.</span>')
S["P06"] = page("dark",
    f'<div {at(150, 330, 1.0, 0, "keys")}>' + "".join(f'<i class="{"dn" if i in (17, 18, 19) else ""}"></i>' for i in range(36)) + '</div>' +
    '<div class="o" style="left:150px;top:-60px;width:1620px;height:330px;border-radius:0 0 12px 12px;background:#15325a;filter:blur(10px);opacity:.7"></div>' +
    f'<div {at(-260, 520, .9, 0, "carnet blur8", "height:500px;width:500px")}></div>',
    'Pas la <span class="trait">saisie.</span>')
S["P07"] = page("dark",
    carnet(160, 60, .95, lines=5, r=0) +
    laptop(1000, 80, .66, crm([("Nom", "Lebrun"), ("Date de naissance", "10/10/1978"), ("Ville", "Paris"), ("Besoin", "")], caret_on=2)) +
    f'<div {at(1060, 130, .66, 0, "laptop", "opacity:.0")}></div>',
    'Pourtant, vous <span class="box">retapez</span> vos notes, fiche par fiche.')
S["P08"] = page("dark",
    dda(410, 60, 1.0, n=3, cursor=True),
    'Vous remplissez le devoir de conseil, <span class="box">case par case.</span>')
S["P09"] = page("dark",
    phone(760, 40, 1.0, lock("samedi 16", "21:14", notif=True)) +
    f'<div {at(-160, 640, 1.0, 8, "agenda blur12", "height:500px")}></div>',
    'Et le prospect qui vous écrit <span class="box">samedi soir…</span>')
S["P10"] = page("dark",
    phone(700, 0, 1.1, lock("lundi 18", "08:30", notif=True, grey=True)),
    'attend <span class="trait">lundi.</span>')
S["P11"] = page("black",
    '<div class="typo" style="top:470px">Et si vous arrêtiez d\'écrire ?<span class="caret" style="height:80px;width:6px;margin-left:10px"></span></div>')
S["P12"] = page("light",
    '<div class="o wave" style="left:510px;top:330px;height:260px">' +
    "".join(f'<i style="height:{30 + (i * 53 % 200)}px"></i>' for i in range(64)) + '</div>' +
    '<div class="o sh" style="left:800px;top:660px;background:#F24E1E;color:#fff;font:600 30px DM Sans;padding:22px 40px;border-radius:6px">🎙 Enregistrement…</div>',
    'Avec <span class="box">Synapze,</span> vous <span class="trait">parlez.</span>')
S["P13"] = page("light",
    laptop(250, 20, 1.08, '<img src="../assets/ui/voice-note-fin.png" style="width:100%;height:100%;object-fit:cover;display:block">'),
    'Une note vocale après le rendez-vous, et la fiche client <span class="box">s\'écrit.</span>')
S["P14"] = page("light",
    dda(410, 40, 1.0, n=5, light=True, stamp=True),
    'Le devoir de conseil se remplit <span class="box">tout seul,</span> traçable.')
S["P15"] = page("light",
    phone(760, 30, 1.0, wa('<div class="pill">Samedi</div>' + CAM + REP)) +
    laptop(1500, 640, .7, crm(EMPTY, brand=True), cls="blur12"),
    'Sur WhatsApp, votre assistant répond à vos clients, <span class="box">jour et nuit.</span>')
S["P16"] = page("light",
    agenda(90, 110, .5) + carnet(740, 70, .62, lines=5, r=-3) + phone(1580, 40, .5, lock("mardi 12", "19:05")) +
    laptop(1250, 470, .48, crm([("Nom", "Lebrun"), ("Date de naissance", "10/10/1978"), ("Ville", "Paris"), ("Prénom", "Louis")], title="Louis Lebrun", brand=True)) +
    '<div class="o cup blur8" style="left:120px;top:640px"></div>',
    'Elle le rend <span class="trait">imbattable.</span>')
S["P17"] = page("dark",
    '<div class="logo" style="top:430px"><span>•</span>Synapze<span>•</span></div>')
S["P18"] = page("dark",
    '<div class="logo" style="top:170px;font-size:96px"><span>•</span>Synapze<span>•</span></div>'
    '<div class="typo" style="top:430px">Le courtier parle.<br><span style="color:#F24E1E">L\'IA fait tout le reste.</span></div>')
S["P19"] = page("dark",
    '<div class="logo" style="top:110px;font-size:80px"><span>•</span>Synapze<span>•</span></div>'
    '<div class="typo" style="top:290px;font-size:68px">Le courtier parle.<br><span style="color:#F24E1E">L\'IA fait tout le reste.</span></div>'
    '<div class="o" style="left:0;right:0;top:600px;text-align:center"><div class="btn" style="transform:scale(.94);box-shadow:0 0 0 18px rgba(242,78,30,.18)">Demander une démo</div>'
    '<div style="margin-top:30px;font:500 26px DM Mono;letter-spacing:3px;color:#9AA3B4">synapze.eu</div></div>'
    '<div class="cursor" style="left:1080px;top:660px"></div>'
    '<div class="o wave" style="left:660px;top:850px;height:60px;opacity:.6">' +
    "".join(f'<i style="width:5px;height:{8 + (i * 29 % 40)}px"></i>' for i in range(54)) + '</div>')

for k, v in S.items():
    (OUT / f"{k}.html").write_text(v, encoding="utf-8")
print(len(S), "styleframes")
