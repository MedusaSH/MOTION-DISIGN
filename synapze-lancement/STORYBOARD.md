---
format: 1920x1080
duration: "43.8s"
message: "Le courtier passe ses soirées à écrire ; avec Synapze, il parle et l'IA écrit à sa place."
arc: Hook → Problem → Pivot → Turn → Demo → Payoff → Reassurance → CTA
audience: "Courtier en assurance indépendant ou dirigeant d'un petit cabinet (1 à 10 personnes)"
mode: autonomous
captions: disabled
music: "pre-mixed with voice and SFX in assets/audio/mix.wav (mounted at root by the orchestrator)"
direction: "B · Le fil de la soirée, avec C2 (l'iPhone dans le noir, samedi 21:14) et C3 (WhatsApp iOS) empruntés à C"
styleframes: "styleframes/png/B1.png (0.80 s), B2.png (11.50 s), B3.png (25.50 s), C2.png (17.50 s), C3.png (31.00 s) ; une image par plan : styleframes/png/P01.png à P19.png, planche styleframes/png/planche.png"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

## Video direction

- **One world** (frame.md) : une ligne du temps horizontale, orange, graduée en heures puis en jours, que la caméra longe de gauche à droite. Frames 1-5 = PROBLEM sur le bleu nuit (la soirée de 18:00 à 22:47, puis le week-end jusqu'à lundi) ; frame 6 = PIVOT sur noir (la ligne plate) ; frames 7-10 = SOLUTION sur le crème (la ligne devenue forme d'onde) ; frame 11 = END CARD sur le bleu nuit (la ligne devenue soulignement du logo). Each frame paints its own full-bleed ground as a `class="clip"` layer.
- **Invisible seams**: every frame enters with `cut`; each seam falls at the top of the blur of a camera move and the `handoff_out` of frame N is copied word for word into the `handoff_in` of frame N+1. Wanted exceptions: 19.50 (« Et », coupe franche vers le noir du pivot, changement d'acte) ; 21.83 flash clair d'assemble.sh depuis le caret (960, 540).
- **Text** (readable without sound): every sentence of the voice is a `subtitle` at the bottom center (band y 890 to 980, nothing else in it) that arrives WORD BY WORD on the timestamps given in each frame (`word@seconds`, frame-local). Exactly ONE word or group per sentence sits in the `key-word-box` (named in the Scene lines as [boîte : …]). No other colored or glowing text. Typographic moments (the sentence IS the image, centered, 84 px at most): « Et si vous arrêtiez d'écrire ? » (frame 6) ; « Le courtier parle. L'IA fait tout le reste. » (frame 11).
- **Peaks**: only the 4 peaks named as [trait : …] (saisie, lundi, parlez, imbattable): a tapered accent brush stroke under THE key word. No giant word, no big box.
- **One thing to look at**: in every shot the camera isolates the subject of the sentence and shows the whole only when it makes sense; the camera follows the line from left to right and never goes back along it; equal side margins; no decor without meaning, no line crossing a sentence.
- **Real interfaces** (frame.md, from recent screenshots): l'écran Synapze « Une note vocale suffit. » (vraie vidéo du site, assets/ui/voice-note-fr.mp4) ; WhatsApp recopié de l'application iOS (frame.md whatsapp-ios) ; écran verrouillé d'iPhone ; avant le pivot, un CRM générique « MON CRM » sans marque. Uncluttered, the same device in the whole film.
- **Motion grammar**: two speeds, gestures of 1 to 6 images (expo.out) and linear drifts that never stop; the 0.3 to 0.9 s range is kept for the camera and the cursor (expo, power3 or power4); elements arrive too big and blurred then settle, never faded in at their final size; no frozen hold (every hold names its living layer); no "effect" transition.
- **Visible copy**: exactly the quoted copy of the Scene lines, nothing else.
- **Negative list**: slideshow (everything at t=0), screensaver (many things floating), doubled object, colored text instead of the box, big sentence, giant word, abstract symbol, hesitating cursor, several objects moving during a seam, any hue other than the accent except real interfaces and tool-tile brand colors.

**MONDE**
- Acte 1 (0.00 à 19.50) : #world 14400 × 2160, la ligne à y 540 ; stations 18:00 Agenda (1200, 540), 19:00 point (2400, 540), 20:00 fiche vide (3600, 540), 21:00 carnet (4800, 540), 21:30 à 22:00 fiches (5400 à 6000, 540), 22:30 fiche de conseil (6600, 540), 22:47 fin du segment hachuré (6936, 540), SAM. 21:14 iPhone (8400, 540), DIM. (9600, 540), LUN. 08:30 (10800, 540) ; fond bleu nuit #0E1624, trame de points crème 7 %, halo chaud derrière l'objet actif.
- Acte 2 (19.50 à 21.95) : noir #0A0F1A, la ligne plate fine (2 px) à y 620, plein cadre.
- Acte 3 (21.95 à 36.45) : #world 9600 × 2160 sur crème #F1EBDE, trame bleu nuit 9 % ; la ligne est une forme d'onde de 0 à 3000, puis redevient un trait ; stations Écran Synapze (4200, 540), Fiche de conseil (6000, 540), WhatsApp SAM. 21:14 (7800, 540), vue d'ensemble de la soirée 18:00 à 20:00 (8400 à 9600).
- Acte 4 (36.45 à 43.80) : bleu nuit, la ligne devenue soulignement sous le logo.
- Couleurs de rôle : accent orange #F24E1E = la ligne, le point, la boîte du mot clé, les traits, le bouton ; négatif = gris #5B6578 (segment hachuré, ligne après 19:00, notification sans réponse).

**SIGNATURES**
- Mécanisme 1 « l'étiquette qui s'accroche » (un objet tombe et pend à la ligne par un fil) : 0.15 (agenda), 4.85 (fiche vide), 7.40 (carnet), 12.06 / 12.38 / 12.57 (fiches), 13.30 (fiche de conseil), 16.30 (iPhone), 26.75 (fiche de conseil), 29.75 (WhatsApp)
- Mécanisme 2 « le point qui court » : 0.50 (il arrive à 19:00), 5.60 à 7.40 (il court jusqu'à 22:47 en traînant le segment hachuré), 19.59 (il devient le caret), 21.70 (il devient la première barre de l'onde), 35.10 (il s'arrête à 19:05), 36.50 (il devient le point gauche du logo)
- Registres de texte : sous-titre mot à mot (monte de 12 px, flou 6 → net en 0,08 s, expo.out) ; boîte du mot clé (fond orange qui s'ouvre de gauche à droite en 0,12 s) ; trait de pic (pinceau effilé tracé en 0,25 s) ; moment typographique (DM Serif Display 84 px centré, mot à mot, ×1,1 flou 8 → net en 0,1 s) ; horloge (DM Sans 150 px, roule chiffre par chiffre)
- Rimes : l'horloge 19:00 (0.60) → 22:47 (7.30) → 19:05 (35.10) ; la notification de samedi 21:14 (17.25) → la réponse à 21:14 (31.05) ; la fiche de conseil cochée à la main (15.20) → cochée seule (27.78) ; la ligne (0.00) → l'onde (21.95) → le soulignement du logo (36.50)

**PARTITION CAMÉRA** (global times) : 0.00 dérive le long de la ligne (+120 px/s) · 1.30 cran ×1,6 sur l'agenda · 3.40 whip droite le long de la ligne vers 20:00 · 5.50 pull ×0,7 et travelling qui suit le point de 19:00 à 22:47 · 7.30 push sur le carnet · 9.30 cran ×1,8 sur le segment hachuré · 10.20 pull en plan partagé carnet | fiche · 12.90 travelling droite vers 22:30 · 15.95 whip droite vers le week-end · 16.20 à 19.50 travelling lent SAM. → LUN. · 19.50 coupe franche (noir) · 21.83 flash clair · 22.00 à 23.70 travelling le long de l'onde · 23.70 push dans l'écran Synapze · 26.40 whip droite vers la fiche de conseil · 29.35 whip droite vers WhatsApp · 32.70 pull ×0,35 sur toute la soirée · 35.95 la ligne se contracte au centre · 36.45 carte de fin, dérive lente jusqu'à l'iris

**VOIX** : timings in onsets.json ; silences over 0.4 s, each written as a shot with its silent action : 5.49 à 7.49 (le gag : le point court de 19:00 à 22:47 et traîne le segment hachuré, la fiche reste vide) · 20.91 à 22.06 (le caret efface la phrase, la ligne frémit, flash) · 40.75 à 43.80 (clic, tenue vivante, iris)

**COUPES** (quota of the voice) : 19.50 · « Et » · changement d'acte : le problème s'arrête net, le pivot se joue sur noir

**RYTHME** : douleur (0 à 19.5) : 10 plans soit 5,1 / 10 s, un événement toutes les 0,3 à 0,6 s ; solution (21.95 à 36.45) : 5 plans soit 3,4 / 10 s, un événement toutes les 0,5 à 0,8 s

**SON** (global times, on the gestures) : pop 0.15 · whoosh-short 0.45 · click-soft 2.95 · whoosh-short 3.45 · pop 4.85 · click-soft 5.80 / 6.30 / 6.80 / 7.30 · pop 7.40 · key-press 9.45 / 9.55 / 9.65 · typing 11.00 · pop 12.06 / 12.38 / 12.57 · pop 13.30 · click 15.20 / 15.47 / 15.67 · whoosh-short 15.95 · pop 16.30 · notification 17.25 · click-soft 18.64 / 18.95 · key-press 21.00 à 21.40 · riser 21.10 · whoosh-cinematic 21.83 · pop 22.85 · typing 25.45 · ping 26.13 · pop 26.75 · click-soft 27.78 à 28.40 · pop 28.87 · whoosh-short 29.40 · notification 31.05 · pop 32.25 / 32.55 · whoosh 35.95 · sparkle 36.95 · click 40.60 · chime 40.65

## Frame 1: Mardi, dix-neuf heures · 0.00 → 3.70

- scene: La ligne du temps orange sur le bleu nuit ; l'agenda « Mardi » pend à 18:00 ; le point arrive à 19:00 ; le rendez-vous de 18:00 se coche et son étiquette part hors champ
- duration: 3.70s
- transition_in: cut
- status: animated
- src: compositions/frames/01-mardi.html
- voiceover: "Mardi, dix-neuf heures. Votre dernier rendez-vous vient de partir."
- type: hook
- blueprint: spatial-pan-stations (Adapt)
- focal: le point qui arrive à 19:00, puis la ligne 18:00 de l'agenda
- rules: viewport-change, vertical-spring-ticker
- world: dark
- handoff_in: aucun (ouverture du film) ; première image = la ligne orange qui traverse le cadre à y 540, graduations « 17:00 » et « 18:00 », l'agenda qui tombe ×1,15 flou au-dessus de 18:00
- handoff_out: à 3.70 : cam(3000, 540, 1.0) au sommet d'un whip vers la droite le long de la ligne (+5200 px/s), flou 12 px ; la ligne orange jusqu'au point de 19:00 (2400), grise ensuite ; l'agenda sort à gauche ; « 19:00 » au-dessus du point ; la graduation « 20:00 » entre par la droite ; sous-titre sorti ; trame 7 %

Word cues: Mardi@0.03 dix-neuf@0.67 heures@0.99 Votre@1.58 dernier@1.83 rendez-vous@2.19 vient@2.74 de@3.00 partir@3.10

Scene 1 (0.00 à 1.50 s) : P1, mardi, 19 h sur le fil
  TEXTE ÉCRAN : subtitle « Mardi, dix-neuf heures. » word by word from 0.03, [boîte : dix-neuf heures.] at 0.67 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 la ligne est là, elle dérive ; 0.15 l'agenda (page « Mardi », MARDI 12) tombe et pend à 18:00 par son fil (×1,15 flou 8 → posé en 0,12 s, balance 2°) ; 0.30 graduations « 17:00 » « 18:00 » « 19:00 » « 20:00 » s'impriment (0,04 s d'écart) ; 0.45 le point orange arrive par la gauche en glissant sur la ligne (0,25 s expo.out) et se pose sur 19:00 ; 0.60 « 19:00 » (horloge 150 px) roule au-dessus du point (0,07 s avant « dix-neuf ») ; 1.00 le halo chaud s'allume derrière le point ; 1.20 l'agenda se balance (1°).
  PISTE CAMÉRA : dérive x +120 px/s le long de la ligne ; 1.30 à 1.50 cran expo.inOut ×1,6 vers la ligne 18:00 de l'agenda, flou 6 px.
  COUCHES ET PROFONDEUR : sujet le point et l'horloge ; l'agenda à gauche ; fond la trame ; avant-plan une graduation floue (×2,5) qui passe en bas à gauche ; couches animées 2 (pic 3 à 0.45).
  OBJET-PONT ET VECTEUR : la ligne 18:00 de l'agenda devient le sujet du plan 2.
  SON : pop à 0.15 (l'agenda s'accroche) ; whoosh-short à 0.45 (le point).
  IMAGE CLÉ : 0.80 : la ligne orange et ses heures, l'agenda pendu à 18:00, « 19:00 » au-dessus du point, « Mardi, [dix-neuf heures.] » en bas (styleframe B1).

Scene 2 (1.50 à 3.70 s) : P2, le dernier rendez-vous part
  TEXTE ÉCRAN : subtitle « Votre dernier rendez-vous vient de partir. » word by word from 1.58, [boîte : partir.] at 3.10 ; écart synchro
  IMAGE DE DÉPART : la page d'agenda en gros plan, ligne « 18:00 · RDV M. Lebrun · mutuelle famille ».
  ÉTAPES : 1.58 sous-titre ; 2.19 l'étiquette du rendez-vous se soulève (ombre +6 px, 0,08 s) ; 2.95 coche orange tracée dans la case (0,15 s) ; 3.00 à 3.15 sur « partir » l'étiquette file vers la gauche hors champ (x -900, rotation -8°, flou 0 → 14, 0,15 s power2.in) ; 3.20 la ligne reste vide, cochée ; 3.40 début du whip.
  PISTE CAMÉRA : dérive x +12 px/s ; 3.40 à 3.70 whip droite expo.in le long de la ligne, flou 0 → 12 px.
  COUCHES ET PROFONDEUR : sujet la ligne et l'étiquette ; fond la page floue (4 px) ; avant-plan le fil de l'agenda flou ; couches animées 2.
  OBJET-PONT ET VECTEUR : vecteur : l'étiquette part à gauche, la caméra file à droite le long de la ligne.
  SON : click-soft à 2.95 (la coche) ; whoosh-short à 3.45 (le whip).
  IMAGE CLÉ : 3.10 : la ligne 18:00 cochée orange, l'étiquette « RDV M. Lebrun » qui file floue vers la gauche, « …vient de [partir.] » en bas.

## Frame 2: La deuxième journée · 3.70 → 7.40

- scene: À 20:00, une fiche prospect vide tombe et pend à la ligne ; dans le silence, le point court de 19:00 à 22:47 en traînant un segment hachuré gris pendant que la fiche reste vide
- duration: 3.70s
- transition_in: cut
- status: outline
- src: compositions/frames/02-deuxieme-journee.html
- voiceover: "Et votre deuxième journée commence."
- type: pain_point
- blueprint: spatial-pan-stations (Adapt)
- focal: la fiche vide et son caret, puis le point qui court
- rules: context-sensitive-cursor, vertical-spring-ticker
- world: dark
- handoff_in: à 0.00 : cam(3000, 540, 1.0) au sommet d'un whip vers la droite le long de la ligne (+5200 px/s), flou 12 px ; la ligne orange jusqu'au point de 19:00 (2400), grise ensuite ; l'agenda sort à gauche ; « 19:00 » au-dessus du point ; la graduation « 20:00 » entre par la droite ; sous-titre sorti ; trame 7 %
- handoff_out: à 3.70 : cam(4800, 380, 1.2) au milieu d'un push vers le haut (power3.in), flou 10 px ; le point arrêté à 22:47 (6936) hors cadre à droite, « 22:47 » ; le segment hachuré de 19:00 à 22:47 ; la fiche vide pendue à 20:00 à gauche ; le carnet qui tombe au-dessus de 21:00 ; sous-titre sorti ; trame 7 %

Word cues: Et@0.13 votre@0.24 deuxième@0.51 journée@0.93 commence@1.31 (silence de 1.79 à 3.70 : le gag muet)

Scene 1 (0.00 à 1.80 s) : P3, la fiche vide s'accroche
  TEXTE ÉCRAN : subtitle « Et votre deuxième journée commence. » word by word from 0.13, [boîte : deuxième journée] at 0.51 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 fin du whip ; 0.30 la graduation « 20:00 » au centre ; 1.15 la fiche « Nouveau prospect » (CRM générique, « MON CRM ») tombe et pend à 20:00 (×1,15 flou → posée, balance 2°), 0,15 s avant « commence » ; 1.40 ses libellés Nom, Date de naissance, Ville, Besoin s'impriment, champs vides ; 1.60 le caret orange clignote dans « Nom ».
  PISTE CAMÉRA : 0.00 à 0.20 fin du whip expo.out ; dérive push +2 %/s sur la fiche.
  COUCHES ET PROFONDEUR : sujet la fiche ; la ligne et son fil ; fond la trame ; avant-plan le point flou à gauche ; couches animées 2.
  OBJET-PONT ET VECTEUR : le point de 19:00 démarre le gag (plan 4).
  SON : pop à 1.15 (la fiche s'accroche).
  IMAGE CLÉ : 1.50 : la fiche vide pendue à la ligne sous « 20:00 », son caret orange, « Et votre [deuxième journée] commence. » en bas.

Scene 2 (1.80 à 3.70 s) : P4, le gag muet
  TEXTE ÉCRAN : aucun sous-titre (silence) ; seuls textes : l'horloge et le micro « SAISIE » sous le segment.
  IMAGE DE DÉPART : la fiche vide, caret qui clignote.
  ÉTAPES : 1.90 pull : la ligne de 19:00 à 23:00 entre dans le cadre ; 2.10 le point part de 19:00 et court vers la droite (linéaire) en traînant derrière lui le segment hachuré gris ; l'horloge au-dessus roule : 20:12 (2.10), 21:30 (2.60), 22:15 (3.10), 22:47 (3.60) ; 2.60 sous le segment, « SAISIE · SAISIE · SAISIE » s'imprime au fur et à mesure ; pendant tout ce temps le caret de la fiche clignote, la fiche reste vide ; 3.60 le point s'arrête net à 22:47 ; 3.40 début du push vers 21:00.
  PISTE CAMÉRA : 1.90 à 2.30 pull ×1,4 → ×0,7 (power3.out) ; puis travelling droite qui suit le point (+900 px/s) ; 3.40 à 3.70 push power3.in vers le haut de 21:00, flou 0 → 10 px.
  COUCHES ET PROFONDEUR : sujet le point et son horloge ; la fiche vide à gauche (un seul actif : le point) ; fond la trame ; couches animées 2 (point + segment).
  OBJET-PONT ET VECTEUR : le carnet tombe au-dessus de 21:00 pendant le push : il sera le sujet du plan 5.
  SON : click-soft à 2.10 / 2.60 / 3.10 / 3.60 (les crans de l'horloge) ; pop à 3.70 (le carnet).
  IMAGE CLÉ : 3.20 : la ligne grise, le segment hachuré qui s'étire de 19:00 vers 22:47, le point et « 22:15 » au-dessus, la fiche vide pendue à 20:00 avec son caret.

## Frame 3: Le conseil, pas la saisie · 7.40 → 13.20

- scene: Le carnet du rendez-vous pend à 21:00 ; « Pas la saisie » sur le segment hachuré ; puis carnet et fiche côte à côte, il retape ses notes, les fiches s'accrochent les unes après les autres
- duration: 5.80s
- transition_in: cut
- status: outline
- src: compositions/frames/03-saisie.html
- voiceover: "Votre métier, c'est le conseil. Pas la saisie. Pourtant, vous retapez vos notes, fiche par fiche."
- type: pain_point
- blueprint: comparison-split (Adapt)
- focal: les notes manuscrites, puis la fiche qui se remplit à la main
- rules: svg-path-draw, discrete-text-sequence, coordinate-target-zoom
- world: dark
- handoff_in: à 0.00 : cam(4800, 380, 1.2) au milieu d'un push vers le haut (power3.in), flou 10 px ; le point arrêté à 22:47 (6936) hors cadre à droite, « 22:47 » ; le segment hachuré de 19:00 à 22:47 ; la fiche vide pendue à 20:00 à gauche ; le carnet qui tombe au-dessus de 21:00 ; sous-titre sorti ; trame 7 %
- handoff_out: à 5.80 : cam(6300, 540, 0.9) au milieu d'un travelling vers la droite (power3.in), flou 8 px ; quatre fiches pendues de 21:30 à 22:00 ; le carnet sort à gauche ; la fiche de conseil entre par la droite au-dessus de 22:30 ; sous-titre sorti ; trame 7 %

Word cues: Votre@0.09 métier@0.39 c'est@0.81 le@1.12 conseil@1.24 Pas@2.02 la@2.16 saisie@2.25 Pourtant@2.87 vous@3.38 retapez@3.60 vos@3.99 notes@4.16 fiche@4.66 par@4.98 fiche@5.17

Scene 1 (0.00 à 1.90 s) : P5, les notes du conseil
  TEXTE ÉCRAN : subtitle « Votre métier, c'est le conseil. » word by word from 0.09, [boîte : le conseil.] at 1.12 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 fin du push, le carnet pendu se pose (balance 2°) ; 0.25 « Louis Lebrun · 18:00 » s'écrit à la main (Caveat, tracé 0,3 s) ; 0.60 « né le 10/10/1978, Paris 15e » ; 0.95 « mutuelle santé famille » ; 1.10 une flèche manuscrite orange « → conseil : garanties renforcées » (0,25 s, 0,02 s avant « conseil ») ; 1.50 le carnet se balance.
  PISTE CAMÉRA : dérive x +14 px/s.
  COUCHES ET PROFONDEUR : sujet les notes ; la ligne hachurée floue en bas ; fond la trame ; couches animées 2.
  OBJET-PONT ET VECTEUR : vecteur : cran vers le bas, sur le segment hachuré juste sous le carnet.
  SON : aucun (la voix).
  IMAGE CLÉ : 1.30 : le carnet pendu à la ligne, quatre lignes manuscrites et la flèche « → conseil », « Votre métier, c'est [le conseil.] » en bas.

Scene 2 (1.90 à 2.80 s) : P6, pas la saisie
  TEXTE ÉCRAN : subtitle « Pas la saisie. » word by word from 2.02, [trait : saisie.] at 2.25 ; écart synchro
  IMAGE DE DÉPART : le segment hachuré en gros plan, le micro « SAISIE » dessous.
  ÉTAPES : 1.90 à 2.00 cran ; 2.05 / 2.15 / 2.25 trois tampons « SAISIE » (DM Mono, gris) frappent sous le segment, chacun ×1,3 → ×1 en 0,05 s ; 2.25 le trait de pic se trace sous « saisie » ; 2.50 le segment continue de défiler.
  PISTE CAMÉRA : 1.90 à 2.00 cran ×1,8 expo.inOut, flou 6 px ; dérive x +40 px/s.
  COUCHES ET PROFONDEUR : sujet le segment ; le bas du carnet flou en haut ; fond ; couches animées 2.
  OBJET-PONT ET VECTEUR : vecteur : pull qui révèle le plan partagé.
  SON : key-press à 2.05 / 2.15 / 2.25.
  IMAGE CLÉ : 2.40 : le segment hachuré en gros plan, trois « SAISIE » tamponnés dessous, « Pas la [saisie.] » avec le trait orange.

Scene 3 (2.80 à 5.80 s) : P7, retaper fiche par fiche
  TEXTE ÉCRAN : subtitle « Pourtant, vous retapez vos notes, fiche par fiche. » word by word from 2.87, [boîte : retapez] at 3.60 ; écart synchro
  IMAGE DE DÉPART : plan partagé, marges égales : le carnet à gauche, la fiche du CRM générique à droite, tous deux pendus à la ligne.
  ÉTAPES : 2.80 à 3.20 pull power3.out ; 3.40 la ligne « Louis Lebrun » du carnet s'éclaire ; 3.60 le caret orange retape « Lebrun » dans « Nom » (0,05 s par lettre) ; 3.95 « 10/10/1978 » ; 4.20 « Paris » ; 4.60 la caméra glisse à droite ; 4.66 / 4.98 / 5.17 trois fiches vides tombent et pendent à 21:30, 21:45, 22:00 (×1,15 flou → posées) ; 5.50 début du travelling.
  PISTE CAMÉRA : dérive x +10 px/s ; 4.60 glissement droite (power3.out, 0,4 s) ; 5.50 à 5.80 travelling droite power3.in, flou 0 → 8 px.
  COUCHES ET PROFONDEUR : sujet la fiche qui se remplit, puis les fiches qui tombent ; fond la trame ; couches animées 3.
  OBJET-PONT ET VECTEUR : vecteur : travelling droite, la fiche de conseil entre au-dessus de 22:30.
  SON : typing de 3.60 à 4.40 (volume 0,2) ; pop à 4.66 / 4.98 / 5.17.
  IMAGE CLÉ : 5.20 : quatre fiches vides pendues au fil gris au-dessus du segment hachuré de 21:00 à 22:00, « …vos notes, fiche par fiche. » en bas (styleframe B2).

## Frame 4: Case par case · 13.20 → 16.20

- scene: La fiche de conseil pend à 22:30 ; une flèche de souris coche les cases une à une ; la ligne s'arrête à 22:47 et la caméra file vers le week-end
- duration: 3.00s
- transition_in: cut
- status: outline
- src: compositions/frames/04-case-par-case.html
- voiceover: "Vous remplissez le devoir de conseil, case par case."
- type: pain_point
- blueprint: cursor-ui-demo (Adapt)
- focal: les cases de la fiche
- rules: press-release-spring, svg-path-draw
- world: dark
- handoff_in: à 0.00 : cam(6300, 540, 0.9) au milieu d'un travelling vers la droite (power3.in), flou 8 px ; quatre fiches pendues de 21:30 à 22:00 ; le carnet sort à gauche ; la fiche de conseil entre par la droite au-dessus de 22:30 ; sous-titre sorti ; trame 7 %
- handoff_out: à 3.00 : cam(7900, 540, 1.0) au sommet d'un whip vers la droite (+6000 px/s), flou 14 px ; le point et « 22:47 » sortent à gauche ; la ligne grise continue, graduée « SAM. » ; sous-titre sorti ; trame 7 %

Word cues: Vous@0.10 remplissez@0.31 le@0.84 devoir@0.94 de@1.26 conseil@1.36 case@2.00 par@2.27 case@2.47

Scene 1 (0.00 à 3.00 s) : P8, case par case
  TEXTE ÉCRAN : subtitle « Vous remplissez le devoir de conseil, case par case. » word by word from 0.10, [boîte : case par case.] at 2.00 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.10 la fiche « Fiche de conseil · Mutuelle santé » (Modèle_DDA_v3.docx) tombe et pend à 22:30 (×1,15 flou → posée) ; 0.40 ses cinq lignes s'impriment, cases vides ; 0.90 la flèche de souris arrive en une courbe (0,4 s power3.out) ; 2.00 / 2.27 / 2.47 elle coche les trois premières cases sur la syllabe (coche 0,08 s, case ×0,9) ; 2.60 deux cases restent vides ; 2.70 début du whip.
  PISTE CAMÉRA : dérive x +16 px/s ; 2.70 à 3.00 whip droite expo.in, flou 0 → 14 px.
  COUCHES ET PROFONDEUR : sujet les cases ; la ligne et « 22:47 » flous en bas à droite ; fond ; couches animées 2 (pic 3 au clic).
  OBJET-PONT ET VECTEUR : la fiche reviendra se cocher seule au plan 14 ; vecteur : whip droite, la ligne continue vers le week-end.
  SON : pop à 0.10 ; click à 2.00 / 2.27 / 2.47 ; whoosh-short à 2.75.
  IMAGE CLÉ : 2.40 : la fiche de conseil pendue au fil, trois cases cochées, la flèche sur la quatrième, « …devoir de conseil, [case par case.] » en bas.

## Frame 5: Samedi soir, lundi · 16.20 → 19.50

- scene: Sur la ligne du week-end, un iPhone pend dans le noir à « SAM. 21:14 » : la notification WhatsApp d'un prospect ; la caméra longe la ligne jusqu'à « LUN. 08:30 », la notification grisée sans réponse
- duration: 3.30s
- transition_in: cut
- status: outline
- src: compositions/frames/05-samedi.html
- voiceover: "Et le prospect qui vous écrit samedi soir... attend lundi."
- type: pain_point
- blueprint: device-surface-showcase (Adapt)
- focal: la notification, puis la date
- rules: vertical-spring-ticker, depth-of-field-blur
- world: dark
- handoff_in: à 0.00 : cam(7900, 540, 1.0) au sommet d'un whip vers la droite (+6000 px/s), flou 14 px ; le point et « 22:47 » sortent à gauche ; la ligne grise continue, graduée « SAM. » ; sous-titre sorti ; trame 7 %
- handoff_out: à 3.30 : cam(10800, 400, 1.5) en plein push lent sur l'iPhone ; graduation « LUN. 08:30 » ; écran verrouillé « lundi 18 · 08:30 », notification « Camille R. » grise ; sous-titre « …attend [lundi.] » encore à l'écran (coupe franche voulue vers le noir du frame 6)

Word cues: Et@0.09 le@0.20 prospect@0.30 qui@0.73 vous@0.89 écrit@1.10 samedi@1.36 soir@1.68 attend@2.44 lundi@2.75

Scene 1 (0.00 à 2.30 s) : P9, le message du samedi soir
  TEXTE ÉCRAN : subtitle « Et le prospect qui vous écrit samedi soir… » word by word from 0.09, [boîte : samedi soir…] at 1.36 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 fin du whip ; 0.10 l'iPhone tombe et pend à « SAM. 21:14 » (×1,15 flou → posé, balance 2°), écran verrouillé « samedi 16 · 21:14 », halo bleuté de l'écran dans le noir ; 0.95 la notification WhatsApp descend du haut de l'écran (×1,08 floue → nette en 0,12 s) : « Camille R. · Bonjour, je cherche une mutuelle pour ma famille. Vous pouvez me faire un devis ? » ; 1.30 à droite, en DM Mono, « SAM. 21:14 » s'éclaire, « DIM. — » et « LUN. 08:30 » attendent en gris ; 1.70 la notification respire (±2 px).
  PISTE CAMÉRA : dérive push +3 %/s sur la notification.
  COUCHES ET PROFONDEUR : sujet la notification ; l'iPhone ; fond noir et halo ; couches animées 2.
  OBJET-PONT ET VECTEUR : la notification de Camille R. revient au plan 15, ouverte, avec la réponse (rime).
  SON : pop à 0.10 ; notification à 1.05 (deux tons, la signature : elle reviendra à 31.05).
  IMAGE CLÉ : 1.80 : l'iPhone pendu dans le noir, « samedi 16 · 21:14 », la notification de Camille R., « SAM. 21:14 · DIM. — · LUN. 08:30 » à droite, « …qui vous écrit [samedi soir…] » en bas (styleframe C2).

Scene 2 (2.30 à 3.30 s) : P10, attend lundi
  TEXTE ÉCRAN : subtitle « attend lundi. » word by word from 2.44, [trait : lundi.] at 2.75 ; écart synchro
  IMAGE DE DÉPART : l'iPhone et la notification.
  ÉTAPES : 2.30 la caméra glisse le long de la ligne vers la droite, l'iPhone suit (il pend au point mobile du fil) ; 2.40 la date de l'écran roule « dimanche 17 » (0,12 s), la graduation « DIM. » passe ; 2.70 « lundi 18 · 08:30 », la graduation « LUN. 08:30 » arrive au centre ; 2.75 trait sous « lundi » ; 2.85 la notification passe au gris, toujours sans réponse ; 3.00 à 3.30 push lent.
  PISTE CAMÉRA : travelling droite +1200 px/s de 2.30 à 2.80 (power2.out) ; dérive push +6 %/s.
  COUCHES ET PROFONDEUR : sujet la date ; la notification grise ; fond ; couches animées 2.
  OBJET-PONT ET VECTEUR : aucun (coupe franche voulue vers le noir, à 19.50, sur « Et »).
  SON : click-soft à 2.44 / 2.75.
  IMAGE CLÉ : 2.95 : l'iPhone « lundi 18 · 08:30 » au-dessus de la graduation « LUN. », la notification grise, « attend [lundi.] » avec le trait orange.

## Frame 6: Et si vous arrêtiez d'écrire ? · 19.50 → 21.95

- scene: Sur noir, la ligne plate traverse le cadre ; la phrase s'écrit au-dessus, suivie du caret orange ; le caret l'efface, reste seul, la ligne frémit, il devient une barre de son ; flash clair
- duration: 2.45s
- transition_in: cut
- status: outline
- src: compositions/frames/06-pivot.html
- voiceover: "Et si vous arrêtiez d'écrire ?"
- type: pivot
- blueprint: kinetic-type-beats (Adapt)
- focal: la phrase, puis le caret seul sur la ligne
- rules: context-sensitive-cursor, discrete-text-sequence
- world: dark
- handoff_in: aucun raccord de caméra (coupe franche voulue) ; noir #0A0F1A plein cadre, la ligne plate orange (2 px, opacité 0,5) à y 620 d'un bord à l'autre
- handoff_out: à 2.45 : flash clair d'assemble.sh depuis (960, 540) au maximum ; sous le flash, une barre orange verticale de 8 × 120 px au centre posée sur la ligne ; aucun sous-titre

Word cues: Et@0.09 si@0.20 vous@0.30 arrêtiez@0.51 d'écrire@0.93 (silence de 1.41 à 2.45 : le caret efface la phrase)

Scene 1 (0.00 à 2.45 s) : P11, le pivot
  TEXTE ÉCRAN : moment typographique centré « Et si vous arrêtiez d'écrire ? » (DM Serif Display 84 px, crème) à y 470, mot à mot ; pas de sous-titre en bas ; écart synchro
  IMAGE DE DÉPART : handoff_in, le caret orange (6 × 84 px) au centre, allumé.
  ÉTAPES : 0.09 « Et » s'écrit, le caret avance avec chaque mot ; 0.51 sur « arrêtiez » le caret cesse de clignoter ; 0.93 « d'écrire ? » ; 1.45 à 1.85 le caret efface la phrase de droite à gauche (une lettre toutes les 0,014 s) ; 1.90 le caret seul glisse sur la ligne jusqu'au centre ; 2.05 la ligne frémit d'un bord à l'autre (onde de 6 px, 0,2 s) ; 2.15 le caret s'étire en barre de son 8 × 120 px (0,12 s expo.out) ; 2.30 flash clair depuis la barre.
  PISTE CAMÉRA : dérive push +1,5 %/s.
  COUCHES ET PROFONDEUR : la phrase, le caret, la ligne ; fond noir et trame 2 % ; couches animées 2.
  OBJET-PONT ET VECTEUR : le caret devient la première barre de la forme d'onde ; la ligne devient l'onde du plan 12.
  SON : key-press de 1.50 à 1.90 (effacement, volume 0,15) ; riser de 1.60 à 2.33 ; whoosh-cinematic à 2.33 (flash).
  IMAGE CLÉ : 1.20 : noir, « Et si vous arrêtiez d'écrire ? » centré en crème, le caret orange fixe, la ligne plate en dessous.

## Frame 7: Vous parlez, la fiche s'écrit · 21.95 → 26.70

- scene: Sur le crème, la ligne est devenue la forme d'onde orange d'une note vocale ; Synapze ; l'onde court vers la droite et entre dans le vrai écran Synapze, où la fiche « Louis Lebrun » se remplit seule
- duration: 4.75s
- transition_in: cut
- status: outline
- src: compositions/frames/07-vous-parlez.html
- voiceover: "Avec Synapze, vous parlez. Une note vocale après le rendez-vous, et la fiche client s'écrit."
- type: demo
- blueprint: panel-edit-live-sync (Adapt)
- focal: la forme d'onde, puis la fiche qui s'écrit
- rules: stat-bars-and-fills, discrete-text-sequence, multi-phase-camera
- world: light
- handoff_in: à 0.00 : flash clair d'assemble.sh depuis (960, 540) au maximum ; sous le flash, une barre orange verticale de 8 × 120 px au centre posée sur la ligne ; aucun sous-titre
- handoff_out: à 4.75 : cam(4900, 540, 1.0) au sommet d'un whip vers la droite (+5000 px/s), flou 12 px ; l'écran Synapze rempli sort à gauche ; la ligne orange (redevenue trait) continue à droite ; sous-titre sorti ; trame 9 %

Word cues: Avec@0.11 Synapze@0.36 vous@0.87 parlez@1.12 Une@1.86 note@2.00 vocale@2.18 après@2.45 le@2.68 rendez-vous@2.77 et@3.48 la@3.57 fiche@3.67 client@3.90 s'écrit@4.18

Scene 1 (0.00 à 1.80 s) : P12, vous parlez
  TEXTE ÉCRAN : subtitle « Avec Synapze, vous parlez. » word by word from 0.11, [boîte : Synapze,] at 0.36, [trait : parlez.] at 1.12 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.15 le flash retombe sur le crème ; 0.10 la barre se démultiplie le long de la ligne, de part et d'autre (70 barres, 0,015 s d'écart) : la ligne EST la forme d'onde ; 0.40 les barres suivent l'amplitude réelle de la voix (waveform.py) ; 0.80 le bouton « Enregistrement… » (orange, micro blanc, comme dans le CRM) se pose au-dessus de l'onde (×1,2 flou → net, 0,08 s) ; 1.12 pic de l'onde sur « parlez », trait sous le mot ; 1.50 l'onde défile vers la droite.
  PISTE CAMÉRA : dérive x +60 px/s le long de l'onde.
  COUCHES ET PROFONDEUR : sujet l'onde ; fond le crème et la trame ; couches animées 2.
  OBJET-PONT ET VECTEUR : l'onde court vers la droite et entre dans la carte de transcription de l'écran Synapze (plan 13).
  SON : whoosh-cinematic de 2.33 (frame 6) qui finit ; pop à 0.90 (le bouton).
  IMAGE CLÉ : 1.20 : la forme d'onde orange qui traverse le crème, le bouton « Enregistrement… » au-dessus, « Avec [Synapze,] vous parlez. » avec le trait.

Scene 2 (1.80 à 4.75 s) : P13, la fiche s'écrit
  TEXTE ÉCRAN : subtitle « Une note vocale après le rendez-vous, et la fiche client s'écrit. » word by word from 1.86, [boîte : s'écrit.] at 4.18 ; écart synchro
  IMAGE DE DÉPART : l'onde qui file à droite vers l'écran Synapze posé sur la ligne (styleframe B3).
  ÉTAPES : 1.80 à 2.30 travelling droite : l'onde entre dans la carte de transcription du vrai écran Synapze (« CRM · PROSPECT », « Une note vocale suffit. », « Louis Lebrun · LEAD · Santé Individuel en souscription ») ; 2.30 à 2.60 push dans l'écran ; 2.40 « 0:18 » et « TRANSCRIPTION IA » ; 2.50 à 3.40 la citation s'écrit : « Louis Lebrun, né le 10 octobre 1978, Paris 15e. Il cherche une mutuelle santé pour sa famille. » ; 3.48 à 4.18 les champs Identité se remplissent avec la puce « IA » (Monsieur, Louis, Lebrun, 10/10/1978, 75015, Paris) ; 4.18 « REMPLIE AUTOMATIQUEMENT » ; 4.45 début du whip. Source : assets/ui/voice-note-fr.mp4, accélérée et calée dans l'écran.
  PISTE CAMÉRA : 1.80 à 2.30 travelling (power3.out) ; 2.30 à 2.60 push ×0,62 → ×1,1 ; dérive x -10 px/s ; 4.45 à 4.75 whip droite expo.in, flou 0 → 12 px.
  COUCHES ET PROFONDEUR : l'écran entier ; sujet la transcription puis le bloc Identité ; couches animées 3.
  OBJET-PONT ET VECTEUR : vecteur : whip droite, la ligne mène à la fiche de conseil.
  SON : typing de 3.48 à 4.20 (volume 0,15) ; ping à 4.18.
  IMAGE CLÉ : 4.00 : le vrai écran Synapze, la transcription de la note vocale, le bloc Identité rempli avec les puces « IA », « …et la fiche client [s'écrit.] » en bas.

## Frame 8: Tout seul, traçable · 26.70 → 29.65

- scene: La fiche de conseil du plan 8 pend à la ligne orange : ses cinq cases se cochent seules avec la puce « IA », la complétude se remplit, le tampon « Piste d'audit · horodatée » se pose
- duration: 2.95s
- transition_in: cut
- status: outline
- src: compositions/frames/08-tracable.html
- voiceover: "Le devoir de conseil se remplit tout seul, traçable."
- type: demo
- blueprint: agent-progress-theater (Adapt)
- focal: les cases qui se cochent seules
- rules: stat-bars-and-fills, svg-path-draw
- world: light
- handoff_in: à 0.00 : cam(4900, 540, 1.0) au sommet d'un whip vers la droite (+5000 px/s), flou 12 px ; l'écran Synapze rempli sort à gauche ; la ligne orange (redevenue trait) continue à droite ; sous-titre sorti ; trame 9 %
- handoff_out: à 2.95 : cam(7000, 540, 1.0) au sommet d'un whip vers la droite (+5000 px/s), flou 12 px ; la fiche de conseil complète sort à gauche ; la graduation « SAM. 21:14 » entre par la droite ; sous-titre sorti ; trame 9 %

Word cues: Le@0.06 devoir@0.17 de@0.49 conseil@0.60 se@0.97 remplit@1.08 tout@1.46 seul@1.67 traçable@2.17

Scene 1 (0.00 à 2.95 s) : P14, la fiche de conseil se remplit seule
  TEXTE ÉCRAN : subtitle « Le devoir de conseil se remplit tout seul, traçable. » word by word from 0.06, [boîte : tout seul,] at 1.46 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.05 la fiche « Fiche de conseil · Santé Individuel · Louis Lebrun, remplie automatiquement » tombe et pend à la ligne (×1,15 flou → posée) ; 0.30 les cinq mêmes lignes qu'au plan 8, cases vides ; 1.08 les cases se cochent seules de haut en bas (0,12 s d'écart), sans curseur, chacune avec la puce « IA » ; 1.10 la barre « Complétude » se remplit (0,5 s power2.out) ; 2.10 le tampon « PISTE D'AUDIT · HORODATÉE » fonce depuis la caméra (×4 flou 12 → ×1, rotation -6°, 0,2 s expo.out), contact à 2.17 ; 2.65 début du whip.
  PISTE CAMÉRA : dérive push +3 %/s ; 2.65 à 2.95 whip droite expo.in, flou 0 → 12 px.
  COUCHES ET PROFONDEUR : sujet les cases ; la barre ; le tampon devant ; fond ; couches animées 3.
  OBJET-PONT ET VECTEUR : vecteur : whip droite le long de la ligne, comme au frame 4.
  SON : pop à 0.05 ; click-soft à 1.08 / 1.20 / 1.32 / 1.44 / 1.56 (volume 0,15) ; pop à 2.17 ; whoosh-short à 2.70.
  IMAGE CLÉ : 2.30 : la fiche de conseil pendue au fil orange, cinq cases cochées avec la puce « IA », la barre pleine, le tampon posé de biais, « …se remplit [tout seul,] traçable. » en bas.

## Frame 9: Jour et nuit · 29.65 → 32.95

- scene: À « SAM. 21:14 », le même iPhone pend à la ligne, WhatsApp ouvert : l'assistant répond à Camille à la minute, puis à 03:12
- duration: 3.30s
- transition_in: cut
- status: outline
- src: compositions/frames/09-whatsapp.html
- voiceover: "Sur WhatsApp, votre assistant répond à vos clients, jour et nuit."
- type: demo
- blueprint: device-surface-showcase (Adapt)
- focal: la bulle de réponse
- rules: vertical-spring-ticker, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : cam(7000, 540, 1.0) au sommet d'un whip vers la droite (+5000 px/s), flou 12 px ; la fiche de conseil complète sort à gauche ; la graduation « SAM. 21:14 » entre par la droite ; sous-titre sorti ; trame 9 %
- handoff_out: à 3.30 : cam(8600, 540, 0.6) au milieu d'un pull power3.out ; l'iPhone WhatsApp pendu à « SAM. 21:14 » rétrécit ; la ligne orange s'étend de part et d'autre ; sous-titre sorti ; trame 9 %

Word cues: Sur@0.09 WhatsApp@0.25 votre@0.72 assistant@0.99 répond@1.46 à@1.78 vos@1.83 clients@1.99 jour@2.57 et@2.78 nuit@2.89

Scene 1 (0.00 à 3.30 s) : P15, l'assistant répond
  TEXTE ÉCRAN : subtitle « Sur WhatsApp, votre assistant répond à vos clients, jour et nuit. » word by word from 0.09, [boîte : jour et nuit.] at 2.57 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.10 l'iPhone tombe et pend à « SAM. 21:14 » (×1,15 flou → posé) ; 0.25 WhatsApp ouvert (frame.md whatsapp-ios) : « Camille R. · en ligne », pastille « Samedi », sa bulle « Bonjour, je cherche une mutuelle pour ma famille. Vous pouvez me faire un devis ? » 21:14 ; 0.95 les trois points « en train d'écrire » ; 1.40 la réponse se pose (bulle verte ×1,08 floue → nette en 0,12 s, 0,06 s avant « répond ») : « Bonjour Camille, je suis l'assistant IA du cabinet. Pour préparer votre devis : combien de personnes à couvrir ? » 21:14, coches bleues ; 2.20 l'heure de la barre d'état roule 21:14 → 03:12 ; 2.50 pastille « Aujourd'hui », « Nous sommes quatre, deux adultes et deux enfants. » 03:12 ; 2.80 les trois points, puis 3.00 la réponse « Parfait. Je prépare trois offres adaptées à votre famille. » arrive ×1,25 floue depuis la droite ; 3.00 début du pull.
  PISTE CAMÉRA : dérive push +2 %/s ; 2.95 à 3.30 pull power3.out ×1 → ×0,6.
  COUCHES ET PROFONDEUR : sujet la bulle de réponse ; fond le fil et le crème ; avant-plan la bulle qui arrive, floue ; couches animées 2.
  OBJET-PONT ET VECTEUR : vecteur : le pull continue au frame 10 jusqu'à toute la soirée.
  SON : pop à 0.10 ; notification à 1.40 (la même qu'à 17.25 : la rime) ; pop à 2.60 / 2.90.
  IMAGE CLÉ : 2.95 : l'iPhone WhatsApp, la question de samedi 21:14 et la réponse de l'assistant, puis la nuit à 03:12, « …vos clients, [jour et nuit.] » en bas (styleframe C3).

## Frame 10: Imbattable · 32.95 → 36.45

- scene: La caméra recule sur toute la soirée en crème : de 18:00 à 20:00, plus de segment hachuré, les objets remplis pendent au fil ; le point s'arrête à 19:05 ; puis la ligne se contracte au centre
- duration: 3.50s
- transition_in: cut
- status: outline
- src: compositions/frames/10-imbattable.html
- voiceover: "L'IA ne remplace pas le courtier. Elle le rend imbattable."
- type: payoff
- blueprint: zoom-out-workspace-reveal (Adapt)
- focal: le point et l'horloge 19:05
- rules: center-outward-expansion, vertical-spring-ticker
- world: light
- handoff_in: à 0.00 : cam(8600, 540, 0.6) au milieu d'un pull power3.out ; l'iPhone WhatsApp pendu à « SAM. 21:14 » rétrécit ; la ligne orange s'étend de part et d'autre ; sous-titre sorti ; trame 9 %
- handoff_out: à 3.50 : la ligne contractée en un trait orange de 360 px au centre (960, 540), le point posé à son extrémité gauche ; le fond passe du crème au bleu nuit #0E1624 ; sous-titre sorti

Word cues: L'IA@0.13 ne@0.37 remplace@0.48 pas@0.96 le@1.13 courtier@1.25 Elle@2.06 le@2.25 rend@2.35 imbattable@2.71

Scene 1 (0.00 à 3.50 s) : P16, la soirée rendue
  TEXTE ÉCRAN : subtitle « L'IA ne remplace pas le courtier. » word by word from 0.13, [boîte : le courtier.] at 1.13 ; puis « Elle le rend imbattable. » from 2.06, [trait : imbattable.] at 2.71 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.40 fin du pull : la ligne orange de 18:00 à 20:00, en entier, sur le crème ; pendus au fil, petits : l'agenda (18:00), le carnet du courtier, la fiche « Louis Lebrun » remplie, la fiche de conseil cochée, l'iPhone WhatsApp ; 0.60 le carnet au centre s'éclaire (l'outil du conseil, celui du courtier) ; 1.25 sur « courtier » le carnet se balance ; 2.06 le point orange glisse depuis 18:00 et s'arrête à 19:05 (0,4 s power3.out) ; 2.20 l'horloge « 19:05 » roule au-dessus (rime de 19:00 et 22:47), aucun segment hachuré derrière lui ; 2.71 trait sous « imbattable » ; 3.00 à 3.50 la ligne et ses objets se contractent au centre (×1 → trait de 360 px, power3.in), le fond vire au bleu nuit.
  PISTE CAMÉRA : dérive pull -2 %/s ; 3.00 à 3.50 contraction.
  COUCHES ET PROFONDEUR : sujet le point et l'horloge ; les objets pendus ; fond ; couches animées 2 (pic 4 à la contraction).
  OBJET-PONT ET VECTEUR : le trait contracté devient le soulignement du logo, le point devient le point orange gauche de « • Synapze • ».
  SON : click-soft à 2.20 ; whoosh à 3.00.
  IMAGE CLÉ : 2.40 : toute la soirée en crème, la ligne orange de 18:00 à 20:00, les objets remplis pendus au fil, le point arrêté à « 19:05 », « Elle le rend [imbattable.] » avec le trait.

## Frame 11: Le courtier parle · 36.45 → 43.80

- scene: Sur le bleu nuit, le logo « • Synapze • » s'assemble sur le trait ; « Le courtier parle. L'IA fait tout le reste. » ; un curseur arrive et clique « Demander une démo »
- duration: 7.35s
- transition_in: cut
- status: outline
- src: compositions/frames/11-fin.html
- voiceover: "Synapze. Le courtier parle, l'IA fait tout le reste. Demandez votre démo."
- type: cta
- blueprint: logo-assemble-lockup (Adapt)
- focal: the wordmark, then the CTA button
- rules: cursor-click-ripple, press-release-spring
- world: dark
- handoff_in: à 0.00 : la ligne contractée en un trait orange de 360 px au centre (960, 540), le point posé à son extrémité gauche ; le fond passe du crème au bleu nuit #0E1624 ; sous-titre sorti
- handoff_out: aucun (fin du film, iris à 7.35)

Word cues: Synapze@0.14 Le@0.92 courtier@1.03 parle@1.47 l'IA@2.00 fait@2.21 tout@2.42 le@2.64 reste@2.74 Demandez@3.41 votre@3.81 démo@4.05 (hold to 7.35)

Scene 1 (0.00 à 0.90 s) : P17, le logo
  TEXTE ÉCRAN : aucun sous-titre ; le logo dit le mot.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 le point devient le point orange gauche ; 0.05 à 0.35 les lettres « Synapze » (DM Serif Display 140 px, crème) tombent une à une sur le trait (×1,4 floues → nettes en 0,12 s, 0,04 s d'écart) ; 0.40 le point orange droit se pose ; 0.50 le trait s'amincit et devient le soulignement du logo ; 0.60 la trame reprend sa dérive.
  PISTE CAMÉRA : dérive pull -1,5 %/s.
  COUCHES ET PROFONDEUR : sujet le logo ; fond bleu nuit, trame, halo orange doux ; couches animées 2.
  OBJET-PONT ET VECTEUR : le logo monte de 180 px pour laisser la promesse.
  SON : sparkle à 0.50.
  IMAGE CLÉ : 0.60 : « • Synapze • » centré, crème sur bleu nuit, points orange, le fin soulignement orange.

Scene 2 (0.90 à 3.30 s) : P18, la promesse
  TEXTE ÉCRAN : moment typographique centré sur deux lignes, comme le haut du site : « Le courtier parle. » (crème) puis « L'IA fait tout le reste. » (orange), DM Serif Display 84 px, mot à mot ; pas de sous-titre en bas ; écart synchro
  IMAGE DE DÉPART : le logo en haut du cadre.
  ÉTAPES : 0.92 « Le » ; 1.03 « courtier » ; 1.47 « parle. » ; 2.00 à 2.74 « L'IA fait tout le reste. » en orange ; 3.00 les deux lignes respirent.
  PISTE CAMÉRA : dérive pull -1,5 %/s.
  COUCHES ET PROFONDEUR : logo, promesse, fond ; couches animées 2.
  OBJET-PONT ET VECTEUR : la promesse remonte de 80 px, le bouton naît dessous.
  SON : aucun (la voix).
  IMAGE CLÉ : 2.90 : le logo, puis « Le courtier parle. » en crème et « L'IA fait tout le reste. » en orange, centrés.

Scene 3 (3.30 à 7.35 s) : P19, le clic et la tenue vivante
  TEXTE ÉCRAN : bouton « Demander une démo » ; dessous, en DM Mono, « synapze.eu » ; aucun sous-titre
  IMAGE DE DÉPART : le logo et la promesse.
  ÉTAPES : 3.35 le bouton orange arrive ×1,1 flou → posé (0,08 s), 0,06 s avant « Demandez » ; 3.60 « synapze.eu » s'imprime ; 3.70 le curseur arrive en une courbe depuis le bas à droite (0,45 s power3.out) ; 4.15 il clique directement : état pressé en 3 couleurs (orange pâle, blanc, orange), onde, ×0,92 et retour ; 4.30 sous le bouton, une fine forme d'onde orange naît sur la ligne et respire (la rime de la voix) ; 4.30 à 6.90 tenue vivante ; 6.90 à 7.35 iris noir sur le bouton.
  PISTE CAMÉRA : dérive pull -1,5 %/s ; 6.90 iris.
  COUCHES ET PROFONDEUR : logo, promesse, bouton, curseur ; fond ; couches animées 3.
  OBJET-PONT ET VECTEUR : aucun (fin du film).
  SON : click à 4.15 ; chime à 4.20.
  IMAGE CLÉ : 4.30 : le logo, la promesse, le bouton orange « Demander une démo » enfoncé sous le curseur avec son onde, « synapze.eu » et la fine onde dessous.
