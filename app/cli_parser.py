from __future__ import annotations

import shlex

KEYS = {"priority", "due", "description", "category"}


def parse_line(line: str) -> tuple[str, dict]:
    tokens = shlex.split(line)
    if not tokens:
        return ("empty", {})
    cmd = tokens[0].lower()
    if cmd == "add":
        return parse_add(tokens)

    return ("unknown", {"raw": line})


def parse_add(tokens) -> tuple[str, dict]:
    tokens_dict = dict()
    i = 0
    while i < len(tokens):
        if tokens[i] == "add":
            tokens_dict["INSERT"] = tokens[i + 1]
            i += 1
        elif tokens[i] == "desc":
            tokens_dict["DESCRIPTION"] = tokens[i + 1]
            i += 1
        elif tokens[i] == "priority":
            tokens_dict["PRIORITY"] = int(tokens[i + 1])
            i += 1
        elif tokens[i] == "due":
            tokens_dict["DUE"] = tokens[i + 1]
            i += 1
        i += 1
