"""Direction B (+ C2, C3): one styleframe per shot P01 to P19. Run from the project folder after directions.py:
python3 styleframes/buildB.py"""
import runpy, pathlib
OUT = pathlib.Path(__file__).parent
D = runpy.run_path(str(OUT / "directions.py"))
G = runpy.run_path(str(OUT / "build.py"))
page, phone, lock, agenda, laptop, carnet, dda, at = (G[k] for k in "page phone lock agenda laptop carnet dda at".split())
F = D["F"]; line = D["line"]; ruler = D["ruler"]
REAL = '<img src="../assets/ui/voice-note-fin.png" style="width:100%;height:100%;object-fit:cover;display:block">'

def thread(x, y1, y2, c="rgba(241,235,222,.4)"):
    return f'<div class="o" style="left:{x}px;top:{y1}px;width:2px;height:{y2-y1}px;background:{c}"></div>'

def card(x, y, s=1, vals=("", "", "", ""), caret=None, r=0):
    keys = ["Nom", "Date de naissance", "Ville", "Besoin"]
    f = "".join(f'<div class="field"><div class="k">{k}</div><div class="v{" on" if caret == i else ""}">{v}{"<span class=caret></span>" if caret == i else ""}</div></div>' for i, (k, v) in enumerate(zip(keys, vals)))
    return (f'<div {at(x, y, s, r, "sh", "width:560px;background:#FBF7EE;border-radius:10px;padding:30px 34px;color:#0E1624")}>'
            f'<div style="font:500 14px DM Mono;letter-spacing:2px;color:#9AA3B4">MON CRM · FICHE PROSPECT</div>'
            f'<div style="font:400 38px DM Serif Display;margin:6px 0 4px">Nouveau prospect</div>{f}</div>')

hatch = lambda x, w, y=520: f'<div class="o" style="left:{x}px;top:{y-20}px;width:{w}px;height:40px;background:repeating-linear-gradient(-45deg,rgba(91,101,120,.6) 0 10px,transparent 10px 20px);border-top:2px solid #5B6578;border-bottom:2px solid #5B6578"></div>'
point = lambda x, y=520: f'<div class="o" style="left:{x-15}px;top:{y-15}px;width:30px;height:30px;border-radius:50%;background:#F24E1E;box-shadow:0 0 0 12px rgba(242,78,30,.2)"></div>'
clock = lambda x, t, y=330, c="#F1EBDE": f'<div class="o" style="left:{x-230}px;top:{y}px;width:460px;text-align:center;font:600 150px DM Sans;color:{c};letter-spacing:-5px">{t}</div>'

S = {}
S["P01"] = F["B1"]
S["P02"] = page("dark", agenda(260, -260, 1.25, checked=True, tabx=-300) + thread(760, 1000, 1080),
    'Votre dernier rendez-vous vient de <span class="box">partir.</span>')
S["P03"] = page("dark", line(y=760, c="#5B6578") + line(y=760, w="420px") + ruler(380, ["19:00", "20:00", "21:00"], y=760, step=600) + point(380, 760) +
    thread(980, 640, 760) + card(700, 40, 1.0, caret=0),
    'Et votre <span class="box">deuxième journée</span> commence.')
S["P04"] = page("dark", line(c="#5B6578") + line(w="290px") + hatch(240, 1260) + point(1500) + clock(1500, "22:15") +
    ruler(240, ["19:00", "20:00", "21:00", "22:00"], step=420) +
    '<div class="o" style="left:250px;top:580px;font:500 22px DM Mono;letter-spacing:3px;color:#5B6578">SAISIE · SAISIE · SAISIE · SAISIE</div>' +
    thread(600, 380, 500) + card(470, 90, .42, caret=0))
S["P05"] = page("dark", carnet(560, 20, .95, lines=5, r=-2) + thread(930, 930, 1080),
    'Votre métier, c\'est <span class="box">le conseil.</span>')
S["P06"] = page("dark", hatch(-40, 2000, 420).replace("height:40px", "height:160px").replace(f"top:{420-20}px", "top:340px") +
    "".join(f'<div class="o" style="left:{300+i*480}px;top:560px;font:500 46px DM Mono;letter-spacing:8px;color:#5B6578;transform:rotate({(-3,2,-1)[i]}deg);border:3px solid #5B6578;padding:8px 20px;border-radius:6px">SAISIE</div>' for i in range(3)),
    'Pas la <span class="trait">saisie.</span>')
S["P07"] = F["B2"]
S["P08"] = page("dark", dda(410, 30, 1.0, n=3, cursor=True) + line(y=820, c="#5B6578") + ruler(700, ["22:30", "22:47"], y=820, step=520) + hatch(-40, 1300, 820),
    'Vous remplissez le devoir de conseil, <span class="box">case par case.</span>')
