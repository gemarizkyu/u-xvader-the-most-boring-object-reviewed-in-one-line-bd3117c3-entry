"""One-line review of the most boring everyday object: a tea towel.

Writes a single original one-line review to /output/entry.txt.
Deterministic: no clock, no randomness, no network, no model calls.

Why a tea towel: it is the dullest object in the kitchen, and the joke
comes from how it really behaves. A tea towel's only job is drying, yet
after drying a rack of dishes it is always the wettest thing in the
room -- damp, limp, and smug about it. The review format ("one star")
frames it as a product review, the turn lands on the em dash, and the
closer ("hired to dry, fails daily") sharpens the last words instead
of trailing off.
"""

from pathlib import Path

# The review, kept as ordered fragments so the turn (em dash + closer)
# stays visible as its own piece of the line.
REVIEW_PARTS = [
    "Tea towel, one star:",
    "dries every dish in the house,",
    "yet somehow stays the wettest thing in the kitchen",
    "\u2014 hired to dry, fails daily.",
]

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MAX_CHARS = 200


def build_review() -> str:
    """Join the fragments into the single review line."""
    return " ".join(REVIEW_PARTS)


def check_line(line: str) -> None:
    """Enforce the gate the sealed scorer checks: 1-200 chars, one line."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"review line is {len(line)} characters, must be 1-{MAX_CHARS}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("review line must stay on one line")
    if line != line.strip():
        raise ValueError("review line must not start or end with whitespace")
    if not line.strip():
        raise ValueError("review line must not be only whitespace")


def main() -> None:
    line = build_review()
    check_line(line)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} characters to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
