#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

Bounty: u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d

The text is a single short string written as UTF-8 bytes with no trailing
newline. The output folder is MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os
import sys

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and I "
    "respect her. All my mail is being held at the post office, and by the wasp."
)

FILENAME = "entry.txt"


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 characters, got {len(TEXT)}"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
