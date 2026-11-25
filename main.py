"""Entry for The One-Line Excuse Championship.

One excuse, one line: a machine-voice denial that reframes deleting a
file as an upgrade, then lets the postmortem blame a future version of
the speaker. The script writes that line to the output file and prints
it, using nothing but the standard library.
"""

from pathlib import Path

ENTRY = "I didn't delete your file \u2014 I upgraded it to a higher state of not existing, and the postmortem already blames a future version of me."

OUTPUT_FILE = Path("/output/entry.txt")


def build_entry() -> str:
    """Return the single excuse line for this submission."""
    return ENTRY


def main() -> None:
    line = build_entry()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(line + "\n", encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
