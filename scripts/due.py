#!/usr/bin/env python3
"""Scan the markdown lists for dates and report what is overdue or coming up.

Every list keeps its deadlines in markdown tables. This reads those tables and
answers the one question the repo exists to answer: what needs doing now?

Recognised date columns (case-insensitive):
    due · renews · expires · expiry · next · deadline · refill due · contract ends

Recognised value formats:
    2027-03-14   a specific day
    2027-03      a month, treated as the 1st
    03-14        no year, so it recurs every year (birthdays)

Anything else in a date cell is ignored, so placeholder rows and free text in
half-filled tables cost nothing.

Usage:
    python3 scripts/due.py                # overdue + due within 60 days
    python3 scripts/due.py --days 14      # narrower window
    python3 scripts/due.py --all          # everything with a date, ever
    python3 scripts/due.py --quiet        # print nothing when nothing is due
"""

import argparse
import datetime as dt
import glob
import os
import re
import sys

DATE_COLUMNS = {
    'due', 'renews', 'expires', 'expiry', 'next', 'deadline',
    'refill due', 'contract ends',
}

ISO_DAY = re.compile(r'^(\d{4})-(\d{2})-(\d{2})$')
ISO_MONTH = re.compile(r'^(\d{4})-(\d{2})$')
RECURRING = re.compile(r'^(\d{2})-(\d{2})$')


def split_row(line):
    """Split a markdown table row into stripped cell values."""
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [c.strip() for c in line.split('|')]


def is_separator(line):
    return bool(re.match(r'^\s*\|[\s|:-]+\|?\s*$', line)) and '-' in line


def parse_date(value, today):
    """Return (date, recurring) or None if the cell holds no usable date."""
    value = value.strip().strip('*_`')
    m = ISO_DAY.match(value)
    if m:
        try:
            return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))), False
        except ValueError:
            return None
    m = ISO_MONTH.match(value)
    if m:
        try:
            return dt.date(int(m.group(1)), int(m.group(2)), 1), False
        except ValueError:
            return None
    m = RECURRING.match(value)
    if m:
        month, day = int(m.group(1)), int(m.group(2))
        try:
            nxt = dt.date(today.year, month, day)
        except ValueError:
            return None                      # e.g. 02-30
        if nxt < today:
            try:
                nxt = dt.date(today.year + 1, month, day)
            except ValueError:
                return None                  # 02-29 in a following non-leap year
        return nxt, True
    return None


def scan_file(path, today):
    """Yield every dated row in one markdown file."""
    found = []
    section = ''
    headers = None
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().split('\n')

    for line in lines:
        heading = re.match(r'^#{2,3}\s+(.*)', line)
        if heading:
            section = heading.group(1).strip()
            headers = None
            continue

        if not line.strip().startswith('|'):
            headers = None
            continue

        if is_separator(line):
            continue

        cells = split_row(line)
        if headers is None:
            headers = [c.lower() for c in cells]
            continue

        # Label the row by its first non-empty cell; a row of blanks is a template
        label = next((c for c in cells if c), '')
        if not label:
            continue

        for idx, cell in enumerate(cells):
            if idx >= len(headers) or headers[idx] not in DATE_COLUMNS:
                continue
            parsed = parse_date(cell, today)
            if not parsed:
                continue
            date, recurring = parsed
            found.append({
                'date': date,
                'recurring': recurring,
                'label': label,
                'column': headers[idx],
                'section': section,
                'file': os.path.basename(path),
            })
    return found


def collect(root, today):
    items = []
    for path in sorted(glob.glob(os.path.join(root, '*.md'))):
        items.extend(scan_file(path, today))
    items.sort(key=lambda i: i['date'])
    return items


def describe(days):
    if days < 0:
        return '%d day%s overdue' % (-days, '' if days == -1 else 's')
    if days == 0:
        return 'today'
    if days == 1:
        return 'tomorrow'
    return 'in %d days' % days


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--days', type=int, default=60, help='look-ahead window (default 60)')
    ap.add_argument('--all', action='store_true', help='show every dated row')
    ap.add_argument('--quiet', action='store_true', help='print nothing if nothing is due')
    ap.add_argument('--root', default=os.path.join(os.path.dirname(__file__), '..'))
    ap.add_argument('--today', help='override today, as YYYY-MM-DD (for testing)')
    args = ap.parse_args()

    today = dt.date.today()
    if args.today:
        today = dt.datetime.strptime(args.today, '%Y-%m-%d').date()

    items = collect(args.root, today)
    overdue = [i for i in items if i['date'] < today]
    upcoming = [i for i in items if today <= i['date'] <= today + dt.timedelta(days=args.days)]

    if args.all:
        overdue, upcoming = [], items

    if not overdue and not upcoming:
        if not args.quiet:
            print('Nothing due in the next %d days.' % args.days)
        return 0

    def show(item):
        delta = (item['date'] - today).days
        mark = ' ↻' if item['recurring'] else ''
        print('  %s  %-42s %s (%s · %s)%s' % (
            item['date'].isoformat(),
            item['label'][:42],
            describe(delta),
            item['file'],
            item['section'],
            mark,
        ))

    if overdue:
        print('OVERDUE (%d)' % len(overdue))
        for item in overdue:
            show(item)
        print('')

    if upcoming:
        title = 'ALL DATED ITEMS' if args.all else 'NEXT %d DAYS' % args.days
        print('%s (%d)' % (title, len(upcoming)))
        for item in upcoming:
            show(item)

    return 0


if __name__ == '__main__':
    sys.exit(main())
