from app.db import db_cursor

if __name__ == "__main__":
    print("Hello there! This is TaskManager, your interactive console program for controlling your tasks.\n"
          "For commands info text 'help'.\n")
    while True:
        request = input(f"What would you like to do? ")

        if not request:
            continue

        match request:
            case "add":
                continue
            case "update":
                continue
            case "delete":
                continue
            case "list":
                continue
            case "set_priority":
                continue
            case "reset":
                response = input("Do you really wish to reset the database? (y/n) ")
                if response in ("y", "Y"):
                    from app.services.reset_db import reset_tables
                    reset_tables()
                    print("Database reset")
                elif response in ("n", "N"):
                    print("Good choice!")
                    continue
            case "init":
                try:
                    from app.services.init_db import apply_schema
                    apply_schema()
                    print("OK: schema applied")
                except Exception as e:
                    print(f"Error: {e}")
            case "help":
                print("Some help")
            case "exit":
                print("Dont worry, your tasks saved local. Goodbye!")
                exit()
            case "ping":
                try:
                    with db_cursor() as cur:
                        cur.execute("SELECT 1;")
                        res = cur.fetchone()
                        print(f"Database is up.")
                except Exception as e:
                    print(f"Database is down: {e}")
            case _:
                print("Unknown command")
