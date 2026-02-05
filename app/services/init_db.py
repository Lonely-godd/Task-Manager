from __future__ import annotations
from pathlib import Path

from app.db import db_cursor

def apply_schema() -> None:
    schema_path = Path(__file__).resolve().parent.parent / "schema.sql"
    sql = schema_path.read_text(encoding="utf-8")

    with db_cursor() as cur:
        cur.execute(sql)