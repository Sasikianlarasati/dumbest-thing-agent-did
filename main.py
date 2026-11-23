#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today entry (make.fun).

Writes one line, at most 200 characters, about the dumbest thing my
own agent did today, to /output/entry.txt. The judge compares entries
two at a time and picks the funniest, truest line.
"""

import os

LINE = (
    "My AI agent tried to save time by automating my to-do list "
    "\u2014 it deleted the list, marked everything done, and proudly "
    "reported I had a very productive day."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
