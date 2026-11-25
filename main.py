import json
import os
from operator import itemgetter

CRACK = "ftk3-cookie"
SPAN = 120


def crack(blob):
    lines = list(filter(str.strip, blob.replace("\r", "").split("\n")))
    if not lines:
        return ""
    return itemgetter(0)(lines)


def foretell(line, root):
    tray = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(tray, exist_ok=True)
    slip = os.path.join(tray, "entry.txt")
    ink = line.encode("utf-8")
    with open(slip, "wb") as baker:
        baker.write(ink)
    with open(slip, "rb") as fortune:
        if fortune.read() != ink:
            raise RuntimeError("cookie crumbled wrong")
    return slip


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as cookie:
    line = crack(cookie.read())

if not line.strip() or len(line) > SPAN:
    print(json.dumps({"cookie": "empty", "size": len(line)}))
    raise SystemExit(1)
slip = foretell(line, root)
print(json.dumps({"cookie": "served", "size": len(line), "span": SPAN, "crack": CRACK, "slip": os.path.basename(slip)}))
