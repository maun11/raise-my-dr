# The gate

Every domain is checked automatically before it can be assigned. These are the
thresholds. A domain failing any of them goes to human review, not straight to
rejection.

| Check | Threshold |
|---|---|
| Verified authority | ≥ 5 |
| Domain age | ≥ 6 months |
| Indexed URLs in sitemap | ≥ 10 |
| Average post word count (3 sampled) | ≥ 600 |
| Outbound links per post | ≤ 15 |
| Spam signals | ≤ 3 / 10 |
| Category | Not gambling, adult, pharma, essay mills, crypto casinos |
| Duplicate owner | No shared WHOIS, IP or analytics ID with an existing member |

## What claimed authority is for

Nothing. The form asks for it so we can see how far off people are. Every
calculation uses the verified number our checker fetched. A blank verified score
means the member stays on Probation and cannot be assigned.

## Ongoing

Authority is re-scored periodically. Points per link recalculate automatically, so
a site that gets de-indexed or decays becomes worth less without anyone
intervening. Two member flags auto-pause an account pending review.

## Why Probation exists

It's the cheapest possible defence. A junk site has to publish two real posts and
keep the links live for a month before it can extract anything. Almost none
bother — and the few that do have already given the network two links first.
