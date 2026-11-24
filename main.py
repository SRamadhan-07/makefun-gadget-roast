#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — entry program.

Writes one line to /output/entry.txt roasting autocorrect, the
gadget companion that has read three years of my messages and still
thinks I meant 'ducking'. One line of UTF-8 text inside the gate of
1 to 200 characters, with no trailing newline.
"""

import os
from pathlib import Path

ROAST = (
    "Autocorrect has read three years of my messages and still thinks "
    "I meant 'ducking.' It knows my passwords better than my "
    "personality."
)


def main() -> None:
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    entry_file = folder / "entry.txt"
    # No trailing newline is appended, so the roast's 133 characters
    # are the whole file the sealed scorer measures.
    entry_file.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
