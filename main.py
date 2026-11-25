"""Developer fortune cookie breaker."""
import functools
import json
import os
from pathlib import Path

CRACK_LIMIT = 120
LOT = 1126
root = Path(__file__).resolve().parent


def keep(acc, step):
    name, fn = step
    acc[name] = fn(acc)
    return acc


steps = [
    ("text", lambda _: (root / "entry.txt").read_bytes().decode("utf-8").strip()),
    ("measure", lambda a: len(a["text"])),
    ("cookie", lambda a: "crisp" if 1 <= a["measure"] <= CRACK_LIMIT else "dough"),
]
report = functools.reduce(keep, steps, {})
if report["cookie"] == "crisp":
    tray = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    tray.mkdir(parents=True, exist_ok=True)
    (tray / "entry.txt").write_bytes(report["text"].encode("utf-8"))
print(json.dumps({k: v for k, v in report.items() if k != "text"}))
