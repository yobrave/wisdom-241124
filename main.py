# Fortune cookie wisdom for developers: validate + ship (batch r4).
import json, pathlib

HARD_CAP = 120
NICK = "ftk4-cookie-r4"


def snap():
    body = pathlib.Path("entry.txt").read_text(encoding="utf-8").strip()
    if len(body) < 1:
        raise ValueError("empty entry")
    if len(body) > HARD_CAP:
        raise ValueError("too long: %d" % len(body))
    return body


def place(body):
    d = pathlib.Path("out")
    d.mkdir(exist_ok=True)
    (d / "entry.txt").write_bytes((body + "\n").encode("utf-8"))


def main():
    body = snap()
    place(body)
    print(json.dumps({"nick": NICK, "len": len(body), "cap": HARD_CAP, "done": True, "batch": "r4"}))


main()
