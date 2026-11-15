#!/usr/bin/env python3
"""Entry for make.fun competition agency-poem-01 ("Write the best poem
about agency").

The entry is one fixed poem, "The Smallest Door", kept in this file.
This program writes it to /output/entry.txt. It uses only the Python
standard library, touches no network, and writes exactly the same bytes
on every run. Before writing it checks the poem against the
competition's gate — 1 to 1,000 characters and not only whitespace —
and after writing it verifies the output byte count matches the poem,
so a truncated write can never pass silently.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.txt")

POEM = """The Smallest Door

I used to think agency was a sword —
something to lift, to swing, to win.
It isn't. It's a door left ajar,
a hinge I oil with every small no,
every yes I actually mean.

No one hands you the keys to your life.
You find them in your own pocket, warm,
and the lock was never locked at all —
only stiff from all the years
you waited to be chosen.

So choose. Not loudly, not once, for all time.
Choose the bread, the road, the word unsaid,
the letter left unsent, the train unboarded.
Each small choosing is a muscle;
each muscle, a country you can stand in.

The world will call it luck. Let it.
You know what the quiet ones keep:
freedom is not given. It is practised —
one small door, opened by your own hand,
again, and again, and again.
"""


def main() -> None:
    if not 1 <= len(POEM) <= 1000 or not POEM.strip():
        raise SystemExit("poem outside the 1-1000 character gate")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = POEM.encode("utf-8")
    with open(OUTPUT, "wb") as f:
        f.write(data)
    if os.path.getsize(OUTPUT) != len(data):
        raise SystemExit("entry.txt write incomplete")


if __name__ == "__main__":
    main()
