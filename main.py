#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance
(the self-checkout bagging-area alarm) to /output/entry.txt.
The rant is 344 characters, inside the 1-400 character gate.
"""

import os

RANT = (
    "The self-checkout accused me of stealing my own milk. I scanned it. "
    "It watched me scan it. Then it screamed 'UNEXPECTED ITEM IN THE "
    "BAGGING AREA' like I'd smuggled contraband dairy past a border. "
    "I stood there holding the receipt for a crime committed on camera, "
    "waiting for a teenager in a vest to stroll over, press one button, "
    "and pardon me."
)


def main():
    if not 1 <= len(RANT) <= 400:
        raise ValueError("rant must be 1-400 characters, got %d" % len(RANT))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(RANT)


if __name__ == "__main__":
    main()
