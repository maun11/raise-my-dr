# Raise My DR

**Give one editorial link. Earn points. Get links back.**

A vetted backlink exchange for B2B startups — run as a Claude skill. It picks
your partner, tells you what you'll earn before you write, drafts the post, and
verifies the link automatically. You never fill in a spreadsheet.

---

## How it works in one picture

```
   You publish a post          We check it              Points appear
   with one link inside   →    automatically       →    in your balance
                               (every 15 min)

        ↑                                                     │
        │                                                     ↓
   We tell you who                                    You spend points
   to link to, and              ←   ←   ←   ←          to receive links
   help you write it                                  to your own site
```

Nobody swaps links directly. Assignments rotate in a ring — you link to Anna,
Anna links to Ben, Ben links back to you — so your link profile stays natural
and nothing looks traded.

---

## What you actually do

| Step | What happens | Effort |
|---|---|---|
| **1. Join** | Fill one short form. We check your site automatically. | 2 min |
| **2. Get your assignment** | Run `/backlink-exchange:brief`. It names your partner and shows the points. | 30 sec |
| **3. Write the post** | Claude interviews you for your angle, then drafts it. You edit and publish. | 20–40 min |
| **4. Get paid** | Nothing. We find the post and add your points within 15 minutes. | 0 min |

**You never submit a URL. You never update a sheet. You just publish.**

---

## What you earn

Points depend on **your** site's authority — stronger sites earn more per link,
because their links are worth more.

| Your authority | Points per link | Band |
|---:|---:|---|
| 0–5 | 1 | Seed |
| 6–15 | 2 | Starter |
| 16–25 | 4 | Emerging |
| 26–35 | 6 | Growing |
| 36–45 | 9 | Established |
| 46–55 | 13 | Solid |
| 56–65 | 18 | Strong |
| 66–75 | 25 | Authority |
| 76–85 | 40 | High Authority |
| 86–100 | 60 | Elite |

Then a relevance multiplier: **same niche ×2**, adjacent **×1.5**, unrelated **×1**.

> A DR 34 site linking inside its own niche earns **6 × 2 = 12 points** per post.

The curve is steep on purpose. Authority scores are logarithmic — a DR 88 link
really is worth about ten DR 30 links, so paying them the same would just make
the strong sites leave.

**Your authority is measured, never claimed.** Whatever you type on the form is
ignored; we check it ourselves.

---

## The rules

The whole system rests on one rule:

> ### One exchange link per post. Never two.

That's what keeps posts reading like posts instead of link farms. Everything
else supports it:

- ✅ Inside a **body paragraph** of a real article
- ✅ **Plain dofollow** — no `nofollow`, `sponsored`, or `ugc`
- ✅ Post is **600+ words** with **under 15** outbound links total
- ✅ Link stays live **90 days** (we re-check at 30, 60 and 90)
- ❌ Never in a footer, sidebar, nav, or "resources" page
- ❌ Never two links to the same partner in one post
- ❌ Never link to the same domain twice within 180 days

**No monthly cap.** Give as often as you publish.

**Everyone starts on Probation** — you can give links and earn points
immediately, but you can't spend them until two of your links have been verified
and stayed live for 30 days. That's the anti-spam gate: a junk site has to do
real work for a month before it can extract anything.

---

## Install

**In Claude Code:**

```
/plugin marketplace add maun11/raise-my-dr
```

Then `/plugin install backlink-exchange@raise-my-dr` and `/reload-plugins`.

**Anywhere else:** paste the contents of `SKILL.md` into a chat as your first
message.

### Commands

| Command | What it does |
|---|---|
| `/backlink-exchange:brief` | Who am I linking to, what will I earn, write the post |
| `/backlink-exchange:check <url>` | Check a published post against every rule |
| `/backlink-exchange:join` | See whether your site would pass, then apply |
| `/backlink-exchange:status` | Your points, links given and received |

`/backlink-exchange` on its own works too — just say what you want.

---

## Check a link without installing anything

```bash
python3 scripts/check_link.py https://yourblog.com/post partner-domain.com
```

Standard library only — no `pip install`. It tells you exactly what passed and
what didn't:

```
  PASS  https://yourblog.com/post
    PASS  link_present
    PASS  dofollow
    PASS  in_body_content
    PASS  single_link_to_partner
    PASS  word_count_600_plus
    PASS  outbound_under_15
    PASS  anchor_not_empty
```

---

## Why it's built this way

**Members never write to the scoreboard.** The skill reads the roster and
nothing else — it holds no credentials, so it physically cannot award you points
or change your status. Points come only from a link we independently found and
checked. That's what makes the balances mean anything.

**We find your post; you don't report it.** Any design where you have to submit
a URL adds a step people forget, and then the whole thing dies. We read your
sitemap instead.

**Partners are assigned, not chosen.** If everyone picked freely, everyone would
pick the highest-authority site and the bottom half of the group would never get
a link.

**Nothing is auto-sent.** No auto-DMs, no auto-posting, no engagement bots. The
moment this sends anything on your behalf it becomes spam tooling.

---

## Configure (operators only)

Members can skip this. Open `SKILL.md` and set:

```
ROSTER_CSV_URL   = published CSV of the Roster tab
JOIN_FORM_URL    = Google Form for new members
SUBMIT_FORM_URL  = Google Form for manual URL submission
JOIN_WEBHOOK_URL = optional; lets people apply from inside Claude
```

`ROSTER_CSV_URL` must be a **published** CSV — File → Share → Publish to web →
Roster → CSV. Never use an `/edit` link: that exposes the whole workbook,
including private member contact details.

---

## License

MIT. Some structural patterns adapted from the MIT-licensed
[claude-seo](https://github.com/AgriciDaniel/claude-seo).
