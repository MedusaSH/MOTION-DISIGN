# Utiliser Motion Studio dans n'importe quelle session Claude Code

La méthode est emballée en **plugin Claude Code** (`motion-studio`), publié par ce dépôt (il sert aussi de
« marketplace »). Le plugin ajoute le skill `motion-studio` : où que tu sois, il trouve ou installe tout seul l'atelier
(ce dépôt : HyperFrames figé, skills audités, kit d'effets, bruitages, scripts) dans `~/motion-studio`, puis fabrique le
film là-bas et recopie les livrables dans ton dossier courant (`./motion/<projet>/`).

## 1. Claude Code sur ton ordinateur (terminal, VS Code, JetBrains, app desktop)

Une seule fois, dans n'importe quelle session :
```
/plugin marketplace add MedusaSH/MOTION-DISIGN
/plugin install motion-studio@motion-studio
```
(ou dans un terminal : `claude plugin marketplace add MedusaSH/MOTION-DISIGN` puis
`claude plugin install motion-studio@motion-studio`). Le plugin est alors actif dans **toutes** tes sessions, quel que
soit le dossier. Mise à jour : `/plugin marketplace update motion-studio`.

Si le dépôt est privé : connecte d'abord git à GitHub (`gh auth login` puis `gh auth setup-git`).
Prérequis installés automatiquement au premier film : Node 20+ doit exister, ffmpeg est installé si possible
(sinon `brew install ffmpeg` sur Mac).

## 2. Claude Code sur le web (claude.ai/code) sur un AUTRE dépôt

Deux façons :
- **La plus simple** : ajoute le dépôt `MedusaSH/MOTION-DISIGN` comme deuxième dépôt de la session (ou de
  l'environnement) ; le skill est alors chargé et l'atelier déjà cloné.
- **Automatique pour un dépôt** : dans le dépôt du client, crée (ou complète) `.claude/settings.json` :
  ```json
  {
    "extraKnownMarketplaces": {
      "motion-studio": { "source": { "source": "github", "repo": "MedusaSH/MOTION-DISIGN" } }
    },
    "enabledPlugins": { "motion-studio@motion-studio": true }
  }
  ```
  Toute session cloud ouverte sur ce dépôt aura le plugin.

## 3. Directement dans l'atelier

Ouvre une session sur ce dépôt (`MOTION-DISIGN`) : le skill `motion-design-kinetic` y est déjà, rien à installer.

## Ensuite : une phrase suffit

```
Fais un motion design pour https://www.exemple.com : 40 secondes, en 16:9 et en 9:16, bouton « Réserver une démo ».
```
Claude lit le site (textes, preuves chiffrées, palette, polices, logo, captures, vidéo de démo), applique la charte de
la marque, te propose le script, puis enchaîne les étapes avec validation (voix, storyboard, musique) jusqu'aux fichiers
web / réseaux sociaux / WhatsApp vérifiés.

Si le site bloque les robots ou n'est pas joignable depuis la session, Claude bascule sur une lecture par WebFetch et
te demande quelques captures d'écran et le logo.
