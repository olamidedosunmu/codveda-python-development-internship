"""Codveda Level 2 - To-Do List Application.

A command-line to-do list that supports adding, viewing, completing,
deleting, and permanently storing tasks in a JSON file.
"""

# json is used to read and write task information in JSON format.
import json

# Path helps build a file path that works across operating systems.
from pathlib import Path


# Keep tasks.json in the same folder as this Python program.
TASK_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load tasks from tasks.json. Return an empty list if it does not exist."""

    # Try to open the existing JSON file and convert its contents into Python data.
    try:
        with TASK_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        # The application expects the saved data to be a list of task dictionaries.
        if not isinstance(tasks, list):
            print("Warning: tasks.json does not contain a task list. Starting empty.")
            return []

        # Keep only entries that have the expected task name and completion status.
        # This prevents malformed records from causing errors in the menu.
        valid_tasks = []
        for task in tasks:
            if (
                isinstance(task, dict)
                and isinstance(task.get("name"), str)
                and isinstance(task.get("completed"), bool)
            ):
                valid_tasks.append(task)

        return valid_tasks

    # A first-time user may not have a tasks.json file yet, so start with an empty list.
    except FileNotFoundError:
        return []

    # Handle a file that exists but does not contain valid JSON.
    except json.JSONDecodeError:
        print("Warning: tasks.json contains invalid JSON. Starting with an empty list.")
        return []

    # Handle other file-reading problems, such as permission or disk errors.
    except OSError as error:
        print(f"Could not read tasks.json: {error}")
        return []


def save_tasks(tasks):
    """Save the current tasks to tasks.json. Return True if successful."""

    # Open the JSON file in write mode and save the full task list.
    try:
        with TASK_FILE.open("w", encoding="utf-8") as file:
            # indent=4 makes the JSON file easier for a person to read.
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True

    # Tell the user if the application cannot write to the file.
    except OSError as error:
        print(f"Could not save tasks: {error}")
        return False


def add_task(tasks):
    """Ask for a task name and add it to the list."""

    # strip() removes extra spaces from the beginning and end of the task name.
    name = input("Enter your task: ").strip()

    # Do not allow the user to add a blank task.
    if not name:
        print("Task cannot be empty!")
        return

    # Add a new dictionary to the list. Every new task starts as not completed.
    tasks.append({"name": name, "completed": False})

    # Save the updated list; undo the addition if saving fails.
    if save_tasks(tasks):
        print("Task added and saved successfully!")
    else:
        tasks.pop()


def view_tasks(tasks):
    """Display all tasks and their completion status."""

    # Give a message instead of trying to loop through an empty list.
    if not tasks:
        print("Your task list is empty!")
        return

    print("\nYOUR TASKS:")

    # enumerate() supplies a user-friendly task number starting from 1.
    for number, task in enumerate(tasks, start=1):
        # Convert the Boolean completion value into readable status text.
        status = "Completed" if task["completed"] else "Not completed"
        print(f"{number}. {task['name']}")
        print(f"Status: {status}")
        print("-------------------")


def choose_task(tasks, prompt):
    """Display task numbers and return a valid zero-based index, or None."""

    # There is no task to select if the list is empty.
    if not tasks:
        print("Your task list is empty!")
        return None

    # Display all available tasks with numbers beginning at 1.
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task['name']}")

    # Convert the user's selected task number from text to an integer.
    try:
        selected = int(input(prompt))
    except ValueError:
        # Handle input such as letters instead of a number.
        print("Please enter a valid number!")
        return None

    # Check that the selected number matches one of the displayed tasks.
    if not 1 <= selected <= len(tasks):
        print("Invalid task number!")
        return None

    # Python list positions start at zero, so subtract 1 from the displayed number.
    return selected - 1


def complete_task(tasks):
    """Mark the selected task as completed."""

    # Ask the user to choose a task and receive its list index.
    index = choose_task(tasks, "Enter task number: ")
    if index is None:
        return

    # Store the previous value so it can be restored if saving fails.
    previous_status = tasks[index]["completed"]

    # Change the selected task's completion status to True.
    tasks[index]["completed"] = True

    # Save the change; restore the old status if the file could not be updated.
    if save_tasks(tasks):
        print("Task marked as completed!")
    else:
        tasks[index]["completed"] = previous_status


def delete_task(tasks):
    """Delete the selected task."""

    # Ask the user to choose which task should be removed.
    index = choose_task(tasks, "Enter task number: ")
    if index is None:
        return

    # pop() removes the selected dictionary and returns it.
    deleted_task = tasks.pop(index)

    # Save the shorter list; put the task back if saving fails.
    if save_tasks(tasks):
        print(f"{deleted_task['name']} has been deleted!")
    else:
        tasks.insert(index, deleted_task)


def main():
    """Run the application menu."""

    # Load previously saved tasks when the application starts.
    tasks = load_tasks()
    print("Welcome to My To-Do List!")
    print(f"Existing tasks loaded: {len(tasks)}")

    # Keep showing the menu until the user chooses to exit.
    while True:
        print("\n===== MY TO-DO LIST =====")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        # Read the menu choice and remove any surrounding spaces.
        choice = input("Enter your choice: ").strip()

        # Call the function that matches the user's selection.
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
            break  # Stop the menu loop and end the program.
        else:
            # Handle any menu choice other than 1, 2, 3, 4, or 5.
            print("Invalid choice! Select between 1 and 5.")


# Run main() only when this file is executed directly, not when imported elsewhere.
if __name__ == "__main__":
    main()
