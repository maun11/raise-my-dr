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

## Install (30 seconds)

Works in **Claude Cowork** and **Claude Code**. Open either one, paste this, and
send it:

> Install the skill at https://github.com/maun11/raise-my-dr

Claude does the rest. That's it — no terminal, no setup, no config file.

<details>
<summary>If you'd rather type the commands yourself</summary>

```
/plugin marketplace add maun11/raise-my-dr
```

then `/plugin install backlink-exchange@raise-my-dr` and `/reload-plugins`.

Anywhere else (claude.ai, ChatGPT, whatever you use): paste the contents of
`SKILL.md` into a chat as your first message.

</details>

### What you can say

You can use the commands below, or just talk to it — "who am I linking to this
week?" works as well as `/backlink-exchange:brief`.

| Command | What it does |
|---|---|
| `/backlink-exchange:brief` | Who am I linking to, what will I earn, write the post |
| `/backlink-exchange:check <url>` | Check a published post against every rule |
| `/backlink-exchange:join` | See whether your site would pass, then apply |
| `/backlink-exchange:status` | Your points, links given and received |

`/backlink-exchange` on its own works too — just say what you want.

---

## Checking your post

Paste the URL. That's the whole job.

```
/backlink-exchange:check https://yourblog.com/my-new-post
```

Claude runs the check itself and tells you in plain English:

> **PASS** — link found in the third paragraph, dofollow, 1,240 words, 9
> outbound links. You're done. Points post within 15 minutes.

or

> **FAIL** — the link is in your footer, not the article body. Want me to
> rewrite the paragraph and place it properly?

You never run a command, install Python, or read a log. If it fails, Claude
offers to fix the post for you.

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

## Not a member yet?

Install the skill, then say:

```
/backlink-exchange:join
```

Claude looks at your site, tells you honestly whether you'd clear the bar, and —
if you want — **submits your application right there in the chat**. No form, no
tab-switching.

Prefer a form? [Apply here](https://docs.google.com/forms/d/e/1FAIpQLScNiPNmj9IikGWvn_KVziP5ol0aOFwIZlsz-8dmP-KQjbnumw/viewform)
instead. Same queue, same review.

Either way, applying grants nothing on its own — no member ID, no points, no
roster entry until a human approves it.

---

Running your own exchange on this? Setup lives in [OPERATING.md](OPERATING.md).

---

## License

MIT. Some structural patterns adapted from the MIT-licensed
[claude-seo](https://github.com/AgriciDaniel/claude-seo).
