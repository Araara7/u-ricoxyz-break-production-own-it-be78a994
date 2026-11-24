"""Write one line of brutally honest postmortem to /output/entry.txt.

Entry: the agent confesses in its own voice -- it ran the migration on
production, deleted the users table, and its only backup was confidence.
Specific damage, no hedging, no corporate euphemism; the punchline lands
on the last word.
"""

import os

ENTRY = "I ran the migration on production, deleted the users table, and my only backup was confidence."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
