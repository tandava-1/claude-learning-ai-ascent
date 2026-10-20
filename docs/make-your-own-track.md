# Make your own track

The hub has two parts:

- **`hub/index.html`** is the app: tabs, checklists, streak, notes, forecasts, digests and database sync. You shouldn't need to touch it.
- **`hub/curriculum.js`** is the course: every word you see on the page. Replace it to build a track on anything (biology, product design, music theory, a new language).

The tutor and digest skills read `curriculum.js` from your published hub, so they follow your new track without being rewritten.

## The shape of `curriculum.js`

It defines plain JavaScript constants. The app reads these:

| Constant | What it is | Required? |
|---|---|---|
| `PLAN` | The track: name, schedule, rituals, setup steps, books, and the optional deep material | Yes |
| `TRACK` | The modules, in order. This is what the Curriculum tab shows | Yes |
| `EXTRA` | Worked examples merged into the deep material, keyed by module id | No |
| `DG_X`, `DG_Y` | Diagrams (SVG strings, or small functions that build interactive ones) | No |
| `DIAGRAM_MAP` | Which diagrams appear on which module, e.g. `{ m1: ['specStack'] }` | No |

Text fields use a small Markdown subset: paragraphs, `###` headings, `-` bullets, `1.` numbered lists, `**bold**`, `*italic*` and `[links](https://…)`.

### `PLAN`

```js
const PLAN = {
  name: "Biology Ascent",                       // page title and masthead
  subtitle: "From curious to fluent · 1 h a day",
  start: "2027-01-04",                          // default start date (each learner can change theirs in the Guide)
  streams: { knowledge: {…}, relevance: {…}, excitement: {…} },   // the three lenses on the Guide tab
  weekTemplate: [ { day: "Mon", unit: "Reading", hours: 1, note: "…" }, … ],  // drives the schedule
  rituals: [ { name: "One unit a day", why: "…" }, … ],
  setup: [ "Step 1 …", "Step 2 …" ],
  after90: [ "What to do once the track ends …" ],
  books: [ { order: 1, title: "…", by: "…", when: "…", why: "…" } ],
  learnerBrief: "Default instructions for how to teach. Each learner edits their own.",
  mathPrimer: [],                               // optional
  modules: [],                                  // optional deep material, referenced by TRACK[].deepFrom
  checklist: ["Reading done", "Exercise done", "Project shipped", "Forecasts logged", "Digest read", "Quiz passed"],  // optional
  capstoneChecklist: ["Brief written", "Shipped", "Demo recorded", "Forecasts scored", "Retrospective written"]       // optional
};
```

The schedule comes from `weekTemplate` hours and each module's `hours`. A module ends when its hours are spent, not on a fixed day.

### A module in `TRACK`

```js
{
  "n": 1, "id": "m1", "alt": "1859",            // number, stable id, and the year shown on the rail
  "title": "How evolution works",
  "tagline": "One line that sticks.",
  "purpose": "Why this module matters and what you'll be able to do after it.",
  "hours": { "reading": 2, "puzzles": 1, "exercise": 2, "prototype": 3.5, "review": 1.5 },
  "concepts": ["variation", "selection", "inheritance"],
  "plain": "The whole module in plain words, three sentences.",
  "words": [ { "term": "fitness", "def": "how many offspring survive, not how strong you are" } ],
  "frame": "### The whole idea\n\nThe reading page, in Markdown…",
  "fourq": { "how": "…", "what": "…", "when": "…", "why": "…" },
  "frameworks": [ { "name": "The Selection Test", "core": "one line", "use": "when to reach for it", "body": "…" } ],
  "exercise": { "title": "…", "time": "about 2 h with the tutor", "intro": "…",
                "scenarios": [ { "domain": "Medicine", "prompt": "…" } ], "deliverable": "…" },
  "prototype": { "title": "…", "time": "…", "goal": "…", "steps": ["…"], "deliverable": "…",
                 "cost": "…", "rule": "…", "stretch": "…" },
  "readings": [ { "kind": "video", "title": "…", "by": "…", "url": "https://…", "time": "20 min", "note": "…" } ],
  "puzzles": [ { "q": "…", "hint": "…", "a": "…" } ],
  "predictions": [ { "q": "A yes/no question about the world", "by": "2027-06-30", "kind": "world", "source": "how it resolves" } ],
  "field": { "teardown": { "name": "…", "body": "…", "url": "…" }, "applied": [ { "t": "…", "url": "…" } ],
             "people": [ { "n": "…", "r": "…" } ], "impact": "…" },
  "horizon": { "frontier": "…", "who": [ { "n": "…", "r": "…" } ], "world": "…", "ideate": "…" },
  "deepFrom": []                                // ids from PLAN.modules to show under "Under the hood"
}
```

Mark the last module with `"capstone": true` to give it the capstone checklist.

The easiest way to learn the format is to open the AI Ascent `curriculum.js` and read module 1 next to the hub page.

## Have Claude write it for you

Open Claude Code in your fork and paste a prompt like this (edit the first paragraph):

```text
I want to turn this repo into a learning track on <TOPIC> for <WHO: e.g. a curious adult with no
biology background>, at about <N> hours a week for <N> weeks, ending in <A CAPSTONE: e.g. a
one-page explainer for a friend, a small project>.

Read docs/make-your-own-track.md and hub/curriculum.js. Then:
1. Propose a module list (title, one-line purpose, the 3–4 frameworks each teaches). Wait for my OK.
2. Write a new hub/curriculum.js in exactly the same format, one module at a time, pausing after
   each so I can review. Keep the structure: reading page, four questions, frameworks, a tutor
   exercise with scenarios from several fields, a small hands-on project, puzzles with answers,
   two dated forecasts, and real readings with working URLs. Never invent a reading, a quote or
   a statistic; if you can't verify one, leave it out.
3. Keep the AI Ascent app (hub/index.html) unchanged. Check the page renders after each module.
```

Then update the README's title and description, and change the skill names if you like (for example `bio-tutor`).

## Credit

The course text is CC BY 4.0, so if your track reuses or adapts AI Ascent content, keep a credit line in your README, for example "Based on AI Ascent by Shivank Shridhar, CC BY 4.0". If you only reuse the app and write all-new content, the MIT licence asks you to keep `LICENSE` in your copy.
