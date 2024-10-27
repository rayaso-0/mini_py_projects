# To-Do List
# Sun, Oct 27, 2024
import os
import json

FILE_PATH = os.path.join(os.path.dirname(__file__), "tasks.json")

def load_tasks():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("tasks.json not found, starting with an empty task list.")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    try:
        with open(FILE_PATH, "w") as file:
            json.dump(tasks, file)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Mark Task as Completed")
    print("5. Save and Exit")

def add_task(tasks):
    task_name = input("Enter task: ")
    tasks.append({"\ntask": task_name, "completed": False})
    print(f"\nTask '{task_name}' added.")
    
def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
        return
    for i, task in enumerate(tasks, start=1):
        task_name = task.get("task", "Unnamed Task")
        status = "✓" if task.get("completed", False) else "✗"
        print(f"{i}. {task_name} [{status}]")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the number of the task to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"\nTask '{removed_task['task']}' deleted.")
    else:
        print("\nInvalid task number.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the number of the task to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        print(f"\nTask '{tasks[task_num]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_completed(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("\nTasks saved. Exiting.")
            break
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()