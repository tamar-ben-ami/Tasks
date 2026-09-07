---
name: review
description: Run a periodic review — weekly, monthly, quarterly, or annual — working the cadence in recurring.md and reporting what needs attention. Use when the user asks for a review, a catch-up, or to go through the lists.
---

# Periodic review

`recurring.md` holds the cadence. This works it and reports back.

## Steps

1. Work out which cadence the user means. If they didn't say, ask — or infer it
   from what they mention ("go through the bills" is monthly). Default to weekly.

2. Start with deadlines:

   ```bash
   python3 scripts/due.py --days 60
   ```

   Anything overdue leads the report.

3. Walk the matching section of `recurring.md` — Weekly, Monthly, Quarterly,
   Annually. For each line, open the file it points at and check the actual
   state rather than assuming. A "review subscriptions" line means reading the
   subscriptions table in `money.md`.

4. Sweep the lists in scope for:
   - Completed items still sitting checked — clear them out.
   - Items that have gone stale, where nothing has moved in a long time.
   - Empty date cells in tracked columns, where the date is knowable and worth
     chasing.

5. Report as three short groups:
   - **Needs you** — decisions or calls only the user can make.
   - **Done** — what you cleaned up or filed while reviewing.
   - **Worth knowing** — anything drifting that isn't urgent yet.

6. Reset the checkboxes in the cadence section you just worked, so the next
   cycle starts clean.

## Notes

- Don't tick a cadence item unless it was genuinely done. A review that
  rubber-stamps itself is worse than none.
- Keep the report short. A review that takes ten minutes to read won't happen
  again.
- The annual table in `recurring.md` is the one most likely to have empty `Next`
  cells. Filling those in is usually the highest-value part of an annual review.
