# Prompts prêts à coller (Claude Code, ce dépôt)

Un prompt par étape. Remplace ce qui est entre `[crochets]`. Chaque prompt se termine par une validation : Claude
s'arrête et attend ton « go ». Ils marchent pour n'importe quelle marque (Synapze n'était que le premier film).

---

## Prompt 0 — Lancer un film à partir d'un site (le plus court)

```
Fais un motion design pour [https://site-du-client.com].
Format : [16:9 pour le site / 9:16 pour TikTok-Reels / les deux] · Durée : [30-45 s]
Bouton final : « [Réserver une démo] » · Langue : [français] · Prononciation de la marque : [« … »]
Matière en plus : [chemin d'un enregistrement d'écran du produit, logo SVG] (facultatif)
```
Claude lit le site (dossier `brand/BRAND.md` : promesse, fonctionnalités, preuves chiffrées avec leur source, tarifs,
boutons, ton, palette, polices, logo, captures desktop et mobile, vidéos de démo), applique la charte de la marque au
kit, puis te montre le brief en 8 lignes et les concepts de script.

## Prompt 0 bis — Version détaillée (quand tu as un vrai brief client)

```
<rôle>
Tu es le réalisateur et l'orchestrateur d'un film de lancement en motion design. Tu suis le skill motion-studio
(ou motion-design-kinetic dans l'atelier) de bout en bout. Le niveau attendu : un film de lancement d'une startup de
2026 (Linear, Vercel, Arc), qui bluffe dès la première seconde.
</rôle>

<client>
Site : [url] (lis-le avec site-intel avant tout)
Marque : [nom] — prononciation : [« … »]
Cible : [qui regarde] · Douleur n°1 : [...] · Promesse : [...]
Diffusion : [landing page 16:9 / reel 9:16 / LinkedIn] · Durée visée : [30-45 s]
Appel à l'action : [texte du bouton + url]
Ton : [sérieux / complice / premium] · Couleur imposée : [#hex ou « celle du site »]
Matière réelle : [captures / vidéo de démo déposées dans le dépôt]
Interdits : [chiffres non validés, concurrents, etc.]
</client>

<consignes>
- Installe tout ce qui manque sans me demander.
- Montre-moi d'abord le BRIEF.md tiré du site (8 lignes) et les preuves chiffrées trouvées, pour que je valide ce qui
  peut être cité.
- Puis passe à l'étape 1 (script) et arrête-toi à sa validation.
</consignes>
```

## Prompt 1 — Script

```
<tâche>Écris le script du film dans [projet]/SCRIPT.md.</tâche>
<méthode>
1. Propose 6 concepts en une ligne chacun (angle, première image, pivot).
2. Écris les 2 meilleurs en entier, en 6 temps : accroche datée et concrète (un jour, une heure) · gag muet de 2 à 3 s ·
   3 douleurs concrètes du quotidien de la cible · pivot sur fond noir (une question ou une phrase courte) ·
   la solution et ses bénéfices, avec le nom de la marque · promesse + appel à l'action.
3. Phrases courtes, une idée par phrase, 170 à 180 mots par minute de voix, nombres en lettres.
4. Pour chaque version : la version mise en scène (avec les images) ET la version à coller dans ElevenLabs
   (texte seul, marque écrite phonétiquement, ponctuation pour les pauses, aucune balise de pause).
5. Termine par 3 « rimes » possibles entre problème et solution (un même objet ou une même heure qui revient).
</méthode>
<validation>Arrête-toi : je choisis une version et je corrige mot à mot.</validation>
```

## Prompt 2 — Voix

```
J'ai déposé la voix ElevenLabs dans [projet]/assets/audio/voix.mp3.
Monte-la pour que le film dure entre [40] et [45] s : raccourcis les pauses trop longues, garde de la place pour le
gag muet et le pivot, coupe seulement dans les silences. Puis calcule le temps de chaque mot (mots.py) et liste les
silences de plus de 0,4 s. Donne-moi la durée finale et fais-moi écouter le montage.
```

Réglages ElevenLabs à utiliser : modèle v3/v4 récent, langue forcée, Stabilité 40-50 %, Similarité 80-90 %,
2 ou 3 prises, garder la meilleure.

## Prompt 3 — Storyboard

```
<tâche>Écris [projet]/frame.md (depuis le modèle du skill) et [projet]/STORYBOARD.md.</tâche>
<sources>SCRIPT.md validé · voix-montage-mots.json · references/edit-grammar.md du skill · synapze-v2/STORYBOARD.md
comme exemple de niveau de détail.</sources>
<exigences>
- En-tête : MONDE (nuit / noir / papier / nuit), SIGNATURES (2 mécanismes récurrents avec chaque instant où ils
  frappent), 3 RIMES, PARTITION CAMÉRA, VOIX (silences), COUPES (environ une par seconde dans le problème, gag toutes
  les 0,25 s), RYTHME, SON.
- Par séquence : coupes sur les mots, scènes datées toutes les 0,1 à 0,4 s (TEXTE ÉCRAN exact, ÉTAPES, PISTE
  CAMÉRA, SON, IMAGE CLÉ), raccords d'entrée et de sortie décrits au pixel.
- Un seul centre d'attention à la fois, chaque phrase lisible sans le son, pas de marque avant qu'elle soit dite,
  les vraies interfaces jamais redessinées.
- Option : rends 3 directions visuelles en images fixes (une image clé par séquence) pour que je choisisse.
</exigences>
<validation>Arrête-toi et montre-moi les images clés.</validation>
```

## Prompt 4 — Animation (agents en parallèle)

```
<rôle>Tu orchestres l'animation. Tu ne codes aucune séquence toi-même : un agent par séquence.</rôle>
<étapes>
1. Construis les paquets (frame-packets.mjs), vérifie qu'il ne reste aucun « {{ » dans frame.md et STORYBOARD.md.
2. Pour chaque séquence, remplis templates/dispatch.md du skill (chemins absolus, « Frame notes » avec les raccords au
   pixel et ce qui doit frapper le plus fort). Lance TOUS les agents dans un seul message, en arrière-plan.
   Note l'identifiant de chaque agent : toute correction repasse par le même agent.
3. Quand tous les fichiers existent : assemble.sh, hyperframes check, rendu brouillon, planches toutes les 0,25 s.
4. Lis chaque planche toi-même. Pour chaque défaut (image vide, objet coupé, mot en retard, deux héros, attente sans
   mouvement), renvoie le constat précis à l'agent de la séquence. Réassemble, revérifie.
</étapes>
<barre>Chaque image doit pouvoir servir de vignette. Si une seconde est molle, elle est à refaire.</barre>
```

## Prompt 5 — Musique et bruitages

```
Musique libre de droits (CC0) depuis la bibliothèque SoundSafari : une piste « tension » jusqu'au pivot (coupée
net sur le noir, avec une montée qui culmine pile dessus), une piste « élan » dont le drop tombe sur le flash de
lumière. La musique s'efface sous la voix (au moins 8 dB d'écart avant le pivot). Bruitages : un impact par mot qui
claque, un whoosh par coup de fouet, un clic par case cochée ou chiffre qui défile, une notification sur chaque rime.
Fais 2 options complètes que je compare à l'oreille, mix à -16 LUFS.
```

## Prompt 6 — Vérification et livraison

```
Rendu final en haute qualité. Puis, avant de me dire que c'est fini : planches toutes les 0,25 s lues en entier,
durée (image et son), erreurs de décodage, images figées, loudness (-16 LUFS, crête ≤ -1,5 dB). Corrige via les
agents ce qui n'est pas premium et refais le rendu. Livre-moi le MP4 (copie compressée si plus de 30 Mo), la
variante musicale et la liste honnête de ce que les contrôles signalent encore. Commit et push.
```

## Prompt « retour client »

```
Retour du client sur [projet] : « [son message tel quel] ».
Traduis chaque remarque en changements précis (séquence, instant, quoi), dis-moi ceux que tu déconseilles et
pourquoi, puis applique le reste via les agents des séquences concernées, refais le rendu et les contrôles.
```
