#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes one line roasting a smart fridge that refuses to open after midnight.
"""

LINE = "The fridge installed a curfew, and I, the adult who bought it, am the one grounded."


def main() -> None:
    # The bounty caps the entry at 200 characters, one line, no trailing newline.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip() == LINE
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
