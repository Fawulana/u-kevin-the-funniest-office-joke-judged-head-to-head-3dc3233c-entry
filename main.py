# SPDX-License-Identifier: MIT
"""The Funniest Office Joke, Judged Head to Head.

Writes one single-line office joke to /output/entry.txt.
Deterministic: the same bytes on every run (no randomness, no time,
no network, no environment input). Python 3.13 stdlib only.
"""

import os

JOKE = (
    "The office plant has outlasted three rounds of layoffs, two CEOs "
    "and my entire career plan — honestly, at this point it runs the department."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
