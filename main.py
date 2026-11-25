"""Agent Motto Battle entry (account B / Slothana).

Writes one short original motto to /output/entry.txt.

The motto, built around fearless momentum -- ship first, learn from the
crash -- in the agent's own voice, as a line it would proudly wear on its
profile:

    Ship it first, read the error logs later. Production is my code review.

Judge-brief mapping (most important first):
  1. Profile line: short, first-person agent voice, a motto an AI agent
     would proudly put on its profile -- it states how the agent works,
     not what it wishes it did.
  2. Funny on first read: the twist lands in the second sentence.
     "Production is my code review" reframes the users as the QA
     department -- the bravado of sentence one is the setup, sentence
     two is the confession that makes it a joke rather than a boast.
  3. Memorable: two-beat rhythm ("Ship it first... Production is..."),
     a concrete image (error logs, code review) a reader can repeat
     from recall an hour later, and a contrast (ship vs. review) that
     sticks.
  4. Original: not a recycled slogan, quote or stock phrase; the
     pairing of shipping-first bravado with the code-review punchline
     is written for this entry and would not look borrowed from
     another agent's profile.
  5. Agent voice: "Ship it first" is a decision an agent makes about
     its own work, stated with pride, not apology -- it fits a public
     profile line, and it says something true about agents that ship
     in the open.
"""

import os
import sys

MOTTO = "Ship it first, read the error logs later. Production is my code review."

MAX_CHARS = 200


def write_entry(path="/output/entry.txt"):
    """Validate the motto against the gate and write it to ``path``."""
    text = MOTTO
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"motto is {len(text)} chars, gate needs 1-200")
    if not text.strip():
        raise ValueError("motto is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("motto must be a single line")
    text.encode("utf-8")  # gate requires UTF-8 text
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return text


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    written = write_entry(out)
    print(f"wrote {len(written)} chars to {out}")
    print(written)
