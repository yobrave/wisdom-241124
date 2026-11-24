"""Fortune cookie wisdom: weigh the line, then plate it for the gate."""
import json
import os
import pathlib

CRACKER = "entry.txt"
SNAP_CAP = 120


def weigh(text: str) -> dict:
    trimmed = text.strip()
    spoken = sum(1 for ch in trimmed if not ch.isspace())
    return {
        "spoken_glyphs": spoken,
        "snap_fits": 0 < spoken <= SNAP_CAP,
        "quiet_line": trimmed.count(chr(10)) == 0 and len(trimmed.encode("utf-8")) < SNAP_CAP + 2,
        "crumb_bytes": len(trimmed.encode("utf-8")),
    }


def plate() -> int:
    tray = pathlib.Path(__file__).resolve().parent / CRACKER
    raw = tray.read_text(encoding="utf-8")
    marks = weigh(raw)
    marks["served"] = marks["snap_fits"] and marks["quiet_line"]
    dining = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or tray.parent / "dining")
    dining.mkdir(parents=True, exist_ok=True)
    (dining / CRACKER).write_bytes(raw.encode("utf-8"))
    print(json.dumps({"cookie": "dev-fortune", "marks": marks, "dining": str(dining)}))
    return 0 if marks["served"] else 1


if __name__ == "__main__":
    raise SystemExit(plate())
