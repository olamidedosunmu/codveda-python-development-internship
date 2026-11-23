"""Codveda Level 2 - To-Do List Application.

A command-line to-do list that supports adding, viewing, completing,
deleting, and permanently storing tasks in a JSON file.
"""

import json
from pathlib import Path


TASK_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load tasks from tasks.json. Return an empty list if it does not exist."""
    try:
        with TASK_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            print("Warning: tasks.json does not contain a task list. Starting empty.")
            return []

        # Ignore malformed entries rather than crashing the application.
        valid_tasks = []
        for task in tasks:
            if (
                isinstance(task, dict)
                and isinstance(task.get("name"), str)
                and isinstance(task.get("completed"), bool)
            ):
                valid_tasks.append(task)

        return valid_tasks

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: tasks.json contains invalid JSON. Starting with an empty list.")
        return []
    except OSError as error:
        print(f"Could not read tasks.json: {error}")
        return []


def save_tasks(tasks):
    """Save the current tasks to tasks.json. Return True if successful."""
    try:
        with TASK_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True
    except OSError as error:
        print(f"Could not save tasks: {error}")
        return False


def add_task(tasks):
    """Ask for a task name and add it to the list."""
    name = input("Enter your task: ").strip()

    if not name:
        print("Task cannot be empty!")
        return

    tasks.append({"name": name, "completed": False})

    if save_tasks(tasks):
        print("Task added and saved successfully!")
    else:
        tasks.pop()


def view_tasks(tasks):
    """Display all tasks and their completion status."""
    if not tasks:
        print("Your task list is empty!")
        return

    print("\nYOUR TASKS:")
    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not completed"
        print(f"{number}. {task['name']}")
        print(f"Status: {status}")
        print("-------------------")


def choose_task(tasks, prompt):
    """Display task numbers and return a valid zero-based index, or None."""
    if not tasks:
        print("Your task list is empty!")
        return None

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task['name']}")

    try:
        selected = int(input(prompt))
    except ValueError:
        print("Please enter a valid number!")
        return None

    if not 1 <= selected <= len(tasks):
        print("Invalid task number!")
        return None

    return selected - 1


def complete_task(tasks):
    """Mark the selected task as completed."""
    index = choose_task(tasks, "Enter task number: ")
    if index is None:
        return

    previous_status = tasks[index]["completed"]
    tasks[index]["completed"] = True

    if save_tasks(tasks):
        print("Task marked as completed!")
    else:
        tasks[index]["completed"] = previous_status


def delete_task(tasks):
    """Delete the selected task."""
    index = choose_task(tasks, "Enter task number: ")
    if index is None:
        return

    deleted_task = tasks.pop(index)

    if save_tasks(tasks):
        print(f"{deleted_task['name']} has been deleted!")
    else:
        tasks.insert(index, deleted_task)


def main():
    """Run the application menu."""
    tasks = load_tasks()
    print("Welcome to My To-Do List!")
    print(f"Existing tasks loaded: {len(tasks)}")

    while True:
        print("\n===== MY TO-DO LIST =====")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using My To-Do List!")
            print("Your tasks are saved in tasks.json.")
            break
        else:
            print("Invalid choice! Select between 1 and 5.")


if __name__ == "__main__":
    main()
