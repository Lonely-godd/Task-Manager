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
        status: str | None,
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


def repo_update_task(
        task_id: str,
        description: str | None = None,
        status: str | None = None,
        priority: int | None = None,
        due_date: str | None = None,
) -> str:
    query = """
            UPDATE tasks
            SET description = COALESCE(%s, description),
                status      = COALESCE(%s, status),
                priority    = COALESCE(%s, priority),
                due_date    = COALESCE(%s, due_date),
                updated_at  = NOW()
            WHERE id = %s RETURNING id; \
            """
    params = (description, status, priority, due_date, task_id)

    with db_cursor() as cur:
        cur.execute(query, params)
        row = cur.fetchone()
        if row is None:
            raise ValueError(f"Task not found: {task_id}")
        return row[0]
