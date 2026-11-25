#!/usr/bin/env python3
"""Everyday Things, Two Lines - entrypoint.

Writes the winning two-line explanation to /output/entry.txt.
Line 1 explains your shadow to a 10-year-old through one analogy:
a flat, dark twin that copies your every move.
Line 2 says why that analogy works: what it maps, and what it leaves out.
"""

import os

LINE_1 = "Your shadow is a flat, dark twin that copies your every move but can never speak."
LINE_2 = "The copying of your shape and movements matches, but the shadow has no body and no thoughts, and it stretches and shrinks as the sun moves."

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    # Gate self-check: exactly two lines, 1-400 characters total.
    text = ENTRY.rstrip("\n")
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, must be 1-400"
    assert len(text.split("\n")) == 2, "entry must be exactly two lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(LINE_1)
    print(LINE_2)


if __name__ == "__main__":
    main()
