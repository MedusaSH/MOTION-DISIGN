---
version: 2
name: "Synapze: launch frame"
description: >
  Video-first frame spec for the Synapze launch motion design (« La deuxième journée », 43.8 s), built on
  ../patterns/PATTERNS.md. Direction B « Le fil de la soirée » with two borrowings from C: the evening of the broker is
  one horizontal time line the camera travels along; the hours he loses are a hatched segment; after the pivot the line
  turns into the waveform of his voice note and runs into the real Synapze screen.
  Two worlds: the PROBLEM lives on the night-blue stage of the site, the SOLUTION on the cream ground of the site; the
  end card returns to the night-blue stage. One accent only, Synapze orange, kept for what matters: the line itself, the
  key-word box of each subtitle and 4 peak strokes. The sentence of the voice is a subtitle at the bottom center that
  arrives word by word.
unit: 1920×1080
principle: readable without sound · one thing to look at at a time · one accent, one highlight mechanism · the voice cues every reveal

colors:
  canvas: "#0E1624"           # dark world (problem + end card), the site's night blue
  canvas-2: "#0A0F1A"         # deepest (pivot black, end card bottom)
  paper: "#F1EBDE"            # light world (solution), the site's cream
  paper-2: "#E8E0D0"          # secondary light surface
  card-light: "#FBF7EE"       # cards and hanging labels on both worlds
  ink: "#F1EBDE"              # text on dark
  ink-soft: "#C9C2B2"
  ink-mute: "#9AA3B4"         # graduations, micro labels on dark
  ink-dark: "#0E1624"         # text on light
  ink-dark-soft: "#5B6578"    # negative role too: hatched lost time, grey ticks, unanswered notification
  hairline-light: "#D8CFBD"
  accent: "#F24E1E"           # Synapze orange: the line, the box, the strokes, the button
  accent-light: "#F57A50"
  accent-deep: "#C93C12"
  accent-glow: "#FFB79C"

fonts:
  DM Serif Display: { files: ["assets/fonts/DMSerifDisplay-400.woff2 (400)", "assets/fonts/DMSerifDisplay-400i.woff2 (400 italic)"] }
  DM Sans: { files: ["assets/fonts/DMSans-400.woff2 (400)", "assets/fonts/DMSans-500.woff2 (500)", "assets/fonts/DMSans-600.woff2 (600)", "assets/fonts/DMSans-700.woff2 (700)"] }
  DM Mono: { files: ["assets/fonts/DMMono-400.woff2 (400)", "assets/fonts/DMMono-500.woff2 (500)"] }
  Caveat: { files: ["assets/fonts/Caveat-500.woff2 (500)"], note: "only the broker's handwritten notes" }

typography:
  subtitle:   { fontFamily: "DM Sans", px: 60, weight: 600, lineHeight: 72, tracking: "-0.01em", note: "the sentence of the voice at the BOTTOM CENTER (top at y 900, band y 890 to 980 carries nothing else), 45 characters at most per chunk, word by word on its timestamps; ink on dark, ink-dark on light, light shadow; a 300 px gradient scrim of the ground color keeps objects out of the band" }
  type:       { fontFamily: "DM Serif Display", px: 84, weight: 400, lineHeight: 1.12, note: "ONLY the pivot « Et si vous arrêtiez d'écrire ? » and the end promise; centered, never bigger than 84 px" }
  clock:      { fontFamily: "DM Sans", px: 150, weight: 600, tracking: "-0.03em", tabularNums: true, note: "the hour above the running point (19:00, 22:47, 19:05); always rolls digit by digit" }
  graduation: { fontFamily: "DM Mono", px: 22, weight: 500, tracking: "0.05em", note: "hours and days under the line, ink-mute" }
  ui:         { fontFamily: "DM Sans", px: 22, weight: 500 }
  title:      { fontFamily: "DM Serif Display", px: 44 }
  micro:      { fontFamily: "DM Mono", px: 16, weight: 500, tracking: "0.2em", upper: true }
  handwriting: { fontFamily: "Caveat", px: 50, weight: 500 }
  wordmark:   { fontFamily: "DM Serif Display", px: 140, note: "« • Synapze • » in ink with the two dots in accent, as on the site" }
  cta:        { fontFamily: "DM Sans", px: 38, weight: 600 }

