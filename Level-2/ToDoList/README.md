# To-Do List Application

**Codveda Technologies — Python Development Internship**  
**Level 2 project**

## Overview

A command-line To-Do List application written in Python. It lets a user add tasks, view tasks, mark tasks as completed, and delete tasks. Task information is stored in `tasks.json` so it remains available after the program is closed and run again.

## Features

- Add a task (empty task names are rejected).
- View all tasks and their completion statuses.
- Mark a selected task as completed.
- Delete a selected task.
- Save and load tasks using JSON.
- Handle invalid menu choices, invalid task numbers, invalid numeric input, missing files, and invalid JSON.

## Requirements

- Python 3
- No third-party packages are required. The application uses Python's built-in `json` and `pathlib` modules.

## How to run

1. Download or clone this folder.
2. Open a terminal in the `ToDoList` folder.
3. Run:

   ```bash
   python to_do_list.py
   ```

4. Follow the menu. Choose `5` to exit.

The application creates or updates `tasks.json` in the same folder as `to_do_list.py`.

## Files

- `to_do_list.py` — application source code.
- `tasks.json` — JSON data file. It starts empty and is updated as tasks are changed.
