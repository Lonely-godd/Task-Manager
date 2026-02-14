HELP_TEXT = """
TaskManager — interactive CLI task manager
==========================================

GENERAL
-------
Commands are entered in the following format:

    <command> [arguments]

Legend:
    *  = optional parameter

Use quotes for multi-word text values.

Example:
    add "Finish backend project" priority 2 due 2026-02-10

AVAILABLE COMMANDS
------------------

init
    Apply database schema (create tables).
    Run once after first launch.

reset
    Drop all tables and reset database.
    WARNING: deletes all data.

ping
    Check database connection.


TASK COMMANDS
-------------

add "<title>" *[description "..."] *[status ...] *[priority N] [due YYYY-MM-DD]
    Create a new task.

    Example:
        add "Buy milk" priority 2 due 2026-02-10

list [status]
    Show tasks.
    If status is omitted — shows all tasks.

    Allowed statuses:
        open
        done
        archived

    Examples:
        list
        list open
        list done


update <id> [description "..."] [priority N] [due YYYY-MM-DD] [status VALUE]
    Update task fields. Only provided fields are changed.

    Example:
        update 325b86eb-c4f4-493f-a4e8-d40f0b91b0e2 \
            desc "Updated text" \
            priority 1 \
            status done


delete <id>  \\ still in development
    Delete task by id.

    Example:
        delete 325b86eb-c4f4-493f-a4e8-d40f0b91b0e2


done <id> \\ still in development
    Shortcut for:
        update <id> status done


SYSTEM
------

help
    Show this help message.

exit
    Exit the application.


NOTES
-----
- Priority range: 1..5
- Dates format: YYYY-MM-DD
- Use quotes for text with spaces
- IDs are UUID strings returned after task creation

"""