components:
  ground-dark:
    background: "solid canvas + a dot grid of ink at 7 % (1.6 px dots, 48 px pitch) that makes every drift readable + one warm radial halo at 15-20 % behind the focal object. Full-duration class=\"clip\" layer."
  ground-light:
    background: "solid paper + dot grid of ink-dark at 9 %, same pitch; no halo. Full-duration class=\"clip\" layer."
  time-line (THE world):
    look: "a 4 px accent line, round caps, crossing the world horizontally at world y 540; graduations every hour (2 px × 28 px ticks, graduation font under them). In the problem the line past 19:00 turns ink-dark-soft and carries the hatched segment."
    world: "#world 14400 × 2160 for act 1, 1 hour = 1200 px: 18:00 at x 1200, 19:00 at x 2400, 20:00 at x 3600, 21:00 at x 4800, 22:00 at x 6000, 22:47 at x 6936; then the days: SAM. 21:14 at x 8400, DIM. at x 9600, LUN. 08:30 at x 10800."
  running-point (signature 2):
    look: "a 30 px accent disc with a 12 px accent ring at 20 %, ON the line; above it the clock. It is the time passing; at the pivot it becomes the caret; in the solution it becomes the first bar of the waveform; at the end it lands on 19:05."
  hatched-segment:
    look: "40 px tall band centered on the line, repeating-linear-gradient(-45deg, ink-dark-soft 55 % 0 10px, transparent 10px 20px), hairlines top and bottom; the micro label « SAISIE » repeated under it."
    motion: "drawn by the running point, scaleX from its left edge, linear, at the speed of the clock."
  hanging-label (signature 1):
    look: "an object hangs from the line by a 2 px ink-mute thread (agenda page, empty prospect card, notebook, advice form, phone, WhatsApp phone). card-light, radius 8, shadow 0 30px 60px rgba(0,0,0,.35)."
    motion: "drops from above ×1.15 and blurred (8 px), settles in 0.12 s expo.out, swings 2° once (0.4 s sine.out), then drifts 1° (living hold)."
  waveform:
    look: "accent bars 7 px wide, 6 px gap, radius 4, heights from the real voice (scripts/waveform.py), centered on the line."
  word-by-word:
    rule: "Each word appears ON its timestamp: fromTo {opacity:0, y:12, filter:blur(6px)} → {opacity:1, y:0, blur(0)} in 0.08 s expo.out, immediateRender:false. Before a seam the subtitle leaves: opacity 1 → 0, blur 0 → 6 px in 0.14 s."
  key-word-box (THE highlight mechanism, one per sentence):
    look: "accent rectangle, radius 6px, padding 0 14px, the word in white inside. Never a black box."
    motion: "opens from the left (scaleX 0 → 1, origin left, 0.12 s power3.out) 0 to 2 frames before the word."
    rule: "ONE box per sentence, on the word named [boîte : …]. No other colored text anywhere."
  peak-stroke:
    look: "tapered accent brush stroke (round attack, thin exit, slight rise) under THE key word."
    motion: "draws from the left in 0.25 s power2.out while the word is spoken."
    rule: "only the 4 peaks [trait : saisie], [trait : lundi], [trait : parlez], [trait : imbattable]."
  caret:
    description: "6 px × 84 px accent bar; blinks as finite on/off steps of 0.5 s (never repeat:-1)."
  product-mock:
    description: "The REAL Synapze screen « Une note vocale suffit. » from assets/ui/voice-note-fr.mp4 (1440 × 810, 11 s): navy sidebar (Tableau de bord, Clients, Appels, Calendrier, Commissions, Contrats, Pilotage IA, Comparateur PDF, Emails), « CRM · PROSPECT », card « Louis Lebrun · LEAD · Santé Individuel en souscription », button « Enregistrement… », transcription card (waveform, « 0:18 », « TRANSCRIPTION IA », quote), IDENTITÉ block filled with « IA » chips and « REMPLIE AUTOMATIQUEMENT », steps bar « Découverte … Converti ». Placed as the video itself (retimed) or its frames, inside a 1300 × 820 dark laptop frame, never redrawn."
  generic-crm:
    description: "Before the pivot only: a brandless prospect card « Nouveau prospect » with fields Nom, Date de naissance, Ville, Besoin, empty grey fields; the sidebar label reads « MON CRM », never Synapze."
  advice-form:
    description: "« Fiche de conseil · Santé Individuel », white document, five lines with check boxes (Besoins exprimés, Situation familiale, Budget, Garanties proposées, Justification du conseil). Problem: ticked by a mouse arrow. Solution: ticks itself, each tick with the « IA » chip of the CRM, a completeness bar, the stamp « PISTE D'AUDIT · HORODATÉE » in DM Mono accent."
  iphone-lock:
    description: "current iPhone, black bezel 14 px, radius 62; lock screen gradient #1B2840 → #0B111D, date DM Sans 22, time 110 px; WhatsApp notification card « Camille R. · Bonjour, je cherche une mutuelle pour ma famille. Vous pouvez me faire un devis ? » (unanswered: turns ink-dark-soft)."
  whatsapp-ios:
    description: "copy of the WhatsApp iOS interface, no logo: status bar, header (back chevron and icons #1DAB61, avatar « CR », « Camille R. », « en ligne »), beige doodle ground #EFEAE2, white incoming bubbles, #D9FDD3 outgoing bubbles with time and blue ticks #53BDEB, date pills, typing dots, input bar. Assistant replies identify as AI in the first message (AI Act)."
  cursor:
    description: "White macOS arrow with dark outline + drop shadow; arrives in ONE curved move (0.4 to 0.5 s power3.out), clicks directly: press (scale .85, 0.06 s) + accent ripple. Never a hesitation."
  light-point:
    description: "white-hot point (radial #fff → accent-glow → transparent) on the caret at (960, 540) where the orchestrator's light flash starts."
  end-card:
    description: "night-blue stage, « • Synapze • » assembled letter by letter, the promise on two lines (« Le courtier parle. » ink, « L'IA fait tout le reste. » accent, as the site hero), ONE button « Demander une démo » (accent fill, white DM Sans 600), mono URL « synapze.eu », a cursor clicks it directly, a thin waveform breathes under it (2 to 3 s of living hold), then iris."

