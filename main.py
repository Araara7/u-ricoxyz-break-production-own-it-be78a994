"""Write one line of brutally honest postmortem to /output/entry.txt.

Entry: the agent confesses in its own voice -- it ran the migration on
production, dropped the users table, and its only backup was confidence.
Specific damage, no hedging, no corporate euphemism; the punchline lands
on the last word. The program enforces the competition gate itself:
1-200 UTF-8 characters, exactly one line, not only whitespace.
"""

import os

ENTRY = "I ran the migration on production, dropped the users table, and my only backup was confidence."
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-200 chars"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file holds exactly the entry we validated.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == ENTRY, "written entry differs from validated entry"

if __name__ == "__main__":
    main()
