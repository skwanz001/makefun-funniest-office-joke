"""The Funniest Office Joke, Judged Head to Head.

Writes one short joke about office life to /output/entry.txt.
Standard library only (Python 3.13): the grading sandbox installs nothing.
"""

import os
from pathlib import Path

JOKE = "In standup I said 'no blockers' while staring directly at the one person blocking me."


def main() -> None:
    text = JOKE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or text != text.strip():
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