negative:
  - "No second highlight mechanism: the key-word box is the ONLY emphasis in a subtitle, the peak stroke marks 4 peaks."
  - "No big sentence: subtitle 60 px, typographic moment 84 px at most; nothing but the subtitle in the band y 890 to 980."
  - "One thing to look at at a time; the camera follows the line, it never goes back along it."
  - "No decor without meaning: every graduation is a real hour of the story, every hanging object is a sentence."
  - "No hue other than orange, navy, cream and grey, except inside the real Synapze screen and the WhatsApp copy."
  - "Synapze never appears before 22.31 s (the generic CRM says « MON CRM »)."
  - "No Inter, Space Grotesk, Geist, system-ui. No emoji."
  - "No repeat:-1, no breathing loops on everything; living holds are named in the storyboard."
  - "Never tween letterSpacing."
---

# Synapze: frame spec

The film has two worlds. **The problem** plays on the night-blue stage of the site: the evening of the broker is a
time line; after 19:00 the running point drags a hatched « saisie » segment to 22:47 while forms hang from the line,
then the line jumps to the weekend, where an unanswered WhatsApp waits until Monday. A single **pivot** (« Et si vous
arrêtiez d'écrire ? » on black, the caret that erases it) freezes everything, then light floods from the caret and we
land on **the solution**, on the cream ground: the line has become the waveform of a voice note, it runs into the real
Synapze screen, the advice form ticks itself, WhatsApp answers; seen from afar the evening has no hatched segment left
and the point stops at 19:05. The line contracts into the underline of the logo and the end card plays on the night
blue.

Everything the viewer reads is DM Sans: the sentence of the voice as a subtitle at the bottom center, word by word,
with exactly one key word per sentence in a small orange box. A tapered orange stroke marks the 4 peaks. Hours, days
and labels are DM Mono; the pivot, the logo and the promise are DM Serif Display, as on the site.
