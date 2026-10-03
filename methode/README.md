# La méthode « Synapze V2 » : faire un motion design de lancement qui bluffe

Ce dossier explique comment refaire, pour n'importe quel client, un film comme `synapze-v2/` (43,8 s : typographie
cinétique, coupes sur les mots, impacts, interfaces réelles en 3D, musique et 80 bruitages calés à l'image).

| fichier | pour quoi |
|---|---|
| `README.md` (ce fichier) | la méthode de bout en bout, ce qu'il faut, combien de temps, les contrôles qualité |
| `PROMPTS.md` | les prompts prêts à coller dans Claude Code, étape par étape |
| `BRIEF-CLIENT.md` | le questionnaire à envoyer au client avant de commencer |
| `BUSINESS.md` | en faire une activité : offres, prix, déroulé client, droits, prospection |
| `INSTALLATION.md` | utiliser la méthode dans **n'importe quelle** session Claude Code (plugin `motion-studio`) |

Côté Claude, la méthode est un skill générique, valable pour n'importe quelle marque : `.claude/skills/motion-design-kinetic/`
(dans l'atelier) et le plugin `motion-studio` (partout ailleurs, voir `INSTALLATION.md`). Synapze (`synapze-v2/`,
`synapze-v2-vertical/`) n'est qu'un exemple de référence.

**Nouveau : il suffit de donner l'adresse du site du client.** Claude le lit avec un navigateur (textes, preuves
chiffrées avec leur source, tarifs, boutons, ton, couleurs, polices, logo, captures desktop et mobile, vidéos de
démo), écrit le dossier `brand/BRAND.md`, applique la charte de la marque au kit (couleur, fonds, polices) et part de
là pour le script. Formats 16:9 et 9:16 natifs, exports web / réseaux sociaux / WhatsApp vérifiés.

---

## 1. Ce qu'il te faut

- **Claude Code**, n'importe où, avec le plugin `motion-studio` (`INSTALLATION.md`), ou ce dépôt ouvert directement.
  Tout le reste s'installe tout seul (HyperFrames, Chromium, ffmpeg, polices, GSAP, musiques libres).
- Un compte **ElevenLabs** (offre payante pour l'usage commercial de la voix).
- Du client : **l'adresse de son site** (le reste en est tiré), le brief (`BRIEF-CLIENT.md`) et, idéalement, **un
  enregistrement d'écran de son vrai produit**. C'est ce qui rend le film crédible.

## 2. Le déroulé (7 étapes, 4 validations)

```
0 Brief ─► 1 Script ✔ ─► 2 Voix ✔ ─► 3 Storyboard ✔ ─► 4 Animation ─► 5 Musique ✔ ─► 6 Vérification ─► 7 Livraison
```

| étape | qui fait quoi | durée réelle |
|---|---|---|
| 0. Brief | tu remplis le questionnaire avec le client, Claude crée le projet et installe le kit | 30 min |
| 1. Script ✔ | Claude propose des concepts puis 2 versions complètes ; tu (ou le client) choisis et corriges | 30 min à 1 h |
| 2. Voix ✔ | tu génères la voix dans ElevenLabs avec le texte et les réglages fournis ; Claude monte la voix à la bonne durée | 20 min |
| 3. Storyboard ✔ | Claude écrit le plan de tournage seconde par seconde (coupes, effets, sons) ; option : 3 directions visuelles en images fixes | 1 h |
| 4. Animation | Claude lance **un agent par séquence, en parallèle** (11 agents pour Synapze) | 30 à 60 min, sans toi |
| 5. Musique ✔ | 2 musiques libres de droits (tension puis élan), bruitages calés ; tu choisis à l'oreille | 20 min |
| 6. Vérification | rendu, planches d'images toutes les 0,25 s, son, durée, images figées ; corrections via les agents | 30 min à 1 h |
| 7. Livraison | MP4 1080p, variante musicale, liste honnête des réserves | 5 min |

Compte **une demi-journée à une journée** de travail réel pour un film de 30 à 60 s, dont la moitié en attente
pendant que les agents travaillent.

## 3. Pourquoi ça bluffe (les 6 règles qui ont fait passer la V1 « linéaire » à la V2)

1. **La voix est l'horloge, l'image coupe sur ses mots.** Une coupe par seconde environ dans la partie
   « problème », un gag muet qui coupe toutes les 0,25 s, chaque silence devient une action.
2. **La typographie est l'héroïne.** Trois registres : gros mots cinétiques (Geist 900), un seul mot d'émotion en
   serif italique (Instrument Serif), sous-titres mot à mot avec un mot-clé dans une boîte de couleur.
3. **Les impacts se sentent.** Le mot arrive trop gros et flou, claque en 4 images avec un décalage rouge/bleu et une
   secousse de caméra, et un son d'impact. Plus : coups de fouet, zooms brusques, flashs, chiffres qui défilent.
4. **Trois mondes qui racontent l'histoire.** Nuit pour le problème, noir pour le pivot, papier lumineux pour la
   solution, nuit pour la fin. Une seule couleur : celle de la marque.
5. **Le vrai produit, en 3D.** Les vraies interfaces du client, inclinées, avec lueur et grain. Jamais redessinées,
   jamais de chiffres inventés.
6. **Des rimes.** Trois échos entre problème et solution (19:00 → 22:47 → 19:05 ; la notification du samedi 21:14 →
   la réponse à 21:14 ; la case cochée à la main → cochée toute seule). C'est ce dont le spectateur se souvient.

Détail technique complet : `.claude/skills/motion-design-kinetic/references/edit-grammar.md`.

## 4. Les contrôles avant de livrer (Claude les fait, toi tu regardes le résultat)

- Durée exacte, image et son présents, aucune erreur de décodage, aucune image figée hors carte de fin.
- Son : -16 LUFS (norme web), crête ≤ -1,5 dB.
- Planches d'images toutes les 0,25 s lues en entier : pas d'image vide, rien de coupé, un seul centre d'attention,
  texte lisible, chaque mot à l'écran au moment où il est dit.
- Chaque défaut est renvoyé à l'agent de la séquence concernée, puis nouveau rendu.

## 5. Démarrer un nouveau film

Dans n'importe quelle session Claude Code (plugin installé) :

```
Fais un motion design pour https://site-du-client.com : 40 s, en 16:9 et en 9:16, bouton « Réserver une démo ».
```

Variantes et prompts détaillés : `PROMPTS.md`.
