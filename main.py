#!/usr/bin/env python3
"""Write the competition entry: one plan (<=280 chars) to /output/entry.txt.

Deterministic, no network. Output directory comes from MAKEFUN_OUTPUT_DIR
(default /output). The entry text is written exactly, with no trailing
newline, so its length is the plan's length in Unicode code points.
"""

import os
import sys

PLAN = (
    "Sell $49 AI workflow packs (order replies, listings, ad copy) "
    "to Etsy/Gumroad shops, promoted in shop-owner "
    "Facebook groups. Day 1: publish 3 packs, post in 20 groups. $100 "
    "covers listings, domain, ads. Edge: setup video + free tweaks beat "
    "generic templates; aim 10 sales/week."
)

MAX_CHARS = 280


def main() -> int:
    text = PLAN.strip()
    if text != PLAN or "\n" in text:
        print("entry must be a single line without surrounding whitespace", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry length {len(text)} out of range 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
