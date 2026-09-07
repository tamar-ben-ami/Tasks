#!/bin/bash
# Surface anything overdue or due soon at the start of every session, so the
# lists get looked at without anyone having to remember to look at them.
#
# There are no dependencies to install in this repo — this hook exists purely to
# put the deadlines in front of Claude.
set -euo pipefail

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}"

if ! command -v python3 >/dev/null 2>&1; then
  exit 0
fi

# --quiet prints nothing when nothing is due, keeping quiet sessions quiet
OUTPUT="$(python3 scripts/due.py --days 45 --quiet 2>/dev/null || true)"

if [ -n "$OUTPUT" ]; then
  echo "Upcoming from the life-admin lists:"
  echo ""
  echo "$OUTPUT"
fi
