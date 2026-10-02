"""Three directions x three styleframes (A1 to C3). Run from the project folder: python3 styleframes/directions.py"""
import runpy, pathlib
G = runpy.run_path(str(pathlib.Path(__file__).parent / "build.py"))
page, phone, lock, agenda, laptop, crm, EMPTY, carnet = (G[k] for k in "page phone lock agenda laptop crm EMPTY carnet".split())
OUT = pathlib.Path(__file__).parent

def wa2(msgs, time="21:14", name="Camille R.", sub="en ligne"):
    return (f'<div class="wa2"><div class="st"><span>{time}</span><span>●●● ▮</span></div>'
            f'<div class="hd"><span class="back">‹</span><div class="av">CR</div><div class="nm">{name}<small>{sub}</small></div>'
            f'<div class="ic"><i></i><i style="border-radius:50%;width:18px;height:18px"></i></div></div>'
            f'<div class="body">{msgs}</div><div class="in-bar">+<div class="f"></div>◎<div class="m"></div></div></div>')

def b(text, t, out=False, ticks="k"):
    tk = f'<span class="k{" g" if ticks == "g" else ""}">✓✓</span>' if out else ""
    return f'<div class="b {"out" if out else "in"}">{text}<span class="t">{t}{tk}</span></div>'

CAM = b("Bonjour, je cherche une mutuelle pour ma famille. Vous pouvez me faire un devis ?", "21:14")
REP = b("Bonjour Camille, je suis l'assistant IA du cabinet. Pour préparer votre devis : combien de personnes à couvrir ?", "21:14", out=True)
CHAT = '<div class="pill">Samedi</div>' + CAM + REP + '<div class="pill">Aujourd\'hui</div>' + b("Nous sommes quatre, deux adultes et deux enfants.", "03:12") + '<div class="typing"><i></i><i></i><i></i></div>'
G["S"]  # keep build output
F = {}
# A : le bureau du soir (le storyboard actuel)
for k, p in (("A1", "P04"), ("A2", "P08"), ("A3", "P13")):
    F[k] = (OUT / f"{p}.html").read_text(encoding="utf-8")

# B : le fil de la soirée (une ligne du temps orange qui devient la forme d'onde)
def ruler(x0, hours, y=520, step=520, color="rgba(241,235,222,.55)"):
    t = "".join(f'<div class="o" style="left:{x0+i*step}px;top:{y-14}px;width:2px;height:28px;background:{color}"></div>'
                f'<div class="o" style="left:{x0+i*step-40}px;top:{y+26}px;width:80px;text-align:center;font:500 22px DM Mono;color:{color}">{h}</div>'
                for i, h in enumerate(hours))
    return t
line = lambda y=520, c="#F24E1E", h=4, x="-50px", w="2100px": f'<div class="o" style="left:{x};top:{y-h//2}px;width:{w};height:{h}px;background:{c};border-radius:{h}px"></div>'
F["B1"] = page("dark",
    line() + ruler(220, ["17:00", "18:00", "19:00", "20:00"]) +
    '<div class="o" style="left:1236px;top:440px;width:30px;height:30px;border-radius:50%;background:#F24E1E;box-shadow:0 0 0 12px rgba(242,78,30,.2)"></div>'
    '<div class="o" style="left:1100px;top:250px;font:600 150px DM Sans;color:#F1EBDE;letter-spacing:-5px">19:00</div>'
    + agenda(560, 120, .34, checked=True, tabx=-200) +
    '<div class="o" style="left:740px;top:470px;width:2px;height:50px;background:rgba(241,235,222,.4)"></div>'
    '',
    'Mardi, <span class="box">dix-neuf heures.</span>')
