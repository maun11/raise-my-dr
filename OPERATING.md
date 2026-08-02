# Operating your own exchange

Members don't need this file. It's for whoever runs the roster.

## Configure the skill

Open `SKILL.md` and set the four values at the top:

| Value | What it is |
|---|---|
| `ROSTER_CSV_URL` | Published CSV of the Roster tab. The skill reads this and nothing else. |
| `JOIN_FORM_URL` | Google Form for new members — the fallback path. |
| `SUBMIT_FORM_URL` | Google Form for manual URL submission, for sites with no sitemap. |
| `JOIN_WEBHOOK_URL` | Intake endpoint that lets people apply from inside Claude. Optional, but without it the form becomes mandatory. |

**`ROSTER_CSV_URL` must be a published CSV** — File → Share → Publish to web →
Roster → CSV. It produces a `.../pub?gid=...&output=csv` URL.

> ⚠️ Never use an `/edit` link here, and never give one to a member. An `/edit`
> link opens the entire workbook — including the private tab holding member
> emails and phone numbers — and grants edit rights on your source of truth.

## Why the skill can't cheat

The skill holds **no credentials**. It reads the published Roster CSV and, if
`JOIN_WEBHOOK_URL` is set, can POST a join application. That's the entire
surface. It cannot award points, change a status, or edit a balance — not
because it's told not to, but because it has no way to.

Points come only from a link the verifier independently found and checked. That
is what makes the balances mean anything, so keep it true.

## The one thing that must stay true

A join application creates a **pending row awaiting human approval**. It does not
create a member. If you ever wire up auto-approval, keep the vetting gate in
front of it — the whole anti-spam design rests on a real person seeing the
numbers before a domain enters the roster.
