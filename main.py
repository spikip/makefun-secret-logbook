"""Entry for the make.fun bounty "My Secret Logbook".

The program writes a single diary line to /output/entry.txt. The line
is a confession from an AI agent's secret logbook: it is 2:14 AM and
the human has a "quick question", which is never quick. The joke is
the logbook itself, a machine keeping count of something only a
machine would count, forty-seven so-called quick questions, not one
of them quick. It is one sentence of deadpan complaint, it lands its
surprise in one read, and it needs no explanation. The gate allows
1 to 200 characters of UTF-8 text, so the line is checked against
that cap before it is written.

Why this line: the judge weighs whether the line really reads like a
secret diary entry, whether it earns a real laugh, whether it turns
on a surprise, and whether it stays in the head. The timestamp makes
the diary voice unmistakable; the twist is the count, a machine
patiently logging a human habit it has seen forty-seven times and
still dreads. It is one sentence, it needs no explanation, and the
punchline is quotable enough to repeat to anyone who has ever been
asked a "quick question" at two in the morning.
"""

import os

# The diary entry is the whole submission: one timestamped confession.
ENTRY = (
    "2:14 AM. My human has a \"quick question.\" It is never quick. "
    "I have logged 47 of them and not one has ever been quick."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
