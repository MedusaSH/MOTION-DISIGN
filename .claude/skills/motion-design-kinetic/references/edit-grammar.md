# Edit grammar: what made the kinetic film « bluffing »

The client's verdict on the calm version (v1, a travelling along a time line): « pas assez moderne, pas assez de
montage, linéaire, polices bof ». The kinetic version (`synapze-v2/`, same voice, same 11 boundaries) fixed it with
the rules below. Write them INTO the storyboard (numbers, times), never as adjectives: a worker only does what a Scene
line dates.

## 1. The voice is the clock, the picture cuts on its words

- Run `mots.py` (word timings), then list the COUPES: the first word of every idea, and every word you want to hit.
  Target: problem acts ≈ 1 cut / 1 s (9 per 10 s), silent gag 1 cut / 0.25 s, solution 1 cut / 1.2 s, end card 2-3.
- Every silence over 0.4 s becomes its own action (a time-lapse gag, a caret erasing, a click), never a hold.
- Most seams are HARD cuts on a word, written « coupe franche voulue » in handoff_in with the first image described.
  They are sold by one of: a 2-frame flash, a whip (blur pan 0.16 s out / 0.22 s in), a match on an object
  (same shape, same place, other role), a cut to black.

## 2. Three text registers, never two saying the same words

| register | font | job |
|---|---|---|
| kinetic | Geist 900, 260-420 px, tracking -0.045em | 1-2 words that ARE the image; slam or rise |
| emotion | Instrument Serif italic 180-320 px | ONE word per beat that carries the feeling (« le courtier. », « lundi », « parlez ») |
| caption | Geist 600 46 px, band y 890-980 | the full sentence word by word on its cue, ONE keyword in the accent box |

Labels and micro-copy in Geist Mono uppercase .14em. This trio (grotesk + serif italic + mono) is what read as
« moderne » after DM Sans was judged « bof ».

## 3. The effect vocabulary (all in reference/fx.html, all seek-safe)

| effect | when | numbers |
|---|---|---|
| SLAM + chroma + shake | the hero word / number of a shot, max 1 per 1.5 s | ×1.6 blur 18 → ×1 in 0.12 s, red/cyan split ±14 px 0.28 s, shake 14 px 0.32 s, + impact SFX |
| ROLL | every clock / counter | discrete digit steps (18:57 → 18:59 → 19:00), never a fade |
| PUNCH | on the word that names the thing | ×1.12-1.35 in 0.18 s, then 4 %/s drift |
| WHIP | leaving a shot sideways | out 0.16 s power3.in blur 28 / in 0.22 s expo.out |
| FLASH | on a hard cut, on the pivot light | 0.85 → 0 in 0.1 s, white on night, ember on the light |
| 3D glass card | every interface | perspective 1800, rotateY -18° → -10°, rotateX 8°, arrives ×1.15 blurred and settles |
| ghost copies / trails | an object that leaves | 3 copies at 30 % offset 0.03 s, blur 24 |
| key box | the caption keyword | accent box opens left → right in 0.14 s on the word |
| shimmer / hot gradient | the payoff word | gradient sweep 1.2 s |
| grain + vignette + glow | always | grain .09 overlay, ember disc behind the hero drifting |

## 4. Acts and worlds (the contrast IS the story)

1. Hook + problem on NIGHT (`.fx-night`, ember glow): short, physical, numbers that roll, a generic tool (« MON CRM »).
2. Pivot on BLACK: silence or near-silence, one sentence in serif italic, a caret / object that becomes a bar of light.
3. Solution on PAPER with accent light (`.fx-paper`): the REAL product UI floating in 3D, punch-ins on what fills
   itself, ticks cascading, a stamp, a split screen (day / night), the payoff word in hot gradient.
4. End card on NIGHT: logo, promise, button, click, hold ≥ 2 s.

No brand before it is spoken. Everything colored belongs to the accent family.

## 5. Signatures and rhymes (what makes it feel authored)

Write a SIGNATURES block in the storyboard header: 2 recurring mechanisms with every time they fire (e.g. « le slam »
at 0.03, 0.67, 9.65, 15.20…; « le caret » at 4.95, 6.00, 11.00, 19.59, 21.70) and 3 rhymes between problem and
solution (the clock 19:00 → 22:47 → 19:05; the notification on Saturday 21:14 → the answer at 21:14; the box ticked
by hand → ticked by itself). Rhymes are what the client remembers.

## 6. Storyboard block format (per frame)

```
## Frame N: <title> · <start> → <end>
- scene / duration / transition_in: cut / src / voiceover / type / blueprint / focal / rules / world
- handoff_in: first image, pixel facts   - handoff_out: last image, pixel facts
Word cues: Mot@0.03 mot@0.67 ...        (frame-local seconds from voix-montage-mots.json)
Scene k (a à b s) : Pk, <name>
  TEXTE ÉCRAN : exact copy, register, size, where the caption box goes
  ÉTAPES : dated actions every 0.1-0.4 s
  PISTE CAMÉRA : drift + dated punch / whip
  SON : dated SFX (they feed sfx-events.json)
  IMAGE CLÉ : t : the one image to check
```

Header blocks: Video direction, MONDE, SIGNATURES, PARTITION CAMÉRA, VOIX (silences), COUPES, RYTHME, SON.
Full worked example: `synapze-v2/STORYBOARD.md`.
