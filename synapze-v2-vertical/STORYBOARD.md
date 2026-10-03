---
format: 1080x1920
duration: "43.8s"
message: "Le courtier passe ses soirées à écrire ; avec Synapze, il parle et l'IA écrit à sa place."
arc: Hook → Problem → Pivot → Turn → Demo → Payoff → Reassurance → CTA
audience: "Courtier en assurance indépendant ou dirigeant d'un petit cabinet"
mode: autonomous
captions: disabled
music: "pre-mixed with voice and SFX in assets/audio/mix-V2.wav (mounted at root by the orchestrator)"
direction: "V2 · Montage cinétique (typographie héroïne, coupes sur les mots, impacts, interfaces 3D)"
styleframes: "styleframes/png/V01.png à V11.png (une image clé par séquence)"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

## FORMAT 9:16 (version verticale TikTok / Instagram Reels) — PRIORITAIRE sur toute position du texte ci-dessous

Ce storyboard est celui du film 16:9 (synapze-v2), porté en 1080 × 1920. Les TEMPS, les mots, les sons, les effets et
le contenu de chaque scène restent ceux écrits plus bas ; toutes les positions, tailles et cadrages en px écrits pour
1920 × 1080 sont à RECOMPOSER pour la verticale (ne jamais réduire le 16:9 dans une bande).
- Canevas 1080 × 1920. Zones de sécurité des apps : haut 0-220 (en-tête), bas 1500-1920 (pseudo, légende, musique),
  droite 930-1080 (boutons j'aime / commentaires / partage). Tout texte et tout héros dans x 70-930, y 220-1500.
- Centre visuel : (500, 880). Les mots cinétiques : Geist 900 170-260 px (un mot par ligne, 2 lignes max, empilés
  verticalement si besoin), centrés sur x 500. Le mot émotion serif : 150-220 px.
- Caption .fx-cap : bande y 1270-1420, x 70-930, 54 px, 2 lignes max, retour à la ligne naturel.
- Interfaces : plus grandes dans le cadre, plein largeur utile (≈ 860 px), inclinées en 3D ; recadrer sur la partie utile
  (punch-in) plutôt que montrer l'écran entier en petit. Le téléphone WhatsApp occupe ≈ 60-70 % de la hauteur.
- Écrans partagés : empilés haut / bas (jour en haut, nuit en bas) au lieu de gauche / droite.
- Mouvements : les whips et glissements gauche / droite deviennent plutôt haut / bas quand c'est plus lisible ; les
  secousses et punch-ins restent identiques.

## Video direction

- **Grammar** (frame.md + reference/fx.html, copied verbatim by every frame): kinetic typography is the hero; hard cuts on the first word of each idea, sold by 2-frame flashes, whips and matches; impacts = slam + chromatic split + shake; 3D-tilted glass cards; glow, vignette and grain over everything. Frames 1-5 PROBLEM on night; frame 6 PIVOT on black; frames 7-10 SOLUTION on paper with orange light; frame 11 END CARD on night.
- **Seams**: every frame enters with `cut`. Most seams are wanted hard cuts on a word (written « coupe franche voulue » in handoff_in, with the first image described); the light flash of the orchestrator covers 21.85 to 22.05 (from the caret at 500, 880).
- **Text**: every sentence of the voice is readable without sound: either as kinetic type (the words themselves, on their cues) or as the caption `.fx-cap` at the bottom center (band y 890-980) word by word with ONE keyword in `.fx-key`. Never both saying the same words at the same time.
- **Real interfaces**: Synapze screen = assets/ui/voice-note/vn-*.jpg (never redrawn); WhatsApp = iOS copy without logo; problem CRM = generic « MON CRM ».
- **Negative list**: slideshow, frozen hold, faded-in hero at final size, two heroes at once, any hue but the orange family, brand before 22.31 s.

**MONDE**
- Acte 1 (0.00 à 19.50) : nuit .fx-night, braise .fx-glow derrière le héros, plans courts coupés sur les mots ; cartes .fx-card dans une scène .fx-3d.
- Acte 2 (19.50 à 21.95) : noir #050507, la phrase en Instrument Serif italique, le caret orange.
- Acte 3 (21.95 à 36.45) : papier .fx-paper avec lumière orange, interfaces .fx-card.light inclinées en 3D.
- Acte 4 (36.45 à 43.80) : nuit, logo, promesse, bouton.
- Couleurs de rôle : accent orange #F24E1E (boîte, glow, texte chaud, bouton, onde) ; tout le reste en nuit / papier / encre.

**SIGNATURES**
- Mécanisme 1 « le slam » (mot géant qui tombe de la caméra avec split chromatique et secousse) : 0.03 MARDI, 0.67 19:00, 9.65 SAISIE, 15.20 / 15.47 / 15.67 cases, 18.95 LUNDI, 35.66 IMBATTABLE
- Mécanisme 2 « le caret orange » : 4.95 champ vide, 6.00 gag, 11.00 retape, 19.59 pivot (efface la phrase), 21.70 devient barre de lumière, 23.07 onde
- Registres de texte : cinétique Geist 900 (slam ou rise) ; mot émotion Instrument Serif italique ; caption Geist 600 46 px mot à mot avec .fx-key ; labels Geist Mono
- Rimes : l'horloge 19:00 (0.67) → 22:47 (7.30) → 19:05 (35.10) ; la notification samedi 21:14 (17.25) → la réponse à 21:14 (31.05) ; la case cochée à la main (15.20) → cochée seule (27.78)

**PARTITION CAMÉRA** (global) : dérives 2-5 %/s dans chaque plan ; punch-ins sur 0.67, 2.19, 9.65, 15.20, 24.40, 25.43, 35.66 ; whips à 3.40, 13.05, 26.40, 29.35 ; coupe noire 19.50 ; flash 21.85

**VOIX** : timings in onsets.json ; silences over 0.4 s : 5.49 à 7.49 (le gag : montage time-lapse) · 20.91 à 22.06 (le caret efface, barre de lumière, flash) · 40.75 à 43.80 (clic, tenue, iris)

**COUPES** (montage cinétique, sur les mots) : 0.67 dix-neuf · 1.58 Votre · 3.70 Et · 5.49 (silence, gag) · 7.40 Votre · 9.42 Pas · 10.27 Pourtant · 13.20 Vous · 15.20 case · 15.47 par · 15.67 case · 16.20 Et · 18.64 attend · 19.50 Et (noir) · 21.95 Avec · 23.81 Une · 26.70 Le · 29.65 Sur · 32.22 jour · 32.95 L'IA · 35.01 Elle · 36.45 Synapze

**RYTHME** : douleur 18 plans / 19.5 s (≈ 9 / 10 s), gag 8 plans en 2 s ; solution 12 plans / 14.5 s

**SON** : voir assets/audio/sfx-events.json (whoosh sur chaque whip, impact sur chaque slam, clic sur chaque case, notification deux tons à 17.25 et 31.05, riser vers le pivot, glitch sur les coupes du gag)

## Frame 1: Mardi, dix-neuf heures · 0.00 → 3.70

- scene: MARDI slams on night; cut on « dix-neuf » to a giant rolling 19:00; cut on « Votre » to a 3D calendar card whose 18:00 event is swiped out on « partir »
- duration: 3.70s
- transition_in: cut
- status: animated
- src: compositions/frames/01-mardi.html
- voiceover: "Mardi, dix-neuf heures. Votre dernier rendez-vous vient de partir."
- type: hook
- blueprint: kinetic-type-beats (Adapt)
- focal: MARDI, then 19:00, then the 18:00 event card
- rules: kinetic-beat-slam, vertical-spring-ticker
- world: dark
- handoff_in: aucun (ouverture du film) ; première image = fond nuit, braise à droite, « MARDI » qui arrive de la caméra (×1.6, flou 18)
- handoff_out: à 3.70 : coupe franche voulue ; dernière image = la carte calendrier qui file floue à gauche (whip, flou 28 px), fond nuit, caption sortie

Word cues: Mardi@0.03 dix-neuf@0.67 heures@0.99 Votre@1.58 dernier@1.83 rendez-vous@2.19 vient@2.74 de@3.00 partir@3.10

Scene 1 (0.00 à 0.62 s) : P1, MARDI
  TEXTE ÉCRAN : kinetic « MARDI » Geist 900 320 px centré, slam à 0.03 avec chroma + shake ; pas de caption (le mot est le texte)
  ÉTAPES : 0.03 slam ; 0.10 shake 0.3 s ; 0.15 à 0.62 le mot dérive (scale 1 → 1.04), la braise glisse de x 1300 à 1240 ; 0.40 un label Geist Mono « MARDI 12 · SEMAINE 42 » se tape sous le mot (0.15 s)
  PISTE CAMÉRA : dérive push 5 %/s
  SON : impact-bass-1 à 0.03 ; key-press sur le label
  IMAGE CLÉ : 0.40 : « MARDI » géant crème sur nuit, braise orange en haut à droite, label mono dessous
Scene 2 (0.62 à 1.50 s) : P2, 19:00
  TEXTE ÉCRAN : kinetic horloge Geist 800 440 px « 19:00 » qui roule (18:57 → 18:59 → 19:00 en 0.15 s, FX.roll) ; caption « Mardi, [boîte : dix-neuf heures.] » mot à mot (Mardi, déjà là ; dix-neuf 0.67 ; heures 0.99)
  ÉTAPES : 0.62 coupe + flash 2 images ; 0.67 slam de l'horloge (chroma) ; 0.82 les chiffres « 19:00 » se posent ; 0.99 un trait orange 6 px se trace sous l'horloge ; 1.20 la braise pulse derrière
  PISTE CAMÉRA : punch-in ×1 → ×1.12 en 0.18 s à 0.67 puis dérive 3 %/s
  SON : whoosh-short 0.62 ; click-soft sur chaque cran de chiffre ; impact léger 0.67
  IMAGE CLÉ : 1.20 : « 19:00 » géant, trait orange dessous, caption « Mardi, [dix-neuf heures.] »
Scene 3 (1.50 à 3.70 s) : P3, le rendez-vous part
  TEXTE ÉCRAN : caption « Votre dernier rendez-vous vient de [boîte : partir.] » mot à mot ; dans la carte : label « MARDI 12 », lignes « 14:00 Point portefeuille », « 16:30 Appel assureur », « 18:00 RDV M. Lebrun · mutuelle famille »
  ÉTAPES : 1.50 coupe + flash ; 1.52 une carte calendrier .fx-card (900 × 560) inclinée rotateY -18° rotateX 8° arrive ×1.15 floue et se pose (0.2 s) ; 1.80 à 2.10 ses lignes se tapent ; 2.19 punch-in sur la ligne 18:00 (l'événement s'éclaire orange) ; 2.74 l'événement se soulève (ombre) ; 3.05 il file vers la gauche hors cadre (x -1400, rotation -12°, 3 copies fantômes à 30 % décalées de 0.03 s, flou 24) — contact 3.10 « partir » ; 3.20 la ligne reste vide avec une coche orange ; 3.40 whip-out de toute la scène vers la gauche
  PISTE CAMÉRA : dérive rotateY -18° → -10° ; punch ×1.35 à 2.19 ; whip 3.40
  SON : whoosh à 3.05 ; click-soft 3.20 ; whoosh-short 3.40
  IMAGE CLÉ : 3.10 : la carte inclinée, l'événement « RDV M. Lebrun » qui file en traînée floue à gauche, caption « …vient de [partir.] »

## Frame 2: La deuxième journée · 3.70 → 7.40

- scene: « DEUXIÈME JOURNÉE » kinetic in outline + fill over a dim empty generic CRM card; then the silent gag as a time-lapse montage of hard cuts every 0.25 s, ending frozen on 22:47
- duration: 3.70s
- transition_in: cut
- status: animated
- src: compositions/frames/02-deuxieme-journee.html
- voiceover: "Et votre deuxième journée commence."
- type: pain_point
- blueprint: kinetic-type-beats (Adapt)
- focal: DEUXIÈME JOURNÉE, then each shot of the gag
- rules: kinetic-beat-slam, beat-freeze-cut
- world: dark
- handoff_in: coupe franche voulue ; première image = fond nuit, braise à gauche, rien d'autre (le whip du frame 1 vient de sortir)
- handoff_out: à 3.70 : coupe franche voulue ; dernière image = « 22:47 » géant figé en chromatique, braise, grain

Word cues: Et@0.13 votre@0.24 deuxième@0.51 journée@0.93 commence@1.31 (silence de 1.79 à 3.70 : le gag muet)

Scene 1 (0.00 à 1.79 s) : P4, la deuxième journée
  TEXTE ÉCRAN : kinetic sur deux lignes : « DEUXIÈME » Geist 900 260 px en contour (.fx-k.outline) qui glisse de droite (0.51), « JOURNÉE » plein qui glisse de gauche (0.93) ; puis « commence. » Instrument Serif italique 200 px orange (.fx-k.hot) qui monte à 1.31 ; caption absente (le texte cinétique dit « deuxième journée commence », la caption montre seulement « Et votre » à 0.13 puis sort à 0.50)
  ÉTAPES : 0.00 derrière, flou 14 px et à 30 %, une carte « MON CRM · Nouveau prospect » vide avec un caret orange qui clignote ; 0.51 DEUXIÈME ; 0.93 JOURNÉE ; 1.31 commence. ; 1.50 tout pousse doucement
  PISTE CAMÉRA : dérive push 4 %/s
  SON : whoosh-short 0.51 et 0.93 ; impact doux 1.31
  IMAGE CLÉ : 1.50 : « DEUXIÈME » en contour, « JOURNÉE » plein, « commence. » serif orange, carte CRM floue derrière
Scene 2 (1.79 à 3.70 s) : P5, le gag time-lapse (muet)
  TEXTE ÉCRAN : aucun caption ; seuls textes : les heures et l'UI
  ÉTAPES : coupes franches avec flash 1 image toutes les ~0.24 s : 1.79 horloge « 20:12 » (Geist 800 400 px) ; 2.03 macro du champ « Nom » vide avec caret orange (clignote) ; 2.27 « 21:30 » ; 2.51 une tasse vue du dessus qui se vide (cercle brun qui rétrécit) ; 2.75 « 22:15 » ; 2.99 le caret, toujours seul ; 3.23 « 22:47 » qui slam (chroma, shake) et se FIGE : à 3.30 effet freeze (léger zoom ×1.06, décalage chromatique tenu 3 px, grain plus fort, lignes de balayage 4 %)
  PISTE CAMÉRA : chaque plan a son mini-zoom (×1 → ×1.05) ; plans alternés gauche/droite
  SON : glitch-1 sur chaque coupe (volume bas), click-soft sur chaque horloge, impact-bass-2 à 3.23
  IMAGE CLÉ : 3.40 : « 22:47 » géant figé, split chromatique, grain, braise

## Frame 3: Le conseil, pas la saisie · 7.40 → 13.20

- scene: « le conseil. » in serif over the broker's handwritten notes; cut to full orange: SAISIE slammed then crossed out; cut to split screen notebook | form being retyped; « fiche par fiche » multiplies the form into a wall
- duration: 5.80s
- transition_in: cut
- status: animated
- src: compositions/frames/03-saisie.html
- voiceover: "Votre métier, c'est le conseil. Pas la saisie. Pourtant, vous retapez vos notes, fiche par fiche."
- type: pain_point
- blueprint: overwhelm-surround (Adapt)
- focal: le conseil, SAISIE, the form, the wall of forms
- rules: kinetic-beat-slam, grid-card-assemble
- world: dark
- handoff_in: coupe franche voulue ; première image = fond nuit, une page de carnet inclinée (rotateX 10°) qui entre floue par le bas
- handoff_out: à 5.80 : coupe franche voulue ; dernière image = un mur de 16 fiches identiques en grille, caméra en recul, caption sortie

Word cues: Votre@0.09 métier@0.39 c'est@0.81 le@1.12 conseil@1.24 Pas@2.02 la@2.16 saisie@2.25 Pourtant@2.87 vous@3.38 retapez@3.60 vos@3.99 notes@4.16 fiche@4.66 par@4.98 fiche@5.17

Scene 1 (0.00 à 2.02 s) : P6, le conseil
  TEXTE ÉCRAN : caption « Votre métier, c'est » mot à mot (0.09 à 0.81) ; puis kinetic « le conseil. » Instrument Serif italique 260 px crème, rise à 1.12 (le caption s'arrête à « c'est », pas de doublon)
  ÉTAPES : 0.00 la page de carnet (papier crème, lignes, marge orange) entre en 3D et se pose à 0.25 ; 0.30 à 1.00 des notes manuscrites (Caveat) s'écrivent : « Louis Lebrun · 18:00 », « né le 10/10/1978, Paris 15e », « mutuelle santé famille » ; 1.05 flèche orange « → conseil : garanties renforcées » ; 1.12 la page recule floue (profondeur) et « le conseil. » monte devant
  PISTE CAMÉRA : dérive rotateX 10° → 4°
  SON : stylo (typing très bas) 0.3 à 1.0 ; whoosh doux 1.12
  IMAGE CLÉ : 1.60 : « le conseil. » serif géant devant la page de notes floue
Scene 2 (2.02 à 2.80 s) : P7, pas la saisie
  TEXTE ÉCRAN : kinetic « SAISIE » Geist 900 380 px noir (.fx-k.ink) sur fond orange plein (.fx-orange), précédé de « PAS LA » Geist Mono 40 px ; pas de caption
  ÉTAPES : 2.02 coupe sur fond orange + flash ; 2.02 « PAS LA » se tape ; 2.25 SAISIE slam (shake) ; 2.45 une barre noire 24 px barre le mot de gauche à droite en 0.12 s
  PISTE CAMÉRA : punch ×1.1 à 2.25
  SON : impact-bass-1 à 2.25 ; whoosh-short 2.45
  IMAGE CLÉ : 2.55 : « SAISIE » noir barré sur orange plein
Scene 3 (2.80 à 5.80 s) : P8, retaper fiche par fiche
  TEXTE ÉCRAN : caption « Pourtant, vous [boîte : retapez] vos notes, » (2.87 à 4.16) ; puis kinetic « FICHE PAR FICHE » en bandeau défilant Geist 900 160 px en contour (4.66 → 5.80) ; le caption sort à 4.60
  ÉTAPES : 2.80 coupe : écran partagé marges égales, à gauche le carnet (notes), à droite une fiche « MON CRM · Nouveau prospect » (.fx-card) ; 3.60 le caret retape « Lebrun » (0.05 s/lettre), 3.95 « 10/10/1978 », 4.20 « Paris » ; 4.66 coupe : la fiche seule au centre ; 4.66 / 4.98 / 5.17 elle se multiplie : 2, 4, puis 16 fiches en grille (chaque palier en 0.1 s, depuis le centre) pendant que la caméra recule ; le bandeau « FICHE PAR FICHE PAR FICHE » défile devant, en contour
  PISTE CAMÉRA : dérive ; recul ×1 → ×0.55 de 4.66 à 5.80 (power2.out)
  SON : typing 3.60 à 4.40 ; pop à 4.66 / 4.98 / 5.17
  IMAGE CLÉ : 5.40 : le mur de 16 fiches identiques, le bandeau « FICHE PAR FICHE » en contour devant

## Frame 4: Case par case · 13.20 → 16.20

- scene: the advice form in 3D; each « case » is a hard cut to an extreme macro of a box being ticked by the mouse, with shake
- duration: 3.00s
- transition_in: cut
- status: animated
- src: compositions/frames/04-case-par-case.html
- voiceover: "Vous remplissez le devoir de conseil, case par case."
- type: pain_point
- blueprint: cursor-ui-demo (Adapt)
- focal: the form, then each box
- rules: press-release-spring, kinetic-beat-slam
- world: dark
- handoff_in: coupe franche voulue ; première image = fond nuit, la fiche de conseil inclinée qui entre ×1.2 floue
- handoff_out: à 3.00 : coupe franche voulue ; dernière image = macro de la 3e case cochée, flou de mouvement, caption « case par case. »

Word cues: Vous@0.10 remplissez@0.31 le@0.84 devoir@0.94 de@1.26 conseil@1.36 case@2.00 par@2.27 case@2.47

Scene 1 (0.00 à 2.00 s) : P9, la fiche de conseil
  TEXTE ÉCRAN : caption « Vous remplissez le devoir de conseil, [boîte : case par case.] » mot à mot sur tout le frame (la boîte s'ouvre à 2.00) ; dans la fiche : « Fiche de conseil · Mutuelle santé », « Modèle_DDA_v3.docx », 5 lignes à cases vides
  ÉTAPES : 0.00 la fiche (document blanc 1100 × 640) entre inclinée rotateX 14° rotateY 10° ×1.2 floue et se pose (0.25 s) ; 0.40 lignes qui se tapent ; 0.90 la flèche de souris arrive en courbe (0.4 s) ; 1.50 lente poussée vers la 1re case
  PISTE CAMÉRA : dérive rotateY 10° → 4° ; push 4 %/s
  SON : pop 0.05
  IMAGE CLÉ : 1.40 : la fiche blanche inclinée sur la nuit, 5 cases vides, la flèche
Scene 2 (2.00 à 3.00 s) : P10, case · par · case
  TEXTE ÉCRAN : caption continue
  ÉTAPES : 2.00 coupe macro 1 (case « Besoins exprimés » remplissant le cadre, ×6) : la flèche clique, coche orange tracée en 0.06 s, shake ; 2.27 coupe macro 2 (case « Situation familiale », angle opposé) : idem ; 2.47 coupe macro 3 (case « Budget », plus serré encore) : idem + chroma ; 2.80 flou de mouvement
  PISTE CAMÉRA : chaque macro a un micro-zoom ×1 → ×1.08
  SON : click à 2.00 / 2.27 / 2.47 (fort)
  IMAGE CLÉ : 2.55 : macro d'une case cochée orange, flèche de souris, grain, caption « …[case par case.] »

## Frame 5: Samedi soir, lundi · 16.20 → 19.50

- scene: a 3D iPhone floating in the night receives a glowing WhatsApp notification on Saturday 21:14; behind it giant days scroll SAM → DIM → LUN; LUNDI. slams in serif; the notification goes grey, unanswered
- duration: 3.30s
- transition_in: cut
- status: animated
- src: compositions/frames/05-samedi.html
- voiceover: "Et le prospect qui vous écrit samedi soir... attend lundi."
- type: pain_point
- blueprint: device-surface-showcase (Adapt)
- focal: the notification, then LUNDI
- rules: vertical-spring-ticker, kinetic-beat-slam
- world: dark
- handoff_in: coupe franche voulue ; première image = fond nuit, l'iPhone qui entre de bas en haut incliné (rotateX 20°), écran verrouillé « samedi 16 · 21:14 »
- handoff_out: à 3.30 : coupe franche voulue (vers le noir du pivot) ; dernière image = « lundi. » serif géant, iPhone en arrière-plan flou, notification grise

Word cues: Et@0.09 le@0.20 prospect@0.30 qui@0.73 vous@0.89 écrit@1.10 samedi@1.36 soir@1.68 attend@2.44 lundi@2.75

Scene 1 (0.00 à 2.30 s) : P11, samedi soir
  TEXTE ÉCRAN : caption « Et le prospect qui vous écrit [boîte : samedi soir…] » mot à mot ; derrière l'iPhone, kinetic géant en contour 30 % « SAMEDI » Geist 900 420 px qui défile lentement
  ÉTAPES : 0.00 l'iPhone monte en 3D et se pose (0.3 s), halo bleuté de l'écran ; 0.95 la notification glass « WhatsApp · Camille R. · Bonjour, je cherche une mutuelle pour ma famille. Vous pouvez me faire un devis ? » tombe du haut avec un glow orange pulsé ; 1.36 « SAMEDI » derrière s'éclaire ; 1.80 le téléphone tourne doucement (rotateY 12° → -8°)
  PISTE CAMÉRA : dérive push 3 %/s
  SON : whoosh 0.05 ; notification à 1.05
  IMAGE CLÉ : 1.80 : iPhone incliné qui flotte, notification qui brille, « SAMEDI » géant en contour derrière
Scene 2 (2.30 à 3.30 s) : P12, attend lundi
  TEXTE ÉCRAN : le mot géant derrière roule verticalement « SAMEDI » → « DIMANCHE » (2.44) → « LUNDI » (2.70) ; puis kinetic « lundi. » Instrument Serif italique 300 px orange chaud qui slam DEVANT à 2.75 ; caption « attend » à 2.44 puis remplacée par le kinetic
  ÉTAPES : 2.30 l'écran verrouillé passe « dimanche 17 » (2.44) puis « lundi 18 · 08:30 » (2.70) ; 2.75 slam « lundi. » + shake ; 2.85 la notification devient grise ; 3.00 l'iPhone recule flou
  PISTE CAMÉRA : punch ×1.15 à 2.75
  SON : click-soft 2.44, 2.70 ; impact-bass-2 2.75
  IMAGE CLÉ : 3.00 : « lundi. » serif orange géant devant l'iPhone flou et sa notification grise

## Frame 6: Et si vous arrêtiez d'écrire ? · 19.50 → 21.95

- scene: silence on black: the question appears word by word in serif italic, the orange caret erases it, then stretches into a bar of light that explodes
- duration: 2.45s
- transition_in: cut
- status: animated
- src: compositions/frames/06-pivot.html
- voiceover: "Et si vous arrêtiez d'écrire ?"
- type: pivot
- blueprint: kinetic-type-beats (Adapt)
- focal: the question, then the caret
- rules: context-sensitive-cursor, discrete-text-sequence
- world: dark
- handoff_in: coupe franche voulue ; noir #050507, le caret orange 6 × 96 px centré en (500, 880)
- handoff_out: à 2.45 : flash de l'orchestrateur au maximum depuis (500, 880) ; dessous, une barre de lumière orange verticale 10 × 160 px centrée en (500, 880)

Word cues: Et@0.09 si@0.20 vous@0.30 arrêtiez@0.51 d'écrire@0.93 (silence de 1.41 à 2.45)

Scene 1 (0.00 à 2.45 s) : P13, le pivot
  TEXTE ÉCRAN : kinetic centré « Et si vous arrêtiez d'écrire ? » Instrument Serif italique 120 px crème, mot à mot sur les cues, le caret avance ; pas de caption
  ÉTAPES : 0.09 à 0.93 les mots ; 0.51 le caret cesse de clignoter ; 1.45 à 1.85 le caret efface la phrase de droite à gauche (une lettre / 0.014 s) ; 1.90 caret seul ; 2.05 il vibre ; 2.15 il s'étire en barre 10 × 160 px avec halo ; 2.30 un anneau de lumière part de la barre
  PISTE CAMÉRA : push 1.5 %/s
  SON : key-press 1.50 à 1.90 ; riser jusqu'à 2.33
  IMAGE CLÉ : 1.20 : noir, la question en serif italique crème, le caret orange fixe

## Frame 7: Vous parlez, la fiche s'écrit · 21.95 → 26.70

- scene: warm paper and orange light; a full-width waveform driven by the real voice with « Synapze » and « parlez. »; cut to the real Synapze screen floating in 3D with punch-ins on the transcription and on the IA fields filling
- duration: 4.75s
- transition_in: cut
- status: animated
- src: compositions/frames/07-vous-parlez.html
- voiceover: "Avec Synapze, vous parlez. Une note vocale après le rendez-vous, et la fiche client s'écrit."
- type: demo
- blueprint: panel-edit-live-sync (Adapt)
- focal: the waveform + parlez, then the real screen
- rules: stat-bars-and-fills, coordinate-target-zoom
- world: light
- handoff_in: flash de l'orchestrateur au maximum ; sous le flash, fond papier .fx-paper, la barre orange 10 × 160 px centrée en (500, 880)
- handoff_out: à 4.75 : coupe franche voulue ; dernière image = punch-in sur le bloc Identité rempli (puces IA), caption « …[s'écrit.] »

Word cues: Avec@0.11 Synapze@0.36 vous@0.87 parlez@1.12 Une@1.86 note@2.00 vocale@2.18 après@2.45 le@2.68 rendez-vous@2.77 et@3.48 la@3.57 fiche@3.67 client@3.90 s'écrit@4.18

Scene 1 (0.00 à 1.86 s) : P14, vous parlez
  TEXTE ÉCRAN : caption « Avec [boîte : Synapze,] vous » (0.11 à 0.87) ; puis kinetic « parlez. » Instrument Serif italique 280 px noir, rise à 1.12 (au-dessus de l'onde) ; le caption sort à 1.05
  ÉTAPES : 0.00 la barre se démultiplie en une forme d'onde pleine largeur (90 barres, depuis le centre, 0.012 s d'écart) ; 0.40 l'onde suit l'amplitude réelle ; 0.36 « Synapze » ; 0.80 pastille « ● Enregistrement… » (.fx-pill) se pose au-dessus ; 1.12 « parlez. » ; pic de l'onde
  PISTE CAMÉRA : dérive pull -2 %/s
  SON : pop 0.80
  IMAGE CLÉ : 1.40 : onde orange pleine largeur sur papier lumineux, « parlez. » serif noir géant, pastille Enregistrement
Scene 2 (1.86 à 4.75 s) : P15, la fiche s'écrit
  TEXTE ÉCRAN : caption « Une note vocale après le rendez-vous, et la fiche client [boîte : s'écrit.] » mot à mot ; label « TRANSCRIPTION IA » visible dans l'écran réel
  ÉTAPES : 1.86 coupe : l'écran réel Synapze (vn-01 → vn-22, swaps discrets) dans un cadre glass .fx-card.light 1500 × 844, incliné rotateY -16° rotateX 6°, qui se redresse à -6° en 0.6 s, glow orange dessous ; 2.40 à 3.40 la transcription s'écrit (vn-02 à vn-10) — punch-in ×1.6 sur la carte de transcription à 2.45 ; 3.48 à 4.18 les champs IA se remplissent (vn-11 à vn-16) — punch déplacé sur le bloc Identité à 3.48 ; 4.18 « REMPLIE AUTOMATIQUEMENT » : un éclat orange court sur le bloc
  PISTE CAMÉRA : punches à 2.45 et 3.48 (expo.out 0.2 s) puis dérive
  SON : typing 2.45 à 3.40 (bas) ; ping 4.18
  IMAGE CLÉ : 4.00 : punch sur le bloc Identité de l'écran réel, puces IA, caption « …la fiche client [s'écrit.] »

## Frame 8: Tout seul, traçable · 26.70 → 29.65

- scene: the same advice form, now on paper light: its five boxes tick themselves in cascade with IA chips and sparks, a completeness ring fills, the stamp slams on « traçable »
- duration: 2.95s
- transition_in: cut
- status: animated
- src: compositions/frames/08-tracable.html
- voiceover: "Le devoir de conseil se remplit tout seul, traçable."
- type: demo
- blueprint: agent-progress-theater (Adapt)
- focal: the boxes ticking themselves, then the stamp
- rules: stat-bars-and-fills, kinetic-beat-slam
- world: light
- handoff_in: coupe franche voulue ; première image = fond papier, la fiche de conseil blanche (même maquette qu'au frame 4) qui entre ×1.2 floue, inclinée
- handoff_out: à 2.95 : coupe franche voulue ; dernière image = whip vers la droite (flou 28 px) sur la fiche complète

Word cues: Le@0.06 devoir@0.17 de@0.49 conseil@0.60 se@0.97 remplit@1.08 tout@1.46 seul@1.67 traçable@2.17

Scene 1 (0.00 à 2.95 s) : P16, ça se remplit tout seul
  TEXTE ÉCRAN : caption « Le devoir de conseil se remplit [boîte : tout seul,] traçable. » mot à mot ; dans la fiche « Fiche de conseil · Santé Individuel », « Louis Lebrun · remplie automatiquement », les 5 lignes, anneau « COMPLÉTUDE »
  ÉTAPES : 0.00 la fiche entre inclinée et se pose (0.25 s) ; 1.08 cascade : les 5 cases se cochent seules (0.1 s d'écart), chaque coche avec une puce « IA » et 6 étincelles orange qui jaillissent (positions déterministes) ; 1.10 l'anneau se remplit 0 → plein (0.6 s) ; 2.10 le tampon « PISTE D'AUDIT · HORODATÉE » slam depuis la caméra (×3.4 flou → ×1, rotation -6°), contact 2.17 + shake ; 2.65 whip-out droite
  PISTE CAMÉRA : rotateY 12° → 0° pendant la cascade ; punch ×1.08 à 2.17
  SON : click-soft ×5 1.08 à 1.48 ; sparkle 1.20 ; impact-bass-1 2.17 ; whoosh-short 2.70
  IMAGE CLÉ : 2.30 : la fiche blanche sur papier lumineux, 5 cases orange avec puces IA, anneau plein, tampon posé de biais

## Frame 9: Jour et nuit · 29.65 → 32.95

- scene: a 3D iPhone with the WhatsApp copy: Camille's Saturday question gets an instant answer at 21:14; on « jour et nuit » the frame splits: left warm day, right deep night, the clock jumps to 03:12 and the assistant answers again
- duration: 3.30s
- transition_in: cut
- status: animated
- src: compositions/frames/09-whatsapp.html
- voiceover: "Sur WhatsApp, votre assistant répond à vos clients, jour et nuit."
- type: demo
- blueprint: comparison-split (Adapt)
- focal: the answer bubble, then the day / night split
- rules: vertical-spring-ticker, kinetic-beat-slam
- world: light
- handoff_in: coupe franche voulue ; première image = fond papier, l'iPhone WhatsApp qui arrive par la droite (whip-in), incliné rotateY -14°
- handoff_out: à 3.30 : coupe franche voulue ; dernière image = écran partagé jour / nuit, les deux iPhones, caption « …[jour et nuit.] »

Word cues: Sur@0.09 WhatsApp@0.25 votre@0.72 assistant@0.99 répond@1.46 à@1.78 vos@1.83 clients@1.99 jour@2.57 et@2.78 nuit@2.89

Scene 1 (0.00 à 2.57 s) : P17, l'assistant répond
  TEXTE ÉCRAN : caption « Sur WhatsApp, votre assistant répond à vos clients, [boîte : jour et nuit.] » mot à mot (la boîte à 2.57)
  ÉTAPES : 0.00 whip-in de l'iPhone ; 0.25 WhatsApp : « Camille R. · en ligne », pastille « Samedi », bulle « Bonjour, je cherche une mutuelle pour ma famille. Vous pouvez me faire un devis ? » 21:14 ; 0.95 trois points ; 1.40 la réponse jaillit (bulle verte ×1.15 → ×1) « Bonjour Camille, je suis l'assistant IA du cabinet. Pour préparer votre devis : combien de personnes à couvrir ? » 21:14, coches bleues ; punch ×1.25 sur la réponse à 1.46
  PISTE CAMÉRA : rotateY -14° → -4°
  SON : whoosh 0.00 ; notification 1.46
  IMAGE CLÉ : 1.80 : iPhone incliné, la question 21:14 et la réponse verte instantanée, punch
Scene 2 (2.57 à 3.30 s) : P18, jour / nuit
  TEXTE ÉCRAN : kinetic « JOUR » (gauche) et « NUIT » (droite) Geist 900 200 px, en contour, derrière les téléphones
  ÉTAPES : 2.57 coupe : écran partagé par un trait vertical orange qui s'ouvre du centre ; à gauche fond papier chaud (soleil : disque orange flou), « JOUR », l'iPhone à 21:14 ; à droite fond nuit bleu profond #0B1424, « NUIT » (2.89), le même fil à « 03:12 » avec « Nous sommes quatre, deux adultes et deux enfants. » et la réponse instantanée « Parfait. Je prépare trois offres adaptées à votre famille. » (2.95)
  PISTE CAMÉRA : dérive pull -2 %/s
  SON : whoosh-short 2.57 ; pop 2.95
  IMAGE CLÉ : 3.10 : écran partagé jour / nuit, deux iPhones, « JOUR » et « NUIT » géants en contour

## Frame 10: Imbattable · 32.95 → 36.45

- scene: « L'IA ne remplace pas le courtier. » kinetic; a 0.6 s fly-through recap of the film's interfaces; IMBATTABLE slams in hot gradient with shimmer and shake; the clock lands on 19:05; everything collapses into an orange line
- duration: 3.50s
- transition_in: cut
- status: animated
- src: compositions/frames/10-imbattable.html
- voiceover: "L'IA ne remplace pas le courtier. Elle le rend imbattable."
- type: payoff
- blueprint: kinetic-type-beats (Adapt)
- focal: le courtier, then IMBATTABLE
- rules: kinetic-beat-slam, gradient-text-sweep
- world: light
- handoff_in: coupe franche voulue ; première image = fond papier, « L'IA » Geist 900 noir qui monte
- handoff_out: à 3.50 : un trait orange horizontal de 300 px × 4 px centré en (500, 880) (x 350 à 650) avec un point de 18 px à son extrémité gauche (350, 880), fond qui vient de virer au nuit #050507

Word cues: L'IA@0.13 ne@0.37 remplace@0.48 pas@0.96 le@1.13 courtier@1.25 Elle@2.06 le@2.25 rend@2.35 imbattable@2.71

Scene 1 (0.00 à 2.06 s) : P19, le courtier
  TEXTE ÉCRAN : kinetic sur deux lignes : « L'IA ne remplace pas » Geist 700 90 px noir (mot à mot sur les cues) puis « le courtier. » Instrument Serif italique 260 px noir, rise à 1.13 ; pas de caption
  ÉTAPES : 0.13 à 0.96 la première ligne ; 1.13 « le courtier. » ; 1.40 à 2.00 derrière le texte, un défilé rapide (fly-through, 5 cartes, 0.12 s chacune, du fond vers la caméra) : la carte calendrier, le carnet, l'écran Synapze réel (vn-22), la fiche de conseil cochée, l'iPhone WhatsApp — floues, à 40 %
  PISTE CAMÉRA : push 4 %/s
  SON : whoosh 1.40
  IMAGE CLÉ : 1.60 : « le courtier. » serif noir géant, cartes du film qui traversent floues derrière
Scene 2 (2.06 à 3.50 s) : P20, imbattable
  TEXTE ÉCRAN : caption « Elle le rend » (2.06 à 2.35) puis kinetic « IMBATTABLE. » Geist 900 300 px en dégradé chaud (.fx-k.hot) slam à 2.71 (chroma + shake), shimmer qui traverse ; sous le mot, petite horloge Geist Mono « 19:05 » qui roule 19:00 → 19:05 à 2.90
  ÉTAPES : 2.71 slam ; 2.80 shimmer 0.5 s ; 2.90 horloge ; 3.10 à 3.45 tout se contracte au centre en un trait orange de 360 px (power3.in), le fond vire au nuit
  PISTE CAMÉRA : punch ×1.12 à 2.71
  SON : impact-bass-1 2.71 ; whoosh 3.10
  IMAGE CLÉ : 2.95 : « IMBATTABLE. » en dégradé orange chaud géant sur papier, shimmer, « 19:05 » dessous

## Frame 11: Le courtier parle · 36.45 → 43.80

- scene: on night, the orange line becomes the logo « • Synapze • »; the promise « Le courtier parle. L'IA fait tout le reste. »; the button « Demander une démo » glows, a cursor clicks it directly; living hold; iris to black
- duration: 7.35s
- transition_in: cut
- status: animated
- src: compositions/frames/11-fin.html
- voiceover: "Synapze. Le courtier parle, l'IA fait tout le reste. Demandez votre démo."
- type: cta
- blueprint: logo-assemble-lockup (Adapt)
- focal: the wordmark, then the CTA button
- rules: cursor-click-ripple, press-release-spring
- world: dark
- handoff_in: à 0.00 : un trait orange horizontal de 300 px × 4 px centré en (500, 880) (x 350 à 650) avec un point de 18 px à son extrémité gauche (350, 880), fond nuit #050507
- handoff_out: aucun (fin du film, iris à 7.35)

Word cues: Synapze@0.14 Le@0.92 courtier@1.03 parle@1.47 l'IA@2.00 fait@2.21 tout@2.42 le@2.64 reste@2.74 Demandez@3.41 votre@3.81 démo@4.05 (hold to 7.35)

Scene 1 (0.00 à 0.90 s) : P21, le logo
  TEXTE ÉCRAN : logo « • Synapze • » Geist 800 160 px crème, points orange
  ÉTAPES : 0.00 le point devient le point gauche ; 0.05 à 0.40 les lettres montent d'un masque (rise, 0.035 s d'écart) sur le trait ; 0.42 point droit ; 0.50 le trait devient soulignement fin ; braise derrière
  SON : sparkle 0.50
  IMAGE CLÉ : 0.60 : « • Synapze • » crème sur nuit, braise
Scene 2 (0.90 à 3.30 s) : P22, la promesse
  TEXTE ÉCRAN : kinetic centré deux lignes : « Le courtier parle. » Geist 800 110 px crème (mot à mot), « L'IA fait tout le reste. » avec « le reste. » en Instrument Serif italique orange chaud (mot à mot) ; le logo est monté en haut
  ÉTAPES : 0.92 à 2.74 les mots ; 3.00 léger shimmer sur « le reste. »
  IMAGE CLÉ : 2.90 : logo en haut, promesse sur deux lignes, « le reste. » serif orange
Scene 3 (3.30 à 7.35 s) : P23, le clic
  TEXTE ÉCRAN : bouton « Demander une démo » (.fx-pill élargi, 40 px) avec glow ; « synapze.eu » Geist Mono dessous
  ÉTAPES : 3.35 le bouton slam doux ; 3.60 url ; 3.70 curseur en une courbe (0.45 s) ; 4.15 clic direct : pression, onde, flash orange doux ; 4.30 une fine onde orange respire sous le bouton ; 4.30 à 6.90 tenue vivante (braise qui dérive, grain) ; 6.90 à 7.35 iris noir sur le bouton
  SON : click 4.15 ; chime 4.20
  IMAGE CLÉ : 4.30 : logo, promesse, bouton orange cliqué avec onde, url, fine onde dessous
