from prompt_toolkit.validation import ValidationError

from app.repo.tasks import insert_task


def create_task(payload: dict) -> int:
    title = payload.get('title')
    priority = payload.get('priority')
    due_date = payload.get('due_date')

    if not title or not title.strip():
        raise ValueError("Task title cannot be empty")

    if priority is not None:
        if not isinstance(priority, int):
            raise ValueError("Priority must be a number")
        if not (1 <= priority <= 5):
            raise ValueError("Priority must be between 1 and 5")
    return insert_task(
        title = title.strip(),
        priority = priority,
        due_date = due_date,
    )
