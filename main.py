#!/usr/bin/env python3
"""make.fun entry - writes the competition text to /output/entry.txt"""
import os

def main():
    entry = 'I built a bot that auto-writes the boring parts of your job; you get 3 hours back every day, it pays for itself in one week, and it already knows more about your codebase than your intern.'
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(entry)

if __name__ == "__main__":
    main()
