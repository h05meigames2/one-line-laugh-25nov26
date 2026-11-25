#!/usr/bin/env python3
"""One Line, One Laugh — writes a single original one-liner to /output/entry.txt.

Stdlib only, deterministic, no network. The output directory honours the
MAKEFUN_OUTPUT_DIR environment variable (used as a stand-in for /output
when testing locally); otherwise it writes to /output.
"""

import os

JOKE = "My horoscope told me to take a risk, so I texted my ex — now my horoscope is blocked too."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
