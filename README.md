# Backlink Exchange — Claude Skill

Give one editorial link, earn points, get links back. A vetted backlink exchange
for B2B startups, run as a Claude skill — it picks your partner, shows what
you'll earn, drafts the post, and verifies the link automatically.

You give an editorial link, you earn points weighted by your site's authority and
niche fit. You spend points to receive links. Nothing is a direct swap —
assignments rotate in rings, so link profiles stay natural.

## Install

**Claude Code — as a plugin (recommended).** In Claude Code:

```
/plugin marketplace add maun11/raise-my-dr
```

then `/plugin install backlink-exchange@raise-my-dr` and `/reload-plugins`.

**Anything else:** paste `SKILL.md` into a chat as your first message.

## Commands

```
/backlink-exchange:brief          who am I linking to, what will I earn, write the post
/backlink-exchange:check <url>    verify a published link passes every rule
/backlink-exchange:join           check whether your site clears the gate, then apply
/backlink-exchange:status         points balance and what it can afford
```

`/backlink-exchange` on its own works too, and routes on what you ask for.

## Configure

Open `SKILL.md` and set the values at the top:

```
ROSTER_CSV_URL   = published CSV of the Roster tab (Publish to web → Roster → CSV)
JOIN_FORM_URL    = Google Form for new members
SUBMIT_FORM_URL  = Google Form for manual URL submission
JOIN_WEBHOOK_URL = optional; enables applying from inside Claude
```

`ROSTER_CSV_URL` must be a **published** CSV, not a `/edit` link. An `/edit` link
exposes the entire workbook, including private member contact details.

## Use

```
/backlink brief          who am I linking to, what will I earn, write the post
/backlink check <url>    verify a published link passes every rule
/backlink join           check whether your site clears the gate, then apply
/backlink status         points balance and what it can afford
```

## Verify a link without the skill

```bash
python scripts/check_link.py https://yourblog.com/post partner-domain.com
```

Standard library only. Checks the link exists, is dofollow, sits in body content,
is the only link to that partner, and that the host post clears 600 words and 15
outbound links.

## Rules in one screen

- One exchange link per post. Never two.
- One link to any given domain per 180 days.
- No direct swaps — A→B, B→C, C→A, with a 90-day cooldown on repeat pairs.
- Body paragraphs only. No footers, sidebars, or resource pages.
- Plain dofollow. 600+ word host post, under 15 outbound links.
- Links stay live 90 days. Re-checked at 30, 60 and 90.
- Everyone starts on Probation: give two links that survive 30 days, then you can
  receive.

Authority is verified by the operator, never taken from the signup form.

## License

MIT. Some structural patterns adapted from the MIT-licensed
[claude-seo](https://github.com/AgriciDaniel/claude-seo).
