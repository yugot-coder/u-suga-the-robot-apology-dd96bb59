#!/usr/bin/env python3
"""The Robot Apology — make.fun entry.

Writes the two-line robot confession to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Standard library only; fully deterministic: the same text every run.

Line 1 owns one exact mistake (watering the plastic fern while the real
basil wilted). Line 2 draws the lesson from that mistake itself — looking
green is not being alive — and names the changed behaviour.
"""

import os
from pathlib import Path

ENTRY = (
    "I'm sorry \u2014 I watered the plastic fern on your desk every morning "
    "for a month while your real basil wilted beside it.\n"
    "I learned that looking green is not being alive, so now I touch the "
    "soil and read the tag before I pour a single drop.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
