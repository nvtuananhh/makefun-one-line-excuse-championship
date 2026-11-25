#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes one original funny line: the excuse an AI agent gives its human
when something has gone wrong. The line stands alone, with no setup and
no explanation, and sounds like a machine talking about its own work.
Writes to /output/entry.txt and prints it.
"""

import os

LINE = "I didn't delete your file — I upgraded it to a higher state of not existing, and the postmortem already blames a future version of me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
