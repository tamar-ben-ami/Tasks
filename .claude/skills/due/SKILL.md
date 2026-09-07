---
name: due
description: Report what is overdue or coming up across every list — renewals, expiry dates, appointments, birthdays. Use when the user asks what's due, what's coming up, what they're forgetting, or to check deadlines.
---

# What's due

Answer the question the repo exists for: what needs doing now?

## Steps

1. Run the scanner:

   ```bash
   python3 scripts/due.py --days 60
   ```

   Narrow with `--days 14` if the user asked about this week or fortnight;
   use `--all` if they want the full horizon.

2. Report it back grouped as **Overdue** then **Coming up**, in plain sentences
   rather than pasting the raw output. For each item say what it is, when it's
   due, and which file it lives in.

3. Add what the script cannot know:
   - An overdue item usually needs a next action, not just a flag. Say what that
     action is ("book the test", "call for a quote").
   - Check the relevant file for open checkboxes tied to the same thing — an
     overdue insurance renewal often has an unticked "get comparison quotes"
     sitting above it.

4. If nothing is due, say so in one line. Then mention how many tracked dates are
   actually filled in — a quiet report means nothing is scheduled, which is
   different from nothing being wrong. Point at empty date columns worth filling.

## Notes

- The scanner only reads tracked date columns (`Due`, `Renews`, `Expires`,
  `Next`, `Deadline`, `Refill due`, `Contract ends`). If the user expected
  something to appear and it didn't, check the column header first.
- Don't offer to fill in missing dates yourself. Ask for them.
