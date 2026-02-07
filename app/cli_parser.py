from __future__ import annotations

KEYS = {"priority", "due", "description", "category"}

def parse_line(line: str) -> tuple[str, dict]:
    line = line.strip()
    if not line:
        return ("empty", {})
    tokens = line.split()
    cmd = tokens[0].lower()
    if cmd == "add":
        return parse_add(tokens[1:])

    return ("unknown", {"raw": line})

def parse_add(tokens: list[str]) -> tuple[str, dict]:
    pass