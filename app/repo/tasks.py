from app.db import db_cursor

def insert_task(
        title: str,
        priority: str | None,
        due_date: str | None,
) -> int:
    query = """
        INSERT INTO tasks (title, priority, due_date)
        VALUES (%s, %s, %s)
        RETURNING id;
    """
    with db_cursor() as cur:
        cur.execute(query, (title, priority, due_date))
        task_id = cur.fetchone()[0]
    return task_id