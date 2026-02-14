# Task-Manager

Task-Manager is a backend-oriented pet project built to practice real-world backend architecture using Python and PostgreSQL.

The goal of this project is not only to manage tasks, but to learn how backend applications are structured by separating responsibilities into layers:


This project focuses on clean architecture, scalable structure, and clear separation between business logic and database access.

---

## Tech Stack

- **Python** — core application logic
- **PostgreSQL** — persistent storage
- **psycopg2** — database driver
- **dotenv** — environment-based configuration

---

## Features

- Interactive CLI interface
- Task management with statuses
- Priorities and due dates
- PostgreSQL persistence
- Layered backend architecture
- Extensible structure for future API / web integration

---

## Command System

TaskManager works as an interactive console application.

### Command format

<command> [arguments]

Legend:

- `<value>` — required parameter
- `*value` — optional parameter
- use quotes for text with spaces

Example:

add "Finish backend pet project" priority 2 due 2026-02-10

---

## Database Commands

### `init`

Create database tables using schema.

init

---

### `reset`

Drop all tables and reset database.

reset

---

### `ping`

Check database connection.

ping

---

## Task Commands

### `add`

Create a new task.

add "<title>" *description "<desc>" *status VALUE *priority N due YYYY-MM-DD

Example:

add "Buy milk" priority 2 due 2026-02-10

---

### `list`

Display tasks.

list *status

Allowed statuses:

- `open`
- `done`
- `archived`

Examples:

list
list open
list done

---

### `update`

Update task fields. Only provided values are changed.

update <id> *description "..." *priority N *due YYYY-MM-DD *status VALUE

Example:

update 325b86eb-c4f4-493f-a4e8-d40f0b91b0e2
description "Updated description"
priority 1
status done

---

### `delete`

Delete task by id.

delete <id>

---

### `done`

Mark task as completed.

done <id>

Equivalent to:

update <id> status done

---

## System Commands

help — show help message
exit — close application

---

## Notes

- Priority range: `1..5`
- Date format: `YYYY-MM-DD`
- Task IDs are generated as UUID values

---

## Project Goals

This pet project is focused on learning:

- backend architecture thinking
- service vs repository separation
- clean SQL interaction patterns
- scalable project structure
- building software that can later evolve into API or web applications
