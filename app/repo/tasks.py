from app.db import db_cursor


def insert_task(
        title: str,
        description: str | None,
        priority: int | None,
        due_date: str | None,
) -> int:
    if priority is None:
        query = """
                INSERT INTO tasks (title, description, priority, due_date)
                VALUES (%s, %s, 3, %s) RETURNING id; \
                """
        params = (title, due_date)
    else:
        query = """
                INSERT INTO tasks (title, description, priority, due_date)
                VALUES (%s, %s, %s, %s) RETURNING id; \
                """
        params = (title, description, priority, due_date)
    with db_cursor() as cur:
        cur.execute(query, params)
        task_id = cur.fetchone()[0]
    return task_id


def select_task(
        status: int | None,
):
    if status is None:
        query = """
                SELECT id, title, description, status, priority, due_date, created_at
                FROM tasks
                ORDER BY created_at DESC; \
                """
        params = ()
    else:
        query = """
                SELECT id, title, description, status, priority, due_date, created_at
                FROM tasks
                WHERE status = %s
                ORDER BY created_at DESC; \
                """
        params = (status,)
    with db_cursor() as cur:
        cur.execute(query, params)
        tasks = cur.fetchall()
    return tasks
