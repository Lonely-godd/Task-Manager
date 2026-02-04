from __future__ import annotations

import psycopg2
from psycopg2.extensions import cursor

from contextlib import contextmanager

from app.config import load_config

def connect() :
    cfg = load_config()
    return psycopg2.connect(
        host = cfg["host"],
        port = cfg["port"],
        dbname = cfg["dbname"],
        user = cfg["user"],
        password = cfg["password"],
    )

@contextmanager
def database_cursor() -> cursor:
    """
    Giving cursor inside of transaction
    - commit if everything is good
    - rollback if there is an error
    """
    conn = connect()
    try:
        cur = conn.cursor()
        yield cur
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()