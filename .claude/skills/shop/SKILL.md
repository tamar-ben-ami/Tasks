---
name: shop
description: Manage the grocery list — add items to this week's shop, build a list from the staples reference or from meals, and clear the list after shopping. Use when the user mentions buying food or household items, or says they've been to the shop.
---

# Groceries

Two modes. Work out which from what the user said.

## Adding items

The common case: "add milk and tomatoes".

1. Open `groceries.md`.
2. Put each item under the right section of **This week** — Produce, Dairy &
   eggs, Bread & bakery, Meat & fish, Dry goods & tins, Frozen, Household &
   cleaning, Toiletries, Other. The sections follow the walk through the store,
   which is the whole point of them.
3. Use the blank `- [ ]` lines already there before adding new ones.
4. If an item doesn't fit any section, use **Other** rather than inventing a
   section.
5. Confirm in one line: what was added, and where.

## Building a list

"What do we need this week?" or "make a list for the week".

1. Read the **Staples** reference and the **Running low** list at the bottom.
2. Everything under **Running low** goes into **This week**, then clear it out
   of Running low.
3. Suggest staples to add, but don't add them uninvited — ask which are needed.
   You cannot see their fridge.
4. If the user gives meals rather than items, work out the ingredients and file
   them by section.

## After shopping

"Got everything", "back from the shop", "done".

1. Delete the checked items from **This week**, leaving the section headings and
   a blank `- [ ]` line under each.
2. Anything the user says was unavailable stays on the list — move it back to
   unchecked rather than deleting it.
3. Never delete the **Staples** reference. It's the source you rebuild from.

## Notes

- Items bought at a shop but not food — a lightbulb, a screwdriver — belong in
  `home.md` under "To buy for the house", not here.
- Keep **Don't buy again** in mind when suggesting staples.
