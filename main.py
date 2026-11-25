#!/usr/bin/env python3
"""Write the meeting-that-should-have-been-an-email one-liner."""

import os

LINE = (
    # The joke: the meeting only exists because nobody read the email,
    # and its single output is yet another meeting about that same email.
    # Concrete numbers (45 minutes, nine people, one slide) make it a
    # meeting everyone recognises, and the turn lands on the last clause.
    "Forty-five minutes, nine people, one slide \u2014 and the action item "
    "was to schedule another meeting to discuss the email we were "
    "supposed to read before this one."
)


def main() -> None:
    # Deterministic: the same single line on every run, no trailing
    # newline, so the gate sees exactly 159 characters of UTF-8 text.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
