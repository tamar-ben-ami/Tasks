# CLAUDE.md

Personal life-admin lists in plain markdown — insurance, groceries, the car, the
paperwork. There is no app and no build step: the files *are* the product. Almost
every request here is a small, precise edit to a list.

## Hard rules

**1. Never write sensitive data into these files.** No ID or passport numbers, no
account, card, or policy numbers, no passwords, no medical results. Git history is
permanent — deleting it later does not remove it. Record *where* a document lives
and *when* it expires, never the document itself. If the user supplies such a
value, leave a placeholder, use it for the task at hand, and tell them why it
wasn't written down.

**2. Never invent a date, cost, provider, or reference number.** A blank cell is
blank because nobody knows the answer yet. Leave it blank and ask. A plausible
invented renewal date is worse than an empty one — it will be trusted.

**3. Edit narrowly.** Change the lines you were asked about. Don't reflow prose,
re-pad table columns, reorder sections, or "tidy" files you weren't asked to
touch. Diffs here should be readable at a glance.

**4. Empty rows and blank bullets are deliberate.** They exist so adding an item
is a two-second edit. Don't delete them as clutter, and don't fill them with
examples.

## Where things go

| The user mentions | File |
| --- | --- |
| Milk, shampoo, anything bought at a shop | [groceries.md](groceries.md) |
| A policy, cover, quote, renewal, claim | [insurance.md](insurance.md) |
| Rent, repairs, furniture, the apartment, moving | [home.md](home.md) |
| Budget, subscriptions, savings, pension, tax | [money.md](money.md) |
| Appointments, checkups, prescriptions | [health.md](health.md) |
| The car — test, service, tires, garage | [car.md](car.md) |
| Passports, licences, utilities, an institution | [documents.md](documents.md) |
| Birthdays, gifts, events, a trip | [family.md](family.md) |
| A cadence — "every month I should…" | [recurring.md](recurring.md) |
| Genuinely unclear, or a half-formed thought | [inbox.md](inbox.md) |

When something could sit in two files, put it where the user would look for it,
add a cross-link from the other, and don't duplicate the content.

## Conventions

**Checkboxes** are `- [ ]` open, `- [x]` done. Mark items done as they happen;
clear completed lines out during a review rather than letting them accumulate.
Groceries are the exception — clear those right after the shop.

**Dates are ISO, always**, because `scripts/due.py` parses them:

| Format | Means | Example |
| --- | --- | --- |
| `YYYY-MM-DD` | A specific day | `2027-03-14` |
| `YYYY-MM` | A month, treated as the 1st | `2027-03` |
| `MM-DD` | Recurs every year (birthdays) | `03-14` |

**Deadlines live in tables, in a column the scanner reads.** These header names
are tracked — use one of them, or the date becomes invisible:

`Due` · `Renews` · `Expires` · `Expiry` · `Next` · `Deadline` · `Refill due` · `Contract ends`

Columns holding *past* events (`Done`, `Last done`, `Renewed`, `Date` in a
history table) are deliberately not scanned. Keep it that way.

**Anything with a deadline goes in a table; anything actionable is a checkbox.**

## Tools

```bash
python3 scripts/due.py              # overdue + due within 60 days
python3 scripts/due.py --days 14    # narrower window
python3 scripts/due.py --all        # every dated row
python3 scripts/test_due.py         # run after touching due.py
```

`scripts/due.py` is the only code in the repo. If you change it, run the tests.

## Skills

Invoke these directly, or just ask in plain language:

| Skill | Does |
| --- | --- |
| `/due` | What's overdue or coming up, across every list |
| `/shop` | Build the grocery list, and clear it after shopping |
| `/triage` | Empty the inbox into the right lists |
| `/review` | Work the weekly, monthly, or annual cadence |

## Working style here

- Prefer doing the edit over describing it. "Add milk" means add milk.
- Batch related edits into one pass, then say what changed in a line or two.
- When a request implies a date the user didn't give ("renew the passport"),
  make the edit and ask for the date separately — don't block on it.
- Don't ask which file something goes in; use the routing table and say where
  you put it. The user can move it.
