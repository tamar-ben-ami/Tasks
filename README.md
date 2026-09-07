# Life admin

Personal lists for everything that isn't work — insurance renewals, the weekly
shop, the car test, the paperwork that turns up once a year and is never where
you left it.

Plain markdown files. No app, no account, no sync to set up. Open a file, edit
it, commit.

Set up to be worked with through [Claude Code](https://claude.com/claude-code) —
see [Working with Claude](#working-with-claude) below — but everything here is
readable and editable by hand, and stays that way.

## The lists

| List | What's in it |
| --- | --- |
| 📥 [Inbox](inbox.md) | Unsorted capture. Dump it here, file it later |
| 🔁 [Recurring](recurring.md) | What comes due weekly, monthly, yearly |
| 🛡️ [Insurance](insurance.md) | Policies, renewal dates, the annual review |
| 🛒 [Groceries](groceries.md) | This week's shop plus a staples reference |
| 🏠 [Home](home.md) | Buying, repairs, maintenance, things to buy |
| 💰 [Money](money.md) | Budget, subscriptions, savings, tax |
| 🩺 [Health](health.md) | Appointments, checkup schedule, contacts |
| 🚗 [Car](car.md) | Test and insurance dates, service history |
| 📄 [Documents](documents.md) | Expiry dates, utilities, institutions |
| 🎉 [Family](family.md) | Birthdays, gifts, events, travel |

**Start with [Recurring](recurring.md).** It's the one file that tells you what
you're forgetting.

## How it works

Checkboxes are just text:

```markdown
- [ ] Not done yet
- [x] Done
```

A few conventions that keep it usable:

- **Delete completed items** rather than letting them pile up. Git remembers
  what you did; the list should only show what's left.
- **Anything with a date goes in a table**, so a glance tells you what's close.
- **Dates are ISO**: `2027-03-14` for a specific day, `2027-03` for a month,
  `03-14` (no year) for something that recurs annually, like a birthday.
- **Empty rows and blank bullets are deliberate** — they're there so adding
  something is a two-second edit, not a formatting decision.
- **Cross-link between files** instead of duplicating. Car insurance lives in
  [car.md](car.md); the policy details live in [insurance.md](insurance.md).
- If a list stops earning its keep, delete it. A file you don't trust is worse
  than no file.

## Working with Claude

The repo carries its own instructions. `CLAUDE.md` holds the conventions — where
each kind of thing goes, the date formats, and a firm rule against writing
sensitive data into a git history that keeps it forever.

Four skills cover the recurring work:

| | |
| --- | --- |
| `/due` | What's overdue or coming up, across every list |
| `/shop` | Build the grocery list, and clear it after shopping |
| `/triage` | Empty the inbox into the right lists |
| `/review` | Work the weekly, monthly, or annual cadence |

Plain language works just as well — "add milk and eggs", "what am I forgetting
this month", "sort the inbox".

There's one script, and it's the engine underneath `/due`:

```bash
python3 scripts/due.py              # overdue + due within 60 days
python3 scripts/due.py --days 14    # narrower window
python3 scripts/due.py --all        # every dated row
python3 scripts/test_due.py         # tests
```

A `SessionStart` hook runs it at the beginning of every Claude session, so
anything overdue is on screen before you ask. It stays silent when nothing is
due.

## Editing from a phone

- The GitHub mobile app edits files directly.
- On the web, press <kbd>.</kbd> in the repo to open a full editor in the browser.
- Or clone it and use any markdown app that syncs with git.

Groceries in particular are worth having on a phone — that's where the list gets
used.

## What not to put in here

This is a git repository. Even a private one keeps every version of every file
forever, and deleting something later doesn't remove it from history.

**Don't commit:** ID or passport numbers · bank or card numbers · policy numbers
· passwords or login details · medical results · scanned documents.

Record *where* something lives and *when* it expires. Keep the thing itself in a
password manager or encrypted storage.
