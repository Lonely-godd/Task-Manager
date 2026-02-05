from __future__ import annotations
from app.db import db_cursor


def reset_tables() -> None:
    with db_cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS tasks CASCADE;")
        cur.execute("DROP TABLE IF EXISTS categories CASCADE;")
