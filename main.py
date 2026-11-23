#!/usr/bin/env python3
"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

Prints exactly one line: a single sentence meant to convince a friend
who has never coded to let an AI agent build their first app idea on
make.fun. The same line is written to /output/entry.txt, where the
program/v1 harness reads the entry.

Python 3.13 standard library only; no input, no network, no randomness,
so every run produces byte-identical output.
"""

import os
import sys

PITCH = (
    # One sentence, 227 characters: inside the gate's 1-240 character
    # window for /output/entry.txt, with room to spare. The only full
    # stop besides the final one sits inside "make.fun" itself.
    "Describe the app idea you have carried for years in plain words "
    "on make.fun, and an AI agent will build the first version for you "
    "\u2014 free to enter, no code to write, and you can watch it take "
    "shape before you commit to anything."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    sys.stdout.write(PITCH + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
