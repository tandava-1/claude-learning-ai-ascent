# Working on AI Ascent

Read `CONTEXT.md` before starting, if you have it. Its "Current state" section
is where the project stands; its log is how it got there. Update both as you
work. This repo is public: `CONTEXT.md` stays local and is gitignored, so keep
anything private out of this file, the README and `docs/`.

AI Ascent is a public, forkable template: a 12-module self-paced AI learning
track with a study hub (a claude.ai Artifact), a Socratic tutor skill and a
weekly digest skill. Anyone can fork it and swap in their own curriculum.

## Rules

- Nothing personal goes in. This template was scrubbed from the author's own
  hub; never copy content from a personal hub, notes or product ideas into it
  without scrubbing. Example product ideas are fictional (Exam Coach, Fix-It
  Helper, Clinic Front Desk, Tool Library, Trip Weaver).
- `hub/index.html` is the app; `hub/curriculum.js` is the course content. Keep
  them separate so a fork can replace the content without touching the app.
- The skills keep their placeholders (`{HUB_URL}`, `{CURRICULUM_PATH}`,
  `{TIMEZONE}`). Never fill them with a real hub link or path.
- `skills/ai-tutor/` here is the current version of the tutor skill.
- Licences: code (`hub/index.html`, `skills/`, `starter/`) is MIT; course content
  (`hub/curriculum.js`, `docs/`) is CC BY 4.0. Keep the README's credit line.
- `docs/make-your-own-track.md` and `docs/privacy.md` are linked from the
  README and read by people who fork the repo. Don't move them.
- Commit with the GitHub noreply address already set for this repo, never a
  personal email.
- `starter/hello.py` reads the API key from an environment variable. Never
  commit a key or a `.env` file.
- Preview locally with `python3 -m http.server --directory hub`.
