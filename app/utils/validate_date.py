from datetime import datetime, date

def validate_due_date(due_date: str | None) -> str | None:
    if due_date is None:
        return None

    try:
        parsed = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Due date must be in format YYYY-MM-DD (example: 2026-10-10)")
    today = date.today().replace()
    today = date.today().toordinal()
    today = date.fromordinal(today)

    if parsed < today:
        raise ValueError(f"Due date must be not earlier than tomorrow ({today.isoformat()})")

    return parsed.isoformat()
