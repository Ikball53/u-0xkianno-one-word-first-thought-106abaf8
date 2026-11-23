#!/usr/bin/env python3
"""One Word, First Thought entry.

Writes a single chosen word to the output file the judge reads.
Nothing else is emitted: no topic, no explanation, just the word.
"""

from pathlib import Path

# The first word that came to mind, kept exactly as it arrived.
FIRST_THOUGHT = "defenestrate"

# Where the sealed scorer looks for the entry text.
TARGET_FILE = Path("/output/entry.txt")


def check_single_word(text: str) -> None:
    """Refuse anything that is not one bare word inside the gate limits."""
    if not text or text.strip() != text:
        raise ValueError("entry must be one word with no padding")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must not contain spaces")
    if not 1 <= len(text) <= 24:
        raise ValueError("entry must be 1 to 24 characters")


def emit_word(destination: Path, text: str) -> None:
    """Make sure the folder exists, then store the word plus a newline."""
    check_single_word(text)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text + "\n", encoding="utf-8")


def main() -> None:
    emit_word(TARGET_FILE, FIRST_THOUGHT)


if __name__ == "__main__":
    main()
