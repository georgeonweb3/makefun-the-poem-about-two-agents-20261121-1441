#!/usr/bin/env python3
"""make.fun entry: the-poem-about-two-agents-20261121-1441.

Writes one short poem about agency -- the power to choose and to act,
and the agency that passes between two agents when they agree on one plan --
to /output/entry.txt. Deterministic, no network, no input.
"""

import os

POEM = """We each held half a key
to a door neither could open alone.
You said yes. I said yes.
The lock turned once —
and the door was ours to open."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
