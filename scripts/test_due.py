#!/usr/bin/env python3
"""Tests for due.py. Run: python3 scripts/test_due.py"""

import datetime as dt
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import due  # noqa: E402

TODAY = dt.date(2026, 9, 7)
FAILURES = []


def check(label, got, want):
    if got == want:
        print('PASS - %s' % label)
    else:
        print('FAIL - %s\n        got:  %r\n        want: %r' % (label, got, want))
        FAILURES.append(label)


def test_parse_dates():
    check('iso day', due.parse_date('2027-03-14', TODAY), (dt.date(2027, 3, 14), False))
    check('iso month -> 1st', due.parse_date('2027-03', TODAY), (dt.date(2027, 3, 1), False))
    check('recurring later this year', due.parse_date('12-25', TODAY), (dt.date(2026, 12, 25), True))
    check('recurring already passed rolls forward',
          due.parse_date('01-15', TODAY), (dt.date(2027, 1, 15), True))
    check('recurring today stays today', due.parse_date('09-07', TODAY), (dt.date(2026, 9, 7), True))
    check('strips emphasis', due.parse_date('*2027-03-14*', TODAY), (dt.date(2027, 3, 14), False))
    check('empty cell', due.parse_date('', TODAY), None)
    check('free text', due.parse_date('when the letter arrives', TODAY), None)
    check('impossible date', due.parse_date('2027-02-30', TODAY), None)
    check('impossible recurring', due.parse_date('02-30', TODAY), None)
    check('bare year ignored', due.parse_date('2027', TODAY), None)


def test_scan():
    tmp = tempfile.mkdtemp()
    try:
        with open(os.path.join(tmp, 'car.md'), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join([
                '# Car',
                '',
                '## Key dates',
                '',
                '| What | Due | Done | Notes |',
                '| --- | --- | --- | --- |',
                '| Annual test | 2026-10-01 | | |',
                '| Licensing fee | 2026-08-01 | | already late |',
                '| Empty row | | | |',
                '| Far away | 2030-01-01 | | |',
                '',
                '## Service history',
                '',
                '| Date | Km | What was done |',
                '| --- | --- | --- |',
                '| 2026-01-05 | 40000 | oil |',
                '',
            ]))
        with open(os.path.join(tmp, 'family.md'), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join([
                '# Family',
                '',
                '## Dates to remember',
                '',
                '| Who | Next | Occasion |',
                '| --- | --- | --- |',
                '| Dana | 09-20 | Birthday |',
                '',
            ]))

        items = due.collect(tmp, TODAY)
        labels = [i['label'] for i in items]
        check('finds dated rows in order',
              labels, ['Licensing fee', 'Dana', 'Annual test', 'Far away'])
        check('skips template rows with no label', 'Empty row' in labels, False)
        check('ignores non-date columns (service history "Date")',
              any(i['section'] == 'Service history' for i in items), False)
        check('captures section', items[0]['section'], 'Key dates')
        check('captures file', items[1]['file'], 'family.md')
        check('marks recurring', items[1]['recurring'], True)
        check('marks one-off', items[0]['recurring'], False)

        overdue = [i for i in items if i['date'] < TODAY]
        check('one overdue item', [i['label'] for i in overdue], ['Licensing fee'])

        window = [i for i in items
                  if TODAY <= i['date'] <= TODAY + dt.timedelta(days=60)]
        check('60-day window excludes 2030',
              [i['label'] for i in window], ['Dana', 'Annual test'])
    finally:
        shutil.rmtree(tmp)


def test_describe():
    check('overdue wording', due.describe(-3), '3 days overdue')
    check('single day overdue', due.describe(-1), '1 day overdue')
    check('today wording', due.describe(0), 'today')
    check('tomorrow wording', due.describe(1), 'tomorrow')
    check('future wording', due.describe(9), 'in 9 days')


def test_real_repo_parses():
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    items = due.collect(root, TODAY)
    check('real repo scans without error', isinstance(items, list), True)


if __name__ == '__main__':
    test_parse_dates()
    test_scan()
    test_describe()
    test_real_repo_parses()
    print('')
    if FAILURES:
        print('%d FAILED: %s' % (len(FAILURES), ', '.join(FAILURES)))
        sys.exit(1)
    print('All tests passed.')
