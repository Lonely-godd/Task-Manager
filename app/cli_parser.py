from __future__ import annotations

import shlex
from typing import Callable, Dict, Tuple, Any

Payload = Dict[str, Any]
ParserFn = Callable[[list[str]], Payload]


def parse_line(line: str) -> tuple[str, Payload]:
    """
    Universal CLI parser:
      - tokenizes with shlex (supports quotes)
      - cmd is first token
      - args are the rest
      - dispatches to a command-specific parser
    Returns: (cmd, payload) or ("error"/"unknown"/"empty", payload)
    """
    line = (line or "").strip()
    if not line:
        return "empty", {}

    try:
        tokens = shlex.split(line)
    except ValueError as e:
        # e.g. unmatched quotes
        return "error", {"message": str(e), "raw": line}

    if not tokens:
        return "empty", {}

    cmd = tokens[0].lower()
    args = tokens[1:]

    dispatch: dict[str, ParserFn] = {
        "add": parse_add_args,
        "delete": parse_delete_args,
        "list": parse_list_args,
        "update": parse_update_args,  # stub for now
        "set_priority": parse_set_priority_args,  # stub for now
        "help": parse_help_args,
        "exit": parse_exit_args,
        "quit": parse_exit_args,
    }

    func = dispatch.get(cmd)
    if func is None:
        return "unknown", {"raw": line, "tokens": tokens}

    try:
        payload = func(args)
        return cmd, payload
    except Exception as e:
        # later we’ll replace with custom ParseError
        return "error", {"message": str(e), "cmd": cmd, "args": args}


def parse_add_args(args: list[str]) -> Payload:
    """
    Expected:
      add "Title" desc "Text ..." priority 3 due 2026-02-10 category "Work"
    Minimal version:
      - title is args[0]
      - then key/value pairs
    """
    if not args:
        return {"title": None}  # later: raise error

    payload: Payload = {
        "title": args[0],
    }

    i = 1
    while i < len(args):
        key = args[i].lower()

        # if user accidentally typed a stray word at the end, just stop
        if i + 1 >= len(args):
            payload.setdefault("_unknown", []).append(args[i])
            break

        val = args[i + 1]

        if key in ("desc", "description"):
            payload["description"] = val
            i += 2
        elif key == "priority":
            # minimal parse (can raise ValueError - caught by parse_line)
            payload["priority"] = int(val)
            i += 2
        elif key in ("due", "due_date"):
            payload["due_date"] = val
            i += 2
        elif key == "category":
            payload["category"] = val
            i += 2
        else:
            # unknown tokens -> keep for debugging; later we’ll validate
            payload.setdefault("_unknown", []).append(args[i])
            i += 1

    return payload


def parse_delete_args(args: list[str]) -> Payload:
    """
    Expected:
      delete <id>
    Minimal:
      returns {"id": args[0]} if present else {"id": None}
    """
    return {"id": args[0] if args else None}


def parse_list_args(args: list[str]) -> Payload:
    """
    Expected:
      list [open|done|archived|all]
    Minimal:
      list -> {"filter": "all"}
      list open -> {"filter": "open"}
    """
    flt = (args[0].lower() if args else "open")
    return {"filter": flt}


# ---- stubs (we’ll implement later) ----

def parse_update_args(args: list[str]) -> Payload:
    """
    Later:
      update <id> title "..." desc "..." priority 2 due 2026-02-10 status done
    For now:
      keep raw args
    """
    return {"raw_args": args}


def parse_set_priority_args(args: list[str]) -> Payload:
    """
    Later:
      set_priority <id> <1..5>
    For now:
      keep raw args
    """
    return {"raw_args": args}


def parse_help_args(args: list[str]) -> Payload:
    return {}


def parse_exit_args(args: list[str]) -> Payload:
    return {}
