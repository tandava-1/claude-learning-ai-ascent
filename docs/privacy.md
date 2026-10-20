# Privacy: where your data lives

Your progress is yours. Nothing you do in AI Ascent comes back to this repository or to anyone who forked it before you.

## What lives where

| What | Where it's stored | Who can see it |
|---|---|---|
| The course itself (modules, puzzles, readings) | The page you publish (`index.html` + `curriculum.js`) | Anyone you share the hub link with |
| Checklist ticks, study days, streak | The hub's database, `progress/main` | Only you (see "The access rule" below) |
| Quiz results, tutor session logs, glossary | The hub's database, `sessions` and `glossary` | Only you |
| Notes, highlights, bookmarks | The hub's database | Only you |
| Forecasts and your Brier score | The hub's database, `forecasts` | Only you |
| Weekly digests | The hub's database, `digests` | Only you |
| Your start date and learner brief | The hub's database, `settings/main` | Only you |
| A backup of the above | Your browser's local storage | Only that browser |

When you publish your fork as a claude.ai Artifact, you get a new database that starts empty. It isn't connected to anyone else's hub, including the original author's.

## The access rule

The README publishes the hub with this database rule:

```json
{ "db": { "rules": [ { "path": "", "read": "admin", "write": "admin" } ] } }
```

`admin` means "people who can edit this artifact". A new artifact is private and only you can edit it, so only you can read or write your progress. If you share the link with view-only access, those people see the course but none of your data. Their copy of the page shows "local only" and keeps any ticks they make in their own browser.

If you *want* a study partner to see your progress, change `read` to `"interact"` (anyone who can view) and republish. If you give someone edit access, they can read and change your data.

## The "Ask Claude" buttons

Some pages have "Check my reasoning" and "Go deeper" buttons. They send that section of the course, your answer and your learner brief to Claude, using the account of whoever is viewing. The first use asks for consent. Nothing is sent until you click.

## The tutor and digest skills

The skills run in your own Claude account and read and write your hub's database through your account's permissions. They don't send your data anywhere else. The digest searches the web for news; it doesn't put any of your data into those searches.

## Before you share or fork onwards

The curriculum file contains no personal data. If you edit it, for example by adding examples from your own work or ideas, remember that anything in `curriculum.js` is public once you push it. Keep private ideas in your hub's notes or your dossier folder, not in the curriculum.