S["P09"] = F["C2"]
S["P10"] = page("dark", phone(640, 20, 1.05, lock("lundi 18", "08:30", notif=True, grey=True)) +
    '<div class="o" style="left:1300px;top:260px;font:500 26px DM Mono;letter-spacing:4px;color:#5B6578;line-height:2.2"><span style="opacity:.35">SAM. 21:14</span><br><span style="opacity:.5">DIM. —</span><br><span style="color:#F1EBDE">LUN. 08:30</span></div>',
    'attend <span class="trait">lundi.</span>')
S["P11"] = page("black", line(y=640, h=2, c="rgba(242,78,30,.5)") +
    '<div class="typo" style="top:460px">Et si vous arrêtiez d\'écrire ?<span class="caret" style="height:80px;width:6px;margin-left:10px"></span></div>')
bars = "".join(f'<i style="height:{24+(i*53%190)}px;width:8px"></i>' for i in range(110))
S["P12"] = page("light", f'<div class="o wave" style="left:-20px;top:420px;height:240px;gap:9px">{bars}</div>' +
    '<div class="o sh" style="left:780px;top:220px;background:#F24E1E;color:#fff;font:600 32px DM Sans;padding:22px 42px;border-radius:6px">🎙 Enregistrement…</div>',
    'Avec <span class="box">Synapze,</span> vous <span class="trait">parlez.</span>')
S["P13"] = page("light", laptop(250, 20, 1.08, REAL),
    'Une note vocale après le rendez-vous, et la fiche client <span class="box">s\'écrit.</span>')
S["P14"] = page("light", dda(410, 20, 1.0, n=5, light=True, stamp=True) + line(y=840) + thread(960, 780, 840, "rgba(14,22,36,.3)"),
    'Le devoir de conseil se remplit <span class="box">tout seul,</span> traçable.')
S["P15"] = F["C3"]
small = lambda x, inner: thread(x + 90, 470, 600, "rgba(14,22,36,.3)") + inner
S["P16"] = page("light", line(y=600) + ruler(160, ["18:00", "19:00", "20:00"], y=600, step=800, color="rgba(14,22,36,.5)") +
    agenda(70, 160, .3) + carnet(470, 140, .36, lines=5, r=-2) + laptop(1180, 300, .26, REAL) + phone(1600, 180, .36, D["wa2"](D["CHAT"], time="03:12")) +
    thread(190, 470, 600, "rgba(14,22,36,.3)") + thread(610, 480, 600, "rgba(14,22,36,.3)") + thread(1350, 510, 600, "rgba(14,22,36,.3)") + thread(1670, 470, 600, "rgba(14,22,36,.3)") +
    point(1027, 600) + clock(1027, "19:05", y=640, c="#0E1624").replace("150px", "110px"),
    'Elle le rend <span class="trait">imbattable.</span>')
logo = lambda top, fs, ul=True: (f'<div class="logo" style="top:{top}px;font-size:{fs}px"><span>•</span>Synapze<span>•</span></div>' +
    (f'<div class="o" style="left:{960-int(fs*1.6)}px;top:{top+int(fs*1.35)}px;width:{int(fs*3.2)}px;height:3px;background:#F24E1E;border-radius:3px"></div>' if ul else ""))
S["P17"] = page("dark", logo(430, 140))
S["P18"] = page("dark", logo(150, 96) + '<div class="typo" style="top:440px">Le courtier parle.<br><span style="color:#F24E1E">L\'IA fait tout le reste.</span></div>')
S["P19"] = page("dark", logo(90, 80) +
    '<div class="typo" style="top:300px;font-size:68px">Le courtier parle.<br><span style="color:#F24E1E">L\'IA fait tout le reste.</span></div>'
    '<div class="o" style="left:0;right:0;top:600px;text-align:center"><div class="btn" style="transform:scale(.94);box-shadow:0 0 0 18px rgba(242,78,30,.18)">Demander une démo</div>'
    '<div style="margin-top:30px;font:500 26px DM Mono;letter-spacing:3px;color:#9AA3B4">synapze.eu</div></div>'
    '<div class="cursor" style="left:1080px;top:660px"></div>'
    '<div class="o wave" style="left:660px;top:850px;height:60px;opacity:.6">' + "".join(f'<i style="width:5px;height:{8 + (i * 29 % 40)}px"></i>' for i in range(54)) + '</div>')
for k, v in S.items():
    (OUT / f"{k}.html").write_text(v, encoding="utf-8")
print("direction B:", len(S), "shots")
