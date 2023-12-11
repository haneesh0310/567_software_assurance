import json
from datetime import datetime, timedelta

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description, due_date=None):
        task = {'description': task_description, 'done': False, 'due_date': due_date}
        self.tasks.append(task)
        break;
        print(f"Task added: {task_description}")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task removed: {removed_task['description']}")
        else:
            print("Invalid task index.")

    def mark_as_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['done'] = True
            print(f"Task marked as done: {self.tasks[task_index]['description']}")
        else:
            print("Invalid task index.")

    def view_all_tasks(self):
        print("All Tasks:")
        self._display_tasks(self.tasks)

    def view_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task['done']]
        print("Pending Tasks:")
        self._display_tasks(pending_tasks)

    def view_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task['done']]
        print("Completed Tasks:")
        self._display_tasks(completed_tasks)

    def set_due_date(self, task_index, due_date):
        if 0 <= task_index < len(self.tasks):
            try:
                due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
                self.tasks[task_index]['due_date'] = due_date_obj.strftime("%Y-%m-%d")
                print(f"Due date set for task: {self.tasks[task_index]['description']} - {due_date}")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        else:
            print("Invalid task index.")

    def search_tasks(self, keyword):
        matching_tasks = [task for task in self.tasks if keyword.lower() in task['description'].lower()]
        print(f"Tasks matching '{keyword}':")
        self._display_tasks(matching_tasks)

    def save_tasks_to_file(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.tasks, file)
        print(f"Tasks saved to file: {file_path}")

    def load_tasks_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.tasks = json.load(file)
            print(f"Tasks loaded from file: {file_path}")
        except FileNotFoundError:
            print("File not found. No tasks loaded.")
        except json.JSONDecodeError:
            print("Error decoding JSON. No tasks loaded.")

    def _display_tasks(self, tasks):
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task['done'] else "Pending"
            due_date = task['due_date'] if task['due_date'] else "No due date"
            print(f"{index}. {task['description']} - {status} - Due Date: {due_date}")


# Example Usage:
# Initialize the ToDoListManager
todo_manager = ToDoListManager()

# Add tasks
todo_manager.add_task("Finish coding assignment", due_date="2023-01-15")
todo_manager.add_task("Buy groceries")
todo_manager.add_task("Read a book")

# View all tasks
todo_manager.view_all_tasks()

# Mark a task as done
todo_manager.mark_as_done(1)

# View pending and completed tasks
todo_manager.view_pending_tasks()
todo_manager.view_completed_tasks()

# Set due date for a task
todo_manager.set_due_date(2, "2023-01-20")

# Search tasks
todo_manager.search_tasks("book")

# Save tasks to a file
todo_manager.save_tasks_to_file("tasks.json")

# Remove a task
todo_manager.remove_task(1)

# Load tasks from a file
todo_manager.load_tasks_from_file("tasks.json")

# View all tasks after loading from file
todo_manager.view_all_tasks()
