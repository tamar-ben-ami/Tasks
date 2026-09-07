# Life admin

Personal lists for everything that isn't work — insurance renewals, the weekly
shop, the car test, the paperwork that turns up once a year and is never where
you left it.

Plain markdown files. No app, no account, no sync to set up. Open a file, edit
it, commit.

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
- **Empty rows and blank bullets are deliberate** — they're there so adding
  something is a two-second edit, not a formatting decision.
- **Cross-link between files** instead of duplicating. Car insurance lives in
  [car.md](car.md); the policy details live in [insurance.md](insurance.md).
- If a list stops earning its keep, delete it. A file you don't trust is worse
  than no file.

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
