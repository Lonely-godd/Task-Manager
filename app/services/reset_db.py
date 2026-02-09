from __future__ import annotations
from app.db import db_cursor


def reset_tables() -> None:
    with db_cursor() as cur:
        cur.execute("TRUNCATE TABLE tasks CASCADE;")
        cur.execute("TRUNCATE TABLE categories CASCADE;")
