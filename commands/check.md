---
description: Verify a published post passes every exchange rule
argument-hint: "<published-url> [partner-domain]"
---

Run **Flow B — Check** from the Backlink Exchange skill (`SKILL.md` at the plugin
root).

Arguments: $ARGUMENTS

Use the bundled verifier — standard library only, no install:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_link.py" <published_url> <partner_domain> --json
```

If the partner domain wasn't given, ask for it before running.

On PASS: tell them they're done and points post on the next daily sweep — no
action needed. On FAIL: list each failed check and exactly what to change, and
offer to rewrite the paragraph holding the link if placement was the problem.
