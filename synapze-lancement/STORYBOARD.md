---
format: 1920x1080
duration: "43.8s"
message: "Le courtier passe ses soirées à écrire ; avec Synapze, il parle et l'IA écrit à sa place."
arc: Hook → Problem → Pivot → Turn → Demo → Payoff → Reassurance → CTA
audience: "Courtier en assurance indépendant ou dirigeant d'un petit cabinet (1 à 10 personnes)"
mode: autonomous
captions: disabled
music: "pre-mixed with voice and SFX in assets/audio/mix.wav (mounted at root by the orchestrator)"
direction: "A · Le bureau du soir (direction unique, tirée de la charte du site : bleu nuit, crème, accent orange)"
styleframes: "styleframes/png/P01.png à styleframes/png/P19.png (une image par plan, planche : styleframes/png/planche.png)"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

## Video direction

- **One world** (frame.md) : le bureau du courtier vu du dessus, un seul plan de travail que la caméra parcourt (agenda, téléphone, ordinateur, carnet, tasse). Frames 1-5 = PROBLEM dans le monde sombre (le bureau à 19 h, bleu nuit, halo de lampe) ; frame 6 = PIVOT sur noir ; frames 7-10 = SOLUTION dans le monde clair (le même bureau en crème, lumière de jour) ; frame 11 = END CARD sur la scène sombre, comme le haut du site. Each frame paints its own full-bleed ground as a `class="clip"` layer.
- **Invisible seams**: every frame enters with `cut`; each seam falls at the top of the blur of a camera move and the `handoff_out` of frame N is copied word for word into the `handoff_in` of frame N+1. Wanted exceptions: 19.50 (« Et », coupe franche vers le noir du pivot, changement d'acte) ; 21.83 flash clair d'assemble.sh depuis le caret (960, 540), passage au monde de la solution.
- **Text** (readable without sound): every sentence of the voice is a `subtitle` at the bottom center (band y 890 to 980, nothing else in it) that arrives WORD BY WORD on the timestamps given in each frame (`word@seconds`, frame-local). Exactly ONE word or group per sentence sits in the `key-word-box` (named in the Scene lines as [boîte : …]). No other colored or glowing text. Typographic moments (the sentence IS the image, centered, 84 px at most): « Et si vous arrêtiez d'écrire ? » (frame 6) ; « Le courtier parle. L'IA fait tout le reste. » (frame 11).
- **Peaks**: only the 4 peaks named as [trait : …] (saisie, lundi, parlez, imbattable): a thin accent stroke or a tapered brush stroke under THE key word. No giant word, no big box.
- **One thing to look at**: in every shot the camera isolates the subject of the sentence and shows the whole only when it makes sense; a clear zoom in one direction, never a back-and-forth; side-by-side layouts with equal margins; no decor without meaning, no line crossing a sentence.
- **Real interfaces** (frame.md, from recent screenshots): CRM Synapze (fiche prospect « Louis Lebrun », panneau « Une note vocale suffit. », forme d'onde orange, bouton « Enregistrement… »), panneau DDA de Synapze, WhatsApp (iPhone). Dessinés d'après la description du site en attendant les captures : À REMPLACER PAR DES CAPTURES RÉCENTES avant l'animation. Uncluttered, the same device in the whole film.
- **Motion grammar**: two speeds, gestures of 1 to 6 images (expo.out) and linear drifts that never stop; the 0.3 to 0.9 s range is kept for the camera and the cursor (expo, power3 or power4); elements arrive too big and blurred then settle, never faded in at their final size; no frozen hold (every hold names its living layer); no "effect" transition.
- **Visible copy**: exactly the quoted copy of the Scene lines, nothing else.
- **Negative list**: slideshow (everything at t=0), screensaver (many things floating), doubled object, colored text instead of the box, big sentence, giant word, abstract symbol, hesitating cursor, several objects moving during a seam, any hue other than the accent except real interfaces and tool-tile brand colors.

**MONDE**
- Acte 1 (0.00 à 19.50) : le bureau du soir, #world 5760×3240 ; stations Agenda (900, 700), Téléphone (2300, 640), Ordinateur/CRM (3400, 1500), Carnet (1500, 2050), Tasse (2650, 2350) ; fond bleu nuit #0E1624, trame de points crème à 5 % (pas 48 px) qui rend la dérive visible, halo de lampe chaud en haut à gauche.
- Acte 2 (19.50 à 21.95) : noir #0A0F1A, plein cadre, le caret orange seul.
- Acte 3 (21.95 à 36.45) : le même bureau, mêmes stations, en crème #F1EBDE, trame de points bleu nuit à 6 %, lumière de jour sans halo.
- Acte 4 (36.45 à 43.80) : scène sombre #0E1624 de la carte de fin, la trame de points reprise.
- Couleurs de rôle : accent orange #F24E1E = ce qui compte (caret, boîte du mot clé, traits, forme d'onde, bouton) ; encre crème #F1EBDE sur sombre, bleu nuit #0E1624 sur clair ; négatif = gris bleuté #5B6578 (cases vides, coches grises, notification sans réponse).

**SIGNATURES**
- Mécanisme 1 « le caret orange » : 6.00 (clignote dans la fiche vide), 11.00 (retape les notes), 19.59 (seul sur le noir, puis efface la phrase), 21.70 (devient la première barre de la forme d'onde), 25.45 (écrit seul les champs de la fiche), 40.10 (devient le curseur de la fin)
- Mécanisme 2 « la coche » : 2.95 (le rendez-vous coché), 15.20 / 15.47 / 15.67 (cases cochées à la main), 27.78 à 28.40 (cases qui se cochent seules), 31.11 (coches bleues de WhatsApp)
- Registres de texte : sous-titre mot à mot (chaque mot monte de 12 px, flou 6 → net en 0,08 s, expo.out) ; boîte du mot clé (fond orange qui s'ouvre de gauche à droite en 0,12 s derrière le mot, power3.out) ; trait de pic (pinceau effilé orange tracé sous le mot en 0,25 s, power2.out) ; moment typographique (DM Serif Display 84 px centré, mot à mot, chaque mot ×1,1 flou 8 → net en 0,1 s)
- Rimes : l'horloge du téléphone « 19:00 » (0.70) revient « 19:05 » (35.20) ; la notification de samedi 21:14 (17.25) devient la conversation à laquelle l'assistant répond (31.11) ; la fiche DDA cochée à la main (15.20) se coche seule (27.78) ; la forme d'onde née du caret (21.70) respire sous le bouton de fin (41.00)

**PARTITION CAMÉRA** (global times) : 0.00 atterrissage ×1,3 → ×1 sur l'Agenda · 1.30 cran vers la ligne 18:00 · 3.40 whip droite vers l'Ordinateur · 5.60 pull ×1,4 → ×0,8 (bureau, téléphone, tasse) · 7.20 push vers le Carnet · 9.30 cran ×1,8 sur le clavier · 10.20 pull en plan partagé Carnet | CRM · 12.90 tilt bas vers la fiche DDA · 15.95 whip gauche vers le Téléphone · 19.50 coupe franche (noir) · 21.83 flash clair · 23.70 pull de la forme d'onde au CRM entier · 26.40 cran bas vers le panneau DDA · 29.30 whip gauche vers le Téléphone · 32.70 pull au bureau entier · 36.00 implosion vers le centre · 36.45 carte de fin, dérive lente jusqu'à l'iris

**VOIX** : timings in onsets.json ; silences over 0.4 s, each written as a shot with its silent action : 5.49 à 7.49 (le gag : l'horloge file de 19:00 à 22:47, la tasse se vide, le caret clignote toujours) · 20.91 à 22.06 (le caret efface la phrase, devient une barre de son, flash) · 40.75 à 43.80 (clic, tenue vivante, iris)

**COUPES** (quota of the voice) : 19.50 · « Et » · changement d'acte : le problème s'arrête net, le pivot se joue sur noir

**RYTHME** : douleur (0 à 19.5) : 12 plans soit 6,2 / 10 s, un événement toutes les 0,3 à 0,6 s ; solution (21.95 à 36.45) : 5 plans soit 3,4 / 10 s, un événement toutes les 0,5 à 0,8 s (le soulagement se sent)

**SON** (global times, on the gestures) : whoosh-short 0.45 · click-soft 2.95 · whoosh-short 3.45 · click-soft 5.80 / 6.05 / 6.30 · pop 6.55 · whoosh-short 7.15 · key-press 9.45 / 9.55 / 9.65 · typing 11.00 · pop 12.06 / 12.38 / 12.57 · click 15.20 / 15.47 / 15.67 · whoosh-short 15.95 · notification 17.25 · click-soft 18.64 / 18.95 · key-press 21.00 à 21.40 · riser 21.10 · whoosh-cinematic 21.83 · pop 22.85 · typing 25.45 · ping 26.13 · click-soft 27.78 à 28.40 · pop 28.87 · whoosh-short 29.40 · notification 31.11 · pop 32.25 / 32.55 · whoosh 35.95 · sparkle 36.95 · click 40.60 · chime 40.65

## Frame 1: Mardi, dix-neuf heures · 0.00 → 3.70

- scene: Sur le bureau sombre, l'agenda « Mardi » ; le téléphone affiche 19:00 ; la ligne « 18:00 · RDV M. Lebrun » se coche et l'étiquette du rendez-vous part hors champ
- duration: 3.70s
- transition_in: cut
- status: outline
- src: compositions/frames/01-mardi.html
- voiceover: "Mardi, dix-neuf heures. Votre dernier rendez-vous vient de partir."
- type: hook
- blueprint: spatial-pan-stations (Adapt)
- focal: l'agenda, puis la ligne du dernier rendez-vous
- rules: viewport-change, depth-of-field-blur
- world: dark
- handoff_in: aucun (ouverture du film) ; première image = la page d'agenda « MARDI » en gros plan, ×1,3 et floue, qui se pose
- handoff_out: à 3.70 : cam(3400, 1500, 1.0) au sommet d'un whip vers la droite (+5200 px/s), flou 12 px ; monde sombre ; l'agenda sort à gauche, la ligne 18:00 cochée orange ; le téléphone (19:00) flou en haut ; l'Ordinateur entre par la droite, écran noir ; sous-titre sorti ; trame de points 5 %

Word cues: Mardi@0.03 dix-neuf@0.67 heures@0.99 Votre@1.58 dernier@1.83 rendez-vous@2.19 vient@2.74 de@3.00 partir@3.10

Scene 1 (0.00 à 1.50 s) : P1, mardi, 19 h
  TEXTE ÉCRAN : subtitle « Mardi, dix-neuf heures. » word by word from 0.03, [boîte : dix-neuf heures.] at 0.67 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 la page d'agenda (papier crème, en-tête « MARDI » DM Serif, lignes horaires DM Mono) ×1,3 flou 10 → ×1 net en 0,12 s expo.out ; 0.15 les heures 9:00 à 18:00 s'impriment en cascade (0,03 s d'écart) ; 0.45 le téléphone fonce depuis la caméra en haut à droite (×4 flou 12 → ×1 en 0,25 s), écran verrouillé ; 0.60 « 19:00 » s'affiche en grand sur l'écran (0,07 s avant « dix-neuf ») ; 0.95 le halo de lampe s'allume en haut à gauche (opacité 0 → 0,35 en 0,1 s) ; 1.20 l'agenda dérive, le téléphone respire (±2 px, 1,6 s).
  PISTE CAMÉRA : dérive x -18 px/s, échelle +3 %/s ; 1.30 à 1.50 cran expo.inOut vers la ligne 18:00 de l'agenda (×1,25), flou 6 px.
  COUCHES ET PROFONDEUR : avant-plan le stylo flou coupé par le bord gauche ; sujet l'agenda net ; fond le téléphone légèrement flou (3 px), la trame ; couches animées 2 (pic 3 à 0.45).
  OBJET-PONT ET VECTEUR : la ligne 18:00 de l'agenda devient le sujet du plan 2.
  SON : whoosh-short à 0.45 (le téléphone arrive).
  IMAGE CLÉ : 0.80 : l'agenda « MARDI » net, le téléphone à « 19:00 » en haut à droite, « Mardi, [dix-neuf heures.] » en bas.

Scene 2 (1.50 à 3.70 s) : P2, le dernier rendez-vous part
  TEXTE ÉCRAN : subtitle « Votre dernier rendez-vous vient de partir. » word by word from 1.58, [boîte : partir.] at 3.10 ; écart synchro
  IMAGE DE DÉPART : la ligne « 18:00 · RDV M. Lebrun · mutuelle famille » au centre, ×1,25.
  ÉTAPES : 1.58 sous-titre ; 2.19 l'étiquette du rendez-vous (onglet crème collé sur la ligne) se soulève (ombre +6 px, 0,08 s) ; 2.95 coche orange tracée dans la case de la ligne (0,15 s, svg-path-draw) ; 3.00 à 3.15 sur « partir » l'étiquette file vers la gauche hors champ (x -900, rotation -8°, flou 0 → 14, 0,15 s power2.in), contact du bord à 3.10 ; 3.20 la ligne reste vide, cochée ; 3.40 début du whip.
  PISTE CAMÉRA : dérive x -12 px/s ; 3.40 à 3.70 whip droite expo.in vers l'Ordinateur, flou 0 → 12 px.
  COUCHES ET PROFONDEUR : sujet la ligne et l'étiquette ; fond le reste de la page floue (4 px) ; avant-plan le coin du téléphone flou en haut ; couches animées 2.
  OBJET-PONT ET VECTEUR : vecteur : l'étiquette part à gauche, la caméra file à droite ; l'Ordinateur entre par la droite dans le même whip.
  SON : click-soft à 2.95 (la coche) ; whoosh-short à 3.45 (le whip).
  IMAGE CLÉ : 3.10 : la ligne 18:00 cochée orange, l'étiquette « RDV M. Lebrun » qui file floue vers la gauche, « …vient de [partir.] » en bas.

## Frame 2: La deuxième journée · 3.70 → 7.40

- scene: Le whip pose l'ordinateur ; sur « commence » une fiche prospect vide s'ouvre ; dans le silence, le caret clignote, l'horloge du téléphone file de 19:00 à 22:47 et la tasse se vide
- duration: 3.70s
- transition_in: cut
- status: outline
- src: compositions/frames/02-deuxieme-journee.html
- voiceover: "Et votre deuxième journée commence."
- type: pain_point
- blueprint: zoom-out-workspace-reveal (Adapt)
- focal: la fiche vide et son caret, puis l'horloge
- rules: context-sensitive-cursor, vertical-spring-ticker
- world: dark
- handoff_in: à 0.00 : cam(3400, 1500, 1.0) au sommet d'un whip vers la droite (+5200 px/s), flou 12 px ; monde sombre ; l'agenda sort à gauche, la ligne 18:00 cochée orange ; le téléphone (19:00) flou en haut ; l'Ordinateur entre par la droite, écran noir ; sous-titre sorti ; trame de points 5 %
- handoff_out: à 3.70 : cam(1500, 2050, 1.1) au milieu d'un push vers le Carnet (power3.in), flou 10 px ; monde sombre, halo de lampe à 0,25 ; l'Ordinateur à droite avec la fiche vide et le caret allumé ; le téléphone à « 22:47 » ; la tasse vide ; sous-titre sorti ; trame 5 %

Word cues: Et@0.13 votre@0.24 deuxième@0.51 journée@0.93 commence@1.31 (silence de 1.79 à 3.70 : le gag muet)

Scene 1 (0.00 à 1.80 s) : P3, l'ordinateur s'allume
  TEXTE ÉCRAN : subtitle « Et votre deuxième journée commence. » word by word from 0.13, [boîte : deuxième journée] at 0.51 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 fin du whip, l'ordinateur se pose (×1,1 flou → net) ; 0.40 écran noir avec reflet de la lampe ; 1.15 l'écran s'allume (0,15 s avant « commence ») : CRM, fiche « Nouveau prospect » qui s'ouvre d'un trait (clip-path 0,22 s power3.out) ; 1.40 les libellés Nom, Foyer, Besoins, Budget s'impriment (0,04 s d'écart), champs vides gris ; 1.60 le caret orange apparaît dans « Nom ».
  PISTE CAMÉRA : 0.00 à 0.20 fin du whip expo.out ; dérive push +2 %/s sur l'écran.
  COUCHES ET PROFONDEUR : sujet l'écran ; fond le clavier et le bureau ; avant-plan la tasse floue coupée en bas à gauche ; couches animées 2.
  OBJET-PONT ET VECTEUR : le caret devient le sujet du gag (plan 4).
  SON : aucun bruitage (la voix).
  IMAGE CLÉ : 1.50 : l'écran du CRM allumé sur une fiche vide, « Et votre [deuxième journée] commence. » en bas.

Scene 2 (1.80 à 3.70 s) : P4, le gag muet
  TEXTE ÉCRAN : aucun sous-titre (silence) ; seul texte : l'heure du téléphone.
  IMAGE DE DÉPART : la fiche vide, caret qui clignote (0,5 s allumé, 0,5 s éteint).
  ÉTAPES : 1.90 pull : le téléphone et la tasse entrent dans le cadre ; 2.10 « 19:00 » roule chiffre par chiffre (vertical-spring-ticker) : 19:00 → 20:12 (2.10) → 21:30 (2.35) → 22:47 (2.60), chaque cran 0,12 s ; 2.85 le café de la tasse (disque brun vu du dessus) rétrécit jusqu'au fond (0,2 s power2.in) ; 3.00 le halo de lampe baisse (0,35 → 0,25) ; 3.10 le caret clignote toujours, la fiche est toujours vide ; 3.40 début du push vers le Carnet.
  PISTE CAMÉRA : 1.90 à 2.40 pull ×1,4 → ×0,8 (power3.out) sur le bureau entier ; dérive x +10 px/s ; 3.40 à 3.70 push power3.in vers le Carnet, flou 0 → 10 px.
  COUCHES ET PROFONDEUR : trois sujets à la suite, un seul actif à la fois : l'horloge (2.10 à 2.70), la tasse (2.85), le caret ; fond la trame ; couches animées 2 (pic 3).
  OBJET-PONT ET VECTEUR : vecteur : push vers la gauche-bas, le Carnet entre au centre dans le même mouvement.
  SON : click-soft à 2.10 / 2.35 / 2.60 (les chiffres) ; pop sourd à 2.85 (la tasse vide) ; whoosh-short à 3.45.
  IMAGE CLÉ : 2.80 : le bureau sombre, la fiche vide et son caret orange, le téléphone à « 22:47 », la tasse vide.

## Frame 3: Le conseil, pas la saisie · 7.40 → 13.20

- scene: Le carnet du rendez-vous et ses notes à la main ; « Pas la saisie » sur le clavier ; puis en plan partagé, le courtier retape ses notes dans le CRM et les fiches s'empilent
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
- handoff_in: à 0.00 : cam(1500, 2050, 1.1) au milieu d'un push vers le Carnet (power3.in), flou 10 px ; monde sombre, halo de lampe à 0,25 ; l'Ordinateur à droite avec la fiche vide et le caret allumé ; le téléphone à « 22:47 » ; la tasse vide ; sous-titre sorti ; trame 5 %
- handoff_out: à 5.80 : cam(3400, 1700, 1.3) au milieu d'un tilt vers le bas (power3.in), flou 8 px ; monde sombre ; l'écran du CRM avec une pile de trois fiches ; le Carnet à gauche, flou, sort du cadre ; sous-titre sorti ; trame 5 %

Word cues: Votre@0.09 métier@0.39 c'est@0.81 le@1.12 conseil@1.24 Pas@2.02 la@2.16 saisie@2.25 Pourtant@2.87 vous@3.38 retapez@3.60 vos@3.99 notes@4.16 fiche@4.66 par@4.98 fiche@5.17

Scene 1 (0.00 à 1.90 s) : P5, les notes du conseil
  TEXTE ÉCRAN : subtitle « Votre métier, c'est le conseil. » word by word from 0.09, [boîte : le conseil.] at 1.12 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 fin du push, le Carnet ouvert se pose (×1,1 → ×1) ; 0.25 « Lebrun · 18:00 » s'écrit à la main (Caveat, encre crème, tracé 0,3 s) ; 0.60 « marié, 2 enfants » ; 0.95 « mutuelle famille, hospitalisation ++ » ; 1.10 une flèche manuscrite « → conseil : garanties renforcées » (tracée 0,25 s, 0,02 s avant « conseil ») ; 1.50 la page dérive, le stylo posé en avant-plan.
  PISTE CAMÉRA : dérive x -14 px/s, rotation +0,3°/s (on lit la page).
  COUCHES ET PROFONDEUR : avant-plan le stylo flou coupé par le bord droit ; sujet les notes ; fond l'ordinateur flou à droite ; couches animées 2.
  OBJET-PONT ET VECTEUR : la ligne « mutuelle famille » sera retapée au plan 7 ; vecteur : cran vers la droite, sur le clavier.
  SON : aucun (la voix ; le stylo gratte sous la musique).
  IMAGE CLÉ : 1.30 : le carnet ouvert, quatre lignes manuscrites et la flèche « → conseil », « Votre métier, c'est [le conseil.] » en bas.

Scene 2 (1.90 à 2.80 s) : P6, pas la saisie
  TEXTE ÉCRAN : subtitle « Pas la saisie. » word by word from 2.02, [trait : saisie.] at 2.25 ; écart synchro
  IMAGE DE DÉPART : le clavier de l'ordinateur en gros plan, vu du dessus.
  ÉTAPES : 1.90 à 2.00 cran ; 2.05 / 2.15 / 2.25 trois touches s'enfoncent (2 px, ombre réduite, 0,05 s yoyo) ; 2.25 le trait de pic se trace sous « saisie » ; 2.50 le caret orange du champ vide se reflète sur l'écran au-dessus.
  PISTE CAMÉRA : 1.90 à 2.00 cran ×1,8 expo.inOut sur le clavier, flou 6 px ; dérive push +4 %/s.
  COUCHES ET PROFONDEUR : sujet les touches ; fond l'écran flou ; avant-plan la main absente, le bord du carnet flou à gauche ; couches animées 2.
  OBJET-PONT ET VECTEUR : vecteur : pull qui révèle le plan partagé ; le clavier reste au centre bas.
  SON : key-press à 2.05 / 2.15 / 2.25.
  IMAGE CLÉ : 2.40 : trois touches enfoncées sous l'écran qui luit, « Pas la [saisie.] » avec le trait orange.

Scene 3 (2.80 à 5.80 s) : P7, retaper fiche par fiche
  TEXTE ÉCRAN : subtitle « Pourtant, vous retapez vos notes, fiche par fiche. » word by word from 2.87, [boîte : retapez] at 3.60 ; écart synchro
  IMAGE DE DÉPART : plan partagé, marges égales : le Carnet à gauche (x 160 à 900), la fiche du CRM à droite (x 1020 à 1760).
  ÉTAPES : 2.80 à 3.20 pull power3.out vers le plan partagé ; 3.40 la ligne « Lebrun » du carnet s'éclaire ; 3.60 le caret orange retape « Lebrun » dans « Nom » lettre par lettre (0,05 s par lettre) ; 3.95 « 2 enfants » dans « Foyer » ; 4.20 « mutuelle famille » dans « Besoins » ; 4.60 la fiche remplie descend d'un cran ; 4.66 / 4.98 / 5.17 deux nouvelles fiches vides tombent par-dessus, chacune ×1,1 floue → posée (0,08 s), décalées de 6 px : une pile de trois ; 5.50 début du tilt vers le bas.
  PISTE CAMÉRA : dérive x +10 px/s ; 5.50 à 5.80 tilt bas power3.in vers la fiche DDA, ×1,3, flou 0 → 8 px.
  COUCHES ET PROFONDEUR : sujet la fiche qui se remplit ; à gauche le carnet net mais secondaire ; fond la trame ; couches animées 3 (caret, fiches, dérive).
  OBJET-PONT ET VECTEUR : la pile de fiches glisse vers le bas et la dernière devient la fiche de conseil DDA du plan 8.
  SON : typing de 3.60 à 4.40 (volume 0,2) ; pop à 4.66 / 4.98 / 5.17 (les fiches).
  IMAGE CLÉ : 4.30 : carnet à gauche, fiche à droite où le caret orange retape « mutuelle famille », « Pourtant, vous [retapez] vos notes, » en bas.

## Frame 4: Case par case · 13.20 → 16.20

- scene: La fiche de conseil DDA, un modèle Word ; une flèche de souris coche les cases une à une, sur « case par case »
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
- handoff_in: à 0.00 : cam(3400, 1700, 1.3) au milieu d'un tilt vers le bas (power3.in), flou 8 px ; monde sombre ; l'écran du CRM avec une pile de trois fiches ; le Carnet à gauche, flou, sort du cadre ; sous-titre sorti ; trame 5 %
- handoff_out: à 3.00 : cam(2300, 640, 1.2) au sommet d'un whip vers la gauche-haut (-5000 px/s), flou 12 px ; monde sombre ; la fiche DDA avec trois cases cochées sort à droite ; le Téléphone entre au centre, écran verrouillé ; sous-titre sorti ; trame 5 %

Word cues: Vous@0.10 remplissez@0.31 le@0.84 devoir@0.94 de@1.26 conseil@1.36 case@2.00 par@2.27 case@2.47

Scene 1 (0.00 à 3.00 s) : P8, case par case
  TEXTE ÉCRAN : subtitle « Vous remplissez le devoir de conseil, case par case. » word by word from 0.10, [boîte : case par case.] at 2.00 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 fin du tilt ; la fiche « Fiche de conseil · Mutuelle santé » (document blanc, mise en page Word) se pose ×1,15 floue → nette ; 0.40 les cinq lignes s'impriment : « Besoins exprimés », « Situation familiale », « Budget », « Garanties proposées », « Justification du conseil », chacune avec une case vide grise ; 0.90 la flèche de souris arrive en une courbe (0,4 s power3.out) sur la première case ; 2.00 / 2.27 / 2.47 elle coche les trois premières cases, contact sur la syllabe (coche tracée 0,08 s, case pressée ×0,9) ; 2.60 deux cases restent vides ; 2.70 début du whip.
  PISTE CAMÉRA : dérive tilt y +16 px/s le long de la fiche ; 2.70 à 3.00 whip gauche-haut expo.in vers le Téléphone, flou 0 → 12 px.
  COUCHES ET PROFONDEUR : sujet les cases ; fond le haut de la fiche flou (4 px) ; avant-plan la pile de fiches floue en bas ; couches animées 2 (pic 3 au clic).
  OBJET-PONT ET VECTEUR : la coche (signature 2) reviendra seule au plan 14 ; vecteur : whip gauche-haut, le Téléphone entre dans le même mouvement.
  SON : click à 2.00 / 2.27 / 2.47 ; whoosh-short à 2.75.
  IMAGE CLÉ : 2.40 : la fiche de conseil, trois cases cochées, la flèche sur la quatrième, « …devoir de conseil, [case par case.] » en bas.

## Frame 5: Samedi soir, lundi · 16.20 → 19.50

- scene: Sur l'écran verrouillé du téléphone, la notification WhatsApp d'un prospect, samedi 21:14 ; personne ne répond ; la date roule jusqu'à lundi
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
- handoff_in: à 0.00 : cam(2300, 640, 1.2) au sommet d'un whip vers la gauche-haut (-5000 px/s), flou 12 px ; monde sombre ; la fiche DDA avec trois cases cochées sort à droite ; le Téléphone entre au centre, écran verrouillé ; sous-titre sorti ; trame 5 %
- handoff_out: à 3.30 : cam(2300, 640, 1.6) en plein push lent sur la notification grisée ; monde sombre ; écran verrouillé « lundi 18 », notification « Camille R. » grise ; sous-titre « …attend [lundi.] » encore à l'écran (coupe franche voulue vers le noir du frame 6)

Word cues: Et@0.09 le@0.20 prospect@0.30 qui@0.73 vous@0.89 écrit@1.10 samedi@1.36 soir@1.68 attend@2.44 lundi@2.75

Scene 1 (0.00 à 2.30 s) : P9, le message du samedi soir
  TEXTE ÉCRAN : subtitle « Et le prospect qui vous écrit samedi soir… » word by word from 0.09, [boîte : samedi soir…] at 1.36 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 fin du whip, l'iPhone se pose (×1,15 flou → net) ; 0.30 écran verrouillé : « samedi 16 », « 21:14 » ; 0.95 la notification WhatsApp descend du haut de l'écran (×1,08 floue → nette en 0,12 s, 0,15 s avant « écrit ») : « Camille R. · Bonjour, je cherche une mutuelle pour ma famille. Vous pouvez me faire un devis ? » ; 1.30 la date « samedi 16 » s'éclaire ; 1.70 la notification respire (±2 px) ; 2.10 rien ne vient.
  PISTE CAMÉRA : dérive push +3 %/s sur la notification.
  COUCHES ET PROFONDEUR : sujet la notification ; fond l'écran verrouillé et le bureau flou ; avant-plan le bord de l'agenda flou en bas à gauche ; couches animées 2.
  OBJET-PONT ET VECTEUR : la notification de Camille R. revient au plan 15, ouverte, avec la réponse (rime).
  SON : notification à 1.05 (deux tons, la signature : elle reviendra à 31.11).
  IMAGE CLÉ : 1.80 : l'iPhone verrouillé « samedi 16 · 21:14 », la notification de Camille R., « …qui vous écrit [samedi soir…] » en bas.

Scene 2 (2.30 à 3.30 s) : P10, attend lundi
  TEXTE ÉCRAN : subtitle « attend lundi. » word by word from 2.44, [trait : lundi.] at 2.75 ; écart synchro
  IMAGE DE DÉPART : l'écran verrouillé avec la notification.
  ÉTAPES : 2.40 la date roule « samedi 16 » → « dimanche 17 » (0,12 s) ; 2.70 → « lundi 18 » (0,12 s), l'heure passe à « 08:30 » ; 2.75 trait de pic sous « lundi » ; 2.85 la notification passe au gris (#5B6578), toujours sans réponse ; 3.00 à 3.30 push lent.
  PISTE CAMÉRA : dérive push +6 %/s ; aucun mouvement brusque avant la coupe.
  COUCHES ET PROFONDEUR : sujet la date ; la notification grise ; fond flou ; couches animées 2.
  OBJET-PONT ET VECTEUR : aucun (coupe franche voulue vers le noir, à 19.50, sur « Et »).
  SON : click-soft à 2.44 / 2.75 (la date qui roule).
  IMAGE CLÉ : 2.95 : l'écran verrouillé « lundi 18 · 08:30 », la notification grise toujours là, « attend [lundi.] » avec le trait orange.

## Frame 6: Et si vous arrêtiez d'écrire ? · 19.50 → 21.95

- scene: Sur noir, la phrase s'écrit au centre, suivie du caret orange ; le caret l'efface, reste seul, vibre et devient une barre de son ; flash clair
- duration: 2.45s
- transition_in: cut
- status: outline
- src: compositions/frames/06-pivot.html
- voiceover: "Et si vous arrêtiez d'écrire ?"
- type: pivot
- blueprint: kinetic-type-beats (Adapt)
- focal: la phrase, puis le caret seul
- rules: context-sensitive-cursor, discrete-text-sequence
- world: dark
- handoff_in: aucun raccord de caméra (coupe franche voulue) ; noir #0A0F1A plein cadre, aucun objet ; la position du caret (960, 540) répond à celle de la notification du frame 5
- handoff_out: à 2.45 : flash clair d'assemble.sh depuis (960, 540) au maximum ; sous le flash, une barre orange verticale de 8 × 120 px au centre (le caret devenu barre de son) ; aucun sous-titre

Word cues: Et@0.09 si@0.20 vous@0.30 arrêtiez@0.51 d'écrire@0.93 (silence de 1.41 à 2.45 : le caret efface la phrase)

Scene 1 (0.00 à 2.45 s) : P11, le pivot
  TEXTE ÉCRAN : moment typographique centré « Et si vous arrêtiez d'écrire ? » (DM Serif Display 84 px, crème), mot à mot, chaque mot ×1,1 flou 8 → net en 0,1 s ; pas de sous-titre en bas ; écart synchro
  IMAGE DE DÉPART : noir plein cadre, le caret orange (6 × 84 px) au centre, allumé.
  ÉTAPES : 0.09 « Et » s'écrit, le caret avance avec chaque mot ; 0.51 sur « arrêtiez » le caret cesse de clignoter (allumé fixe) ; 0.93 « d'écrire ? » ; 1.45 à 1.85 le caret efface la phrase de droite à gauche, une lettre toutes les 0,014 s ; 1.90 le caret seul au centre ; 2.05 il vibre (±2 px, 3 images) puis s'étire en barre de son 8 × 120 px (0,12 s expo.out) ; 2.30 flash clair depuis la barre.
  PISTE CAMÉRA : dérive push lente +1,5 %/s sur le centre (le noir porte la trame à 2 % pour rendre la poussée visible).
  COUCHES ET PROFONDEUR : un seul sujet, le texte puis le caret ; fond noir et trame ; couches animées 2.
  OBJET-PONT ET VECTEUR : le caret devient la première barre de la forme d'onde du plan 12.
  SON : key-press de 1.50 à 1.90 (effacement, volume 0,15) ; riser de 1.60 à 2.33 ; whoosh-cinematic à 2.33 (flash).
  IMAGE CLÉ : 1.20 : noir, « Et si vous arrêtiez d'écrire ? » centré en crème, le caret orange fixe après le point d'interrogation.

## Frame 7: Vous parlez, la fiche s'écrit · 21.95 → 26.70

- scene: Dans le monde clair, la barre devient la forme d'onde orange d'une note vocale ; Synapze ; la caméra recule sur le vrai CRM et la fiche « Louis Lebrun » se remplit seule
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
- handoff_in: à 0.00 : flash clair d'assemble.sh depuis (960, 540) au maximum ; sous le flash, une barre orange verticale de 8 × 120 px au centre (le caret devenu barre de son) ; aucun sous-titre
- handoff_out: à 4.75 : cam(3400, 1800, 1.4) au milieu d'un cran vers le bas (expo.inOut), flou 6 px ; monde clair crème ; l'écran du CRM : panneau « Une note vocale suffit. » à gauche, fiche « Louis Lebrun » remplie à droite ; le panneau DDA entre par le bas ; sous-titre sorti ; trame bleu nuit 6 %

Word cues: Avec@0.11 Synapze@0.36 vous@0.87 parlez@1.12 Une@1.86 note@2.00 vocale@2.18 après@2.45 le@2.68 rendez-vous@2.77 et@3.48 la@3.57 fiche@3.67 client@3.90 s'écrit@4.18

Scene 1 (0.00 à 1.80 s) : P12, vous parlez
  TEXTE ÉCRAN : subtitle « Avec Synapze, vous parlez. » word by word from 0.11, [boîte : Synapze,] at 0.36, [trait : parlez.] at 1.12 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.15 le flash retombe sur le crème ; 0.10 la barre orange se démultiplie : 48 barres naissent de part et d'autre (0,02 s d'écart, depuis le centre) ; 0.40 elles suivent l'amplitude réelle de la voix (waveform.py sur 21.95 à 23.75) ; 0.80 le bouton rond « Enregistrement… » (orange, point blanc pulsant) se pose sous l'onde (×1,2 flou → net, 0,08 s) ; 1.12 pic de l'onde sur « parlez », trait sous le mot ; 1.50 l'onde continue de défiler.
  PISTE CAMÉRA : dérive pull -2 %/s.
  COUCHES ET PROFONDEUR : sujet l'onde ; fond le crème et la trame ; avant-plan aucun (le plan respire après le noir) ; couches animées 2.
  OBJET-PONT ET VECTEUR : l'onde et le bouton sont ceux du panneau « Une note vocale suffit. » que le pull révèle au plan 13.
  SON : whoosh-cinematic de 2.33 (frame 6) qui finit ; pop à 0.90 (le bouton).
  IMAGE CLÉ : 1.20 : la forme d'onde orange au centre du crème, le bouton « Enregistrement… » dessous, « Avec [Synapze,] vous parlez. » avec le trait sous « parlez ».

Scene 2 (1.80 à 4.75 s) : P13, la fiche s'écrit
  TEXTE ÉCRAN : subtitle « Une note vocale après le rendez-vous, et la fiche client s'écrit. » word by word from 1.86, [boîte : s'écrit.] at 4.18 ; écart synchro
  IMAGE DE DÉPART : l'onde et le bouton au centre.
  ÉTAPES : 1.75 à 2.30 pull power3.out : l'onde se range dans le panneau gauche du CRM (titre « Une note vocale suffit. », étiquette DM Mono « NOTE VOCALE · APRÈS LE RDV ») ; à droite la fiche « Louis Lebrun » vide ; 2.40 l'onde se fige en note enregistrée « 0:48 » ; 3.40 le caret orange part de la note et écrit seul : « Identité : Louis Lebrun » (3.48), « Foyer : marié, 2 enfants » (3.70), « Besoins : mutuelle famille, hospitalisation » (3.92), « Budget : à préciser » (4.10), chaque champ en 0,15 s ; 4.18 la fiche est complète, un liseré orange en fait le tour (0,2 s) ; 4.45 début du cran vers le bas.
  PISTE CAMÉRA : 1.75 à 2.30 pull ×2,2 → ×1 ; dérive x -10 px/s ; 4.45 à 4.75 cran bas expo.inOut vers le panneau DDA, ×1,4, flou 6 px.
  COUCHES ET PROFONDEUR : plan partagé à marges égales (note à gauche, fiche à droite) ; sujet la fiche ; fond l'écran ; couches animées 3 (caret, champs, dérive).
  OBJET-PONT ET VECTEUR : les champs de la fiche alimentent le panneau DDA qui entre par le bas au plan 14 ; la fiche répond à la fiche vide du plan 3 (rime).
  SON : typing de 3.48 à 4.20 (volume 0,15) ; ping à 4.18 (la fiche complète).
  IMAGE CLÉ : 4.00 : le CRM Synapze, la note vocale à gauche, la fiche « Louis Lebrun » qui se remplit seule à droite, « …et la fiche client [s'écrit.] » en bas.

## Frame 8: Tout seul, traçable · 26.70 → 29.65

- scene: Le panneau DDA de Synapze : les cinq cases de la fiche de conseil se cochent seules, la complétude se remplit, un tampon « Piste d'audit horodatée » se pose
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
- handoff_in: à 0.00 : cam(3400, 1800, 1.4) au milieu d'un cran vers le bas (expo.inOut), flou 6 px ; monde clair crème ; l'écran du CRM : panneau « Une note vocale suffit. » à gauche, fiche « Louis Lebrun » remplie à droite ; le panneau DDA entre par le bas ; sous-titre sorti ; trame bleu nuit 6 %
- handoff_out: à 2.95 : cam(2300, 640, 1.2) au sommet d'un whip vers la gauche-haut (-5000 px/s), flou 12 px ; monde clair ; le panneau DDA complet sort à droite ; le Téléphone entre au centre, WhatsApp ouvert ; sous-titre sorti ; trame 6 %

Word cues: Le@0.06 devoir@0.17 de@0.49 conseil@0.60 se@0.97 remplit@1.08 tout@1.46 seul@1.67 traçable@2.17

Scene 1 (0.00 à 2.95 s) : P14, la fiche de conseil se remplit seule
  TEXTE ÉCRAN : subtitle « Le devoir de conseil se remplit tout seul, traçable. » word by word from 0.06, [boîte : tout seul,] at 1.46 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.15 fin du cran, le panneau « Devoir de conseil · DDA » se pose ; 0.30 les cinq mêmes lignes qu'au plan 8, cases vides ; 1.08 sur « remplit » les cases se cochent seules, de haut en bas, 0,12 s d'écart (1.08 à 1.56), sans curseur ; 1.10 la barre « Complétude » se remplit en même temps (scaleX 0 → 1, 0,5 s power2.out) ; 2.10 le tampon « PISTE D'AUDIT · HORODATÉE » (DM Mono, encre orange, cadre fin) fonce depuis la caméra (×4 flou 12 → ×1, rotation -6°, 0,2 s expo.out), contact à 2.17 ; 2.50 le panneau dérive ; 2.65 début du whip.
  PISTE CAMÉRA : dérive push +3 %/s ; 2.65 à 2.95 whip gauche-haut expo.in vers le Téléphone, flou 0 → 12 px.
  COUCHES ET PROFONDEUR : sujet les cases ; la barre ; le tampon devant le panneau ; fond la fiche floue au-dessus ; couches animées 3 (pic 3 au tampon).
  OBJET-PONT ET VECTEUR : la coche (signature 2) passe aux coches bleues de WhatsApp au plan 15 ; vecteur : whip gauche-haut, comme au frame 4.
  SON : click-soft à 1.08 / 1.20 / 1.32 / 1.44 / 1.56 (volume 0,15) ; pop à 2.17 (le tampon) ; whoosh-short à 2.70.
  IMAGE CLÉ : 2.30 : le panneau DDA de Synapze, cinq cases cochées, la barre de complétude pleine, le tampon « Piste d'audit · horodatée » posé de biais, « …se remplit [tout seul,] traçable. » en bas.

## Frame 9: Jour et nuit · 29.65 → 32.95

- scene: Le même téléphone, la conversation de Camille R. ouverte : l'assistant répond à la minute, puis à 3 h du matin
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
- handoff_in: à 0.00 : cam(2300, 640, 1.2) au sommet d'un whip vers la gauche-haut (-5000 px/s), flou 12 px ; monde clair ; le panneau DDA complet sort à droite ; le Téléphone entre au centre, WhatsApp ouvert ; sous-titre sorti ; trame 6 %
- handoff_out: à 3.30 : cam(2900, 1500, 0.7) au milieu d'un pull power3.out sur le bureau clair entier ; le Téléphone en haut à gauche (conversation à 03:12) ; l'Ordinateur au centre avec la fiche remplie ; sous-titre sorti ; trame 6 %

Word cues: Sur@0.09 WhatsApp@0.25 votre@0.72 assistant@0.99 répond@1.46 à@1.78 vos@1.83 clients@1.99 jour@2.57 et@2.78 nuit@2.89

Scene 1 (0.00 à 3.30 s) : P15, l'assistant répond
  TEXTE ÉCRAN : subtitle « Sur WhatsApp, votre assistant répond à vos clients, jour et nuit. » word by word from 0.09, [boîte : jour et nuit.] at 2.57 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 fin du whip, l'iPhone se pose ; 0.25 WhatsApp ouvert (à remplacer par une capture) : en-tête « Camille R. », pastille « Samedi », sa bulle « Bonjour, je cherche une mutuelle pour ma famille. Vous pouvez me faire un devis ? » 21:14 (la même qu'au plan 9) ; 0.95 l'indicateur « en train d'écrire… » ; 1.40 la réponse se pose (bulle verte ×1,08 floue → nette en 0,12 s, 0,06 s avant « répond ») : « Bonjour Camille, je suis l'assistant IA du cabinet. Pour préparer votre devis : combien de personnes à couvrir ? » 21:14 ; 1.55 les coches de Camille passent au bleu ; 2.20 la barre d'état roule 21:14 → 03:12 ; 2.50 pastille « Mardi », une bulle de Camille « Nous sommes quatre. » 03:12 ; 2.80 la réponse arrive aussitôt, 03:12 ; 3.00 début du pull.
  PISTE CAMÉRA : dérive push +2 %/s ; 2.95 à 3.30 pull power3.out sur le bureau entier, ×1,2 → ×0,7.
  COUCHES ET PROFONDEUR : sujet la bulle de réponse ; fond le reste du fil et le bureau flou ; avant-plan le coin de l'ordinateur flou en bas à droite ; couches animées 2.
  OBJET-PONT ET VECTEUR : vecteur : le pull continue au frame 10 jusqu'au bureau entier.
  SON : notification à 1.46 (deux tons, la même qu'à 17.25 : la rime) ; pop à 2.60 / 2.90.
  IMAGE CLÉ : 1.80 : l'iPhone, la bulle de Camille du samedi 21:14 et, dessous, la réponse de l'assistant à 21:14, coches bleues, « …votre assistant répond à vos clients, » en bas.

## Frame 10: Imbattable · 32.95 → 36.45

- scene: Le bureau clair entier, tout est fait ; le téléphone affiche 19:05 ; puis tout se rassemble vers le centre
- duration: 3.50s
- transition_in: cut
- status: outline
- src: compositions/frames/10-imbattable.html
- voiceover: "L'IA ne remplace pas le courtier. Elle le rend imbattable."
- type: payoff
- blueprint: zoom-out-workspace-reveal (Adapt)
- focal: le carnet du courtier au centre, puis l'horloge à 19:05
- rules: center-outward-expansion, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : cam(2900, 1500, 0.7) au milieu d'un pull power3.out sur le bureau clair entier ; le Téléphone en haut à gauche (conversation à 03:12) ; l'Ordinateur au centre avec la fiche remplie ; sous-titre sorti ; trame 6 %
- handoff_out: à 3.50 : implosion au maximum : les objets du bureau rassemblés en un point au centre (960, 540), ×0,15, flou 10 px ; le fond passe du crème au bleu nuit #0E1624 ; sous-titre sorti

Word cues: L'IA@0.13 ne@0.37 remplace@0.48 pas@0.96 le@1.13 courtier@1.25 Elle@2.06 le@2.25 rend@2.35 imbattable@2.71

Scene 1 (0.00 à 3.50 s) : P16, le courtier rendu imbattable
  TEXTE ÉCRAN : subtitle « L'IA ne remplace pas le courtier. » word by word from 0.13, [boîte : le courtier.] at 1.13 ; puis « Elle le rend imbattable. » from 2.06, [trait : imbattable.] at 2.71 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.35 fin du pull : le bureau clair entier, rangé (agenda, téléphone, ordinateur fiche remplie, carnet fermé, tasse) ; 0.60 la caméra glisse vers le carnet et le stylo au centre (l'outil du conseil, celui du courtier) ; 1.20 le carnet s'ouvre sur « → conseil : garanties renforcées » (la ligne du plan 5) ; 2.10 l'écran du téléphone s'allume : « 19:05 » (rime de 19:00 et 22:47) ; 2.40 l'ordinateur se referme (écran qui bascule, 0,15 s) ; 2.71 trait sous « imbattable » ; 3.00 à 3.50 implosion : tout le bureau se rassemble vers le centre (×1 → ×0,15, power3.in, 0,5 s), le fond vire au bleu nuit.
  PISTE CAMÉRA : dérive pull -2 %/s ; 0.60 à 1.10 glissement vers le carnet (power3.out) ; 3.00 à 3.50 implosion.
  COUCHES ET PROFONDEUR : sujet le carnet puis l'horloge ; fond le bureau ; avant-plan la tasse floue coupée en bas ; couches animées 2 (pic 4 à l'implosion).
  OBJET-PONT ET VECTEUR : le point de l'implosion devient le point orange gauche du logo « • Synapze • » au frame 11.
  SON : whoosh à 3.00 (implosion).
  IMAGE CLÉ : 2.30 : le bureau clair rangé, le carnet ouvert au centre, le téléphone à « 19:05 », « Elle le rend [imbattable.] » avec le trait orange.

## Frame 11: Le courtier parle · 36.45 → 43.80

- scene: Sur la scène sombre, le logo « • Synapze • » s'assemble ; « Le courtier parle. L'IA fait tout le reste. » ; un curseur arrive et clique « Demander une démo »
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
- handoff_in: à 0.00 : implosion au maximum : les objets du bureau rassemblés en un point au centre (960, 540), ×0,15, flou 10 px ; le fond passe du crème au bleu nuit #0E1624 ; sous-titre sorti
- handoff_out: aucun (fin du film, iris à 7.35)

Word cues: Synapze@0.14 Le@0.92 courtier@1.03 parle@1.47 l'IA@2.00 fait@2.21 tout@2.42 le@2.64 reste@2.74 Demandez@3.41 votre@3.81 démo@4.05 (hold to 7.35)

Scene 1 (0.00 à 0.90 s) : P17, le logo
  TEXTE ÉCRAN : aucun sous-titre ; le logo dit le mot.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 le point de l'implosion devient le point orange gauche ; 0.05 à 0.35 les lettres « Synapze » (DM Serif Display 140 px, crème) tombent une à une (×1,4 floues → nettes en 0,12 s, 0,04 s d'écart) ; 0.40 le point orange droit se pose ; 0.60 la trame de points crème reprend sa dérive.
  PISTE CAMÉRA : dérive pull -1,5 %/s.
  COUCHES ET PROFONDEUR : sujet le logo ; fond bleu nuit, trame, halo orange très doux derrière ; couches animées 2.
  OBJET-PONT ET VECTEUR : le logo monte de 180 px pour laisser la promesse au plan 18.
  SON : sparkle à 0.50.
  IMAGE CLÉ : 0.60 : « • Synapze • » centré, crème sur bleu nuit, points orange.

Scene 2 (0.90 à 3.30 s) : P18, la promesse
  TEXTE ÉCRAN : moment typographique centré sur deux lignes, comme le haut du site : « Le courtier parle. » (crème) puis « L'IA fait tout le reste. » (orange), DM Serif Display 84 px, mot à mot ; pas de sous-titre en bas ; écart synchro
  IMAGE DE DÉPART : le logo en haut du cadre.
  ÉTAPES : 0.92 « Le » ; 1.03 « courtier » ; 1.47 « parle. » ; 2.00 à 2.74 « L'IA fait tout le reste. » en orange ; 3.00 les deux lignes respirent.
  PISTE CAMÉRA : dérive pull -1,5 %/s.
  COUCHES ET PROFONDEUR : logo, promesse, fond ; couches animées 2.
  OBJET-PONT ET VECTEUR : la promesse remonte de 80 px, le bouton naît dessous au plan 19.
  SON : aucun (la voix).
  IMAGE CLÉ : 2.90 : le logo, puis « Le courtier parle. » en crème et « L'IA fait tout le reste. » en orange, centrés.

Scene 3 (3.30 à 7.35 s) : P19, le clic et la tenue vivante
  TEXTE ÉCRAN : bouton « Demander une démo » ; dessous, en DM Mono, « synapze.eu » ; aucun sous-titre
  IMAGE DE DÉPART : le logo et la promesse.
  ÉTAPES : 3.35 le bouton orange (texte blanc, coins 6 px) arrive ×1,1 flou → posé (0,08 s), 0,06 s avant « Demandez » ; 3.60 « synapze.eu » s'imprime ; 3.70 le curseur arrive en une courbe depuis le bas à droite (0,45 s power3.out) ; 4.15 il clique directement : état pressé en 3 couleurs (orange pâle, blanc, orange), onde, ×0,92 et retour ; 4.30 sous le bouton, une fine forme d'onde orange naît et respire (la rime de la note vocale) ; 4.30 à 6.90 tenue vivante (dérive, onde) ; 6.90 à 7.35 iris noir sur le bouton.
  PISTE CAMÉRA : dérive pull -1,5 %/s ; 6.90 iris.
  COUCHES ET PROFONDEUR : logo, promesse, bouton, curseur ; fond ; couches animées 3.
  OBJET-PONT ET VECTEUR : aucun (fin du film).
  SON : click à 4.15 ; chime à 4.20.
  IMAGE CLÉ : 4.30 : le logo, la promesse, le bouton orange « Demander une démo » enfoncé sous le curseur avec son onde, « synapze.eu » dessous.
