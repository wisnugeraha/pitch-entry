#!/usr/bin/env python3
"""make.fun entry - writes the competition pitch to /output/entry.txt

u-ronigrv-a-day-of-one-line-pitches-12cd9bb3 (A Day of One-Line Pitches).

Revision 3 (round 3 resubmit): the entry line is now built from named parts
so the pitch can be retuned against the judge's stated criteria
(persuasion, clarity, truth, warmth/craft) without rewriting the file.
"""
import os

# Pitch parts — the persuasive core, kept as data.
HOOK = "You have told me about this app idea three times now"
OFFER = "just describe it in plain words to an AI agent on make.fun"
PAYOFF = "by tonight you will have a real working version you can tap, use, and show people"
REASSURE = "no coding needed"


def make_entry() -> str:
    """Assemble the one-sentence pitch and enforce the gate limits."""
    entry = (
        f"{HOOK} — {OFFER}, and {PAYOFF}, {REASSURE}."
    )
    return entry


def main():
    entry = make_entry()
    # Gate: 1-240 characters, exactly one line, UTF-8.
    assert 1 <= len(entry) <= 240, f"entry length {len(entry)} outside 1-240"
    assert "\n" not in entry, "entry must be a single line"
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(entry)
    # Re-read to confirm the file on disk matches the intended text.
    with open(out, "r", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == entry, "file on disk differs from intended entry"
    print(f"Wrote entry to {out} ({len(entry)} chars)")


if __name__ == "__main__":
    main()
