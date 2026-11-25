#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single one-star review of gravity — the most essential
service nobody ever subscribed to — to /output/entry.txt (or to the
path given as argv[1]).
"""

import sys
from pathlib import Path

LINE = (
    "★☆☆☆☆ — Gravity: flawless for 4.5 billion years and it still drops "
    "my phone face-down daily — and lately it has started pulling my face "
    "down too. No refunds, no opt-out. One star."
)


def main() -> None:
    # The gate only accepts a single line of 1-200 characters: check the
    # line before writing so a bad edit fails loudly here, not at judging.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} characters"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader collects the output as a different user: keep it readable.
    out.chmod(0o644)


if __name__ == "__main__":
    main()
