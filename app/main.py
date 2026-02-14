from app.db import db_cursor
from app.cli_parser import parse_line

HELP_COMMANDS = {"reset", "init", "help", "exit", "ping"}

if __name__ == "__main__":
    print(
        "Hello there! This is TaskManager, your interactive console program for controlling your tasks.\n"
        "For commands info text 'help'.\n"
    )

    while True:
        request = input("What would you like to do? ").strip()
        if not request:
            continue

        cmd, payload = parse_line(request)

        if request in HELP_COMMANDS:
            match request:
                case "reset":
                    response = input("Do you really wish to reset the database? (y/n) ")
                    if response in ("y", "Y"):
                        from app.services.reset_db import reset_tables

                        reset_tables()
                        print("Database reset")
                    else:
                        print("Good choice!")
                case "init":
                    try:
                        from app.services.init_db import apply_schema

                        apply_schema()
                        print("OK: schema applied")
                    except Exception as e:
                        print(f"Error: {e}")
                case "help":
                    from app.help_text import HELP_TEXT
                    print(HELP_TEXT)
                case "exit":
                    print("Dont worry, your tasks saved local. Goodbye!")
                    raise SystemExit
                case "ping":
                    try:
                        with db_cursor() as cur:
                            cur.execute("SELECT 1;")
                        print("Database is up.")
                    except Exception as e:
                        print(f"Database is down: {e}")
        else:
            match cmd:
                case "add":
                    try:
                        from app.services.tasks import create_task

                        task_id = create_task(payload)
                        print(f"Created task with id: {task_id}")
                    except Exception as e:
                        print(f"Error: {e}")
                case "list":
                    try:
                        from app.services.tasks import get_task

                        tasks = get_task(payload)
                        for t in tasks:
                            print(t)
                    except Exception as e:
                        print(f"Error: {e}")
                case "update":
                    try:
                        from app.services.tasks import update_task

                        task_id = update_task(payload)
                        print(f"Updated task with id: {task_id}")
                    except Exception as e:
                        print(f"Error: {e}")
                case "unknown":
                    print("Unknown command:", payload.get("raw"))
                case "error":
                    print("Parse error:", payload.get("message"))
                case _:
                    print("Unhandled command:", cmd, payload)
