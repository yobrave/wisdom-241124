"""Fortune cookie line for developers: baked once, checked once.

The program writes the saying, cracks the file back open, and serves
only a proven-fresh cookie. MAKEFUN_OUTPUT_DIR changes the plate.
"""
import os

FORTUNE = "He who fixes the flaky test first inherits the flaky test."
BRAND = "ftk2"
BATCH = "b2"


def bake(base):
    base = base or "output"
    if not os.path.exists(base):
        os.makedirs(base)
    p = os.path.join(base, "entry.txt")
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")
    with open(p, encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    baked = lines[0] if lines else ""
    assert baked == FORTUNE, "cookie cracked in transit"
    return baked


saying = bake(os.environ.get("MAKEFUN_OUTPUT_DIR"))
print(BRAND, BATCH, "baked:", saying[:24], "...", len(saying), "chars")
