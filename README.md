# AI Ascent

**A self-paced, 12-module track for going from AI power user to AI product builder and strategist, with a study hub, a Socratic tutor and a weekly news digest, all running on Claude.**

About 13.5 hours a week for 10 weeks (1.5 h on weekdays, 3 h at weekends). No coding background, GPU or advanced maths needed.

Fork it to follow the track yourself, or swap in your own `curriculum.js` and build a track on any topic ([how](docs/make-your-own-track.md)).

## What's in a module

Each module has the same rhythm:

- **A reading page** that explains one big idea from first principles, through four questions: how does it work, what can it do, when did it arrive, and why did it win.
- **Frameworks**: three or four reusable thinking tools (the Spec Stack, the Permission Ladder, the Eval Pyramid, the Unit-Economics Ladder…).
- **A tutor exercise**: a scenario from an unfamiliar field, where the tutor questions you instead of lecturing.
- **A prototype** you design and Claude Code builds. You write the spec, the labels and the success measure, then read the results yourself.
- **Puzzles**, **two forecasts** to log and score later, and **field notes and horizon** pages on who is applying the idea and where it's heading.

Across the track you build one **dossier** on one product idea, a chapter per module, assembled in the capstone. Bring your own idea, or start from one of three: **Exam Coach**, **Fix-It Helper** or **Clinic Front Desk**.

| # | Module |
|---|---|
| 1 | How a model learns: data, the score, and the proxy trap |
| 2 | Inside a language model: tokens, context and attention |
| 3 | Where capability comes from: scale, data and compute |
| 4 | From model to assistant: post-training and alignment |
| 5 | Reasoning: when thinking pays |
| 6 | Images, voice and video: what's possible |
| 7 | Agents, tools and retrieval |
| 8 | Evals: how you know an AI feature works |
| 9 | The stack and the economics |
| 10 | Trust: safety, failure and regulation |
| 11 | Strategy: adoption, labor and where value accrues |
| 12 | Capstone: a product dossier or a strategy thesis |

Each module also keeps the original deep material (the maths and the from-scratch builds) under "Under the hood", for when you want to go further.

## What's in the repo

```
hub/index.html            the study hub app (tabs, checklists, streak, notes, forecasts, digests)
hub/curriculum.js         the course content; replace it to make your own track
skills/ai-tutor/          the /ai-tutor skill: Socratic sessions that read and write your hub
skills/weekly-digest/     a weekly task that posts AI news through your current module's lens
starter/                  hello.py, the first setup step: call Claude from a script
docs/                     make-your-own-track.md, privacy.md
```

## Set it up (about 20 minutes)

You need a Claude account and [Claude Code](https://claude.com/claude-code).

### 1. Get your own copy

Press **Use this template**, or **Fork**, on GitHub, then clone your copy and open Claude Code in the folder.

### 2. Publish your hub

The hub is a claude.ai Artifact with its own private database. In Claude Code, inside your copy, ask:

```text
Publish hub/index.html as a new private Artifact titled "AI Ascent", with hub/curriculum.js as a
supporting file published at curriculum.js, and these capabilities:
{"db": {"rules": [{"path": "", "read": "admin", "write": "admin"}]}, "sample": {}}
Then give me the link.
```

Save the link: this is your **hub URL**. It starts empty, and only you can see your progress ([privacy](docs/privacy.md)). Open it, go to **Guide**, set your start date and edit your learner brief (how you like to be taught).

To try the page without publishing, run `python3 -m http.server --directory hub` and open http://localhost:8000. Progress is then kept in that browser only, and the tutor can't see it.

### 3. Install the tutor

Copy `skills/ai-tutor/` into `~/.claude/skills/ai-tutor/` (for Claude Code), or zip the folder and upload it as a skill in claude.ai. Then replace the three placeholders in `SKILL.md`:

- `{HUB_URL}`: your hub link from step 2
- `{CURRICULUM_PATH}`: the full path to `hub/curriculum.js` in your copy (or delete that line)
- `{TIMEZONE}`: for example `Europe/London`

Now `/ai-tutor` picks up where you are. `/ai-tutor quiz`, `exercise`, `build`, `explain <idea>`, `review`, `forecast` and `status` run the other modes.

### 4. Optional: the weekly digest

Put your hub URL into `skills/weekly-digest/SKILL.md`, then ask Claude to run it as a scheduled task every Monday morning. Each digest appears on your hub's **Digests** tab.

### 5. Run the starter

Follow **Guide → Setup** on your hub: get an API key, set a spending cap (about $10 covers the whole track), store the key as an environment variable, and run `starter/hello.py`. Never paste the key into a file you commit.

## Make your own track

Keep the app and write a new `hub/curriculum.js`: biology, design, a language, anything. [docs/make-your-own-track.md](docs/make-your-own-track.md) explains the format and gives a prompt that has Claude draft it with you, one module at a time.

## Licence

- **Code** (`hub/index.html`, `skills/`, `starter/`): [MIT](LICENSE).
- **Course content** (`hub/curriculum.js`, `docs/`): [CC BY 4.0](LICENSE-CONTENT).

You can reuse and adapt both, including commercially, as long as you credit the original:

> Based on AI Ascent by Shivank Shridhar (https://github.com/tandava-1/claude-learning-ai-ascent), CC BY 4.0.

Linked readings and videos belong to their authors.