hatch = '<div class="o" style="left:240px;top:500px;width:1440px;height:40px;background:repeating-linear-gradient(-45deg,rgba(91,101,120,.55) 0 10px,transparent 10px 20px);border-top:2px solid #5B6578;border-bottom:2px solid #5B6578"></div>'
F["B2"] = page("dark",
    line(c="#5B6578") + hatch + ruler(240, ["19:00", "20:00", "21:00", "22:00"], step=480) +
    '<div class="o" style="left:1660px;top:430px;font:600 34px DM Mono;color:#F24E1E">22:47</div>' +
    "".join(f'<div class="o sh" style="left:{520+i*330}px;top:{150+(i%2)*20}px;width:280px;height:330px;background:#F1EBDE;border-radius:8px;transform:rotate({(-3,2,-1,3)[i]}deg);padding:22px;font:500 15px DM Mono;color:#5B6578">FICHE PROSPECT<div style="height:12px;background:#D8CFBD;margin-top:24px;border-radius:4px;width:{(80,60,90,40)[i]}%"></div><div style="height:12px;background:#D8CFBD;margin-top:16px;border-radius:4px;width:70%"></div><div style="height:12px;background:#D8CFBD;margin-top:16px;border-radius:4px;width:50%"></div></div>'
            f'<div class="o" style="left:{660+i*330}px;top:480px;width:2px;height:40px;background:rgba(241,235,222,.4)"></div>' for i in range(4)) +
    '<div class="o" style="left:250px;top:580px;font:500 22px DM Mono;letter-spacing:3px;color:#5B6578">SAISIE · SAISIE · SAISIE</div>',
    'Pourtant, vous <span class="box">retapez</span> vos notes, fiche par fiche.')
bars = "".join(f'<i style="height:{20+(i*53%150)}px;width:7px"></i>' for i in range(70))
F["B3"] = page("light",
    f'<div class="o wave" style="left:-40px;top:430px;height:180px;gap:6px">{bars}</div>' +
    laptop(980, 90, .62, '<img src="../assets/ui/voice-note-fin.png" style="width:100%;height:100%;object-fit:cover;display:block">') +
    '<div class="o" style="left:620px;top:516px;width:420px;height:6px;background:linear-gradient(90deg,#F24E1E,rgba(242,78,30,.0))"></div>',
    'Une note vocale après le rendez-vous, et la fiche client <span class="box">s\'écrit.</span>')

# C : tout se passe dans le téléphone du courtier
notifs = lambda items: "".join(f'<div class="notif" style="top:{290+i*108}px"><div class="app"><i style="background:{c}"></i>{a}</div><b>{t}</b><br>{d}</div>' for i, (a, c, t, d) in enumerate(items))
F["C1"] = page("dark",
    phone(650, -100, 1.5, lock("mardi 12", "19:00")) +
    '<div class="o" style="left:700px;top:420px;width:520px;transform:scale(1.25);transform-origin:50% 0">' + notifs([("CALENDRIER · 18:00","#F24E1E","RDV M. Lebrun","Terminé · mutuelle famille")]).replace("top:290px","top:0") + '</div>' +
    f'<div {G["at"](-420, 600, .7, 14, "agenda blur12")}></div>',
    'Mardi, <span class="box">dix-neuf heures.</span>')
F["C2"] = page("dark",
    phone(640, 20, 1.05, lock("samedi 16", "21:14", notif=True)) +
    '<div class="o" style="left:520px;top:-100px;width:900px;height:1100px;background:radial-gradient(closest-side,rgba(120,160,230,.18),transparent)"></div>'
    '<div class="o" style="left:1300px;top:260px;font:500 26px DM Mono;letter-spacing:4px;color:#5B6578;line-height:2.2">SAM. 21:14<br><span style="opacity:.6">DIM. —</span><br><span style="opacity:.35">LUN. 08:30</span></div>',
    'Et le prospect qui vous écrit <span class="box">samedi soir…</span>')
F["C3"] = page("light",
    phone(700, 10, 1.05, wa2(CHAT, time="03:12")) +
    '<div class="o sh" style="left:1220px;top:470px;transform:scale(1.25) rotate(-2deg);filter:blur(1.5px);max-width:380px;background:#D9FDD3;border-radius:12px;padding:10px 14px;font:400 19px/1.35 DM Sans;color:#111">Parfait. Je prépare trois offres adaptées à votre famille.</div>',
    'Sur WhatsApp, votre assistant répond à vos clients, <span class="box">jour et nuit.</span>')
for k, v in F.items():
    (OUT / f"{k}.html").write_text(v, encoding="utf-8")
print("directions:", " ".join(F))
