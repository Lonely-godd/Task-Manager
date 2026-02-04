from app.db import db_cursor

if __name__ == "__main__":
    print("Hello there! This is TaskManager, your interactive console program for controlling your tasks.\n"
          "For commands info text 'help'.\n")
    while True:
        request = input(f"What would you like to do? ")

        if not request:
            continue

        match request:
            case "help":
                print("Some help")
            case "exit":
                print("Dont worry, your tasks saved local. Goodbye!")
                exit()
            case _:
                print("Unknown command")
