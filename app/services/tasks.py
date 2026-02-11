from prompt_toolkit.validation import ValidationError

from app.repo.tasks import insert_task
from app.repo.tasks import select_task
from app.repo.tasks import repo_update_task


def create_task(payload: dict) -> int:
    title = payload.get('title')
    priority = payload.get('priority')
    due_date = payload.get('due_date')
    description = payload.get('description')
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty")

    if priority is not None:
        if not isinstance(priority, int):
            raise ValueError("Priority must be a number")
        if not (1 <= priority <= 5):
            raise ValueError("Priority must be between 1 and 5")
    return insert_task(
        title=title.strip(),
        description=description,
        priority=priority,
        due_date=due_date,
    )


def get_task(payload: dict):
    status = payload.get('filter')
    if status is None:
        return select_task(status)
    if status not in ("open", "done", "archived"):
        raise ValueError("Unknown status filter")
    return select_task(status)


def update_task(payload: dict) -> str:
    task_id = payload.get('id')
    if not task_id or not task_id.strip():
        raise ValueError("You must enter a task id to update tasks!")

    description = payload.get('description')
    status = payload.get('status')
    priority = payload.get('priority')
    due_date = payload.get('due_date')

    if status is not None and status not in ("open", "done", "archived"):
        raise ValueError("Unknown status filter")
    if priority is not None and not (1 <= priority <= 5):
        raise ValueError("Priority must be between 1 and 5")

    return repo_update_task(task_id=task_id.strip(),
                            description=description,
                            status=status,
                            priority=priority,
                            due_date=due_date,
                            )
