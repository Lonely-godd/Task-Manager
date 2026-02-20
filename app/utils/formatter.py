from datetime import date, datetime
from typing import Iterable


def format_tasks(rows: Iterable[tuple]) -> str:
    """
    Pretty-prints tasks table

    Expected row format:
    (
        id,
        title,
        description,
        status,
        priority,
        due_date,
        created_at
    )
    """

    if not rows:
        return "No tasks found."

    headers = ["ID", "TITLE", "STATUS", "PRIORITY", "DUE_DATE", "CREATED_AT"]
    formatted_rows = []

    for row in rows:
        task_id, title, _, status, priority, due_date, created_at = row
        due_str = due_date.strftime("%Y-%m-%d")
        created_str = created_at.strftime("%Y-%m-%d %H:%M")
        formatted_rows.append([
            str(task_id),
            title,
            status,
            str(priority),
            due_str,
            created_str,
        ])
    # Calculate column widths
    col_widths = [
        max(len(str(cell)) for cell in column)
        for column in zip(headers, *formatted_rows)
    ]
    # Build lines
    lines = []

    # Header
    header_line = "  ".join(
        header.ljust(width)
        for header, width in zip(headers, col_widths)
    )
    lines.append(header_line)
    lines.append("-" * len(header_line))

    for row in formatted_rows:
        lines.append(
            "  ".join(
                cell.ljust(width)
                for cell, width in zip(row, col_widths)
            )
        )
    return "\n".join(lines)
