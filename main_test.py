import unittest
import json
from datetime import datetime


from main import ToDoListManager

class TestToDoListManager(unittest.TestCase):
    def setUp(self):
        self.todo_manager = ToDoListManager()

    def test_add_task(self):
        self.todo_manager.add_task("Test Task")
        self.assertEqual(len(self.todo_manager.tasks), 1)

    def test_remove_task(self):
        self.todo_manager.add_task("Test Task")
        self.todo_manager.remove_task(0)
        self.assertEqual(len(self.todo_manager.tasks), 0)

    def test_mark_as_done(self):
        self.todo_manager.add_task("Test Task")
        self.todo_manager.mark_as_done(0)
        self.assertTrue(self.todo_manager.tasks[0]['done'])

    def test_view_all_tasks(self):
        self.todo_manager.add_task("Test Task 1")
        self.todo_manager.add_task("Test Task 2")
        self.assertEqual(self.todo_manager.view_all_tasks(), "All Tasks:\n1. Test Task 1 - Pending - Due Date: No due date\n2. Test Task 2 - Pending - Due Date: No due date")

    def test_view_pending_tasks(self):
        self.todo_manager.add_task("Test Task 1")
        self.todo_manager.add_task("Test Task 2")
        self.todo_manager.mark_as_done(0)
        self.assertEqual(self.todo_manager.view_pending_tasks(), "Pending Tasks:\n2. Test Task 2 - Pending - Due Date: No due date")

    def test_view_completed_tasks(self):
        self.todo_manager.add_task("Test Task 1")
        self.todo_manager.add_task("Test Task 2")
        self.todo_manager.mark_as_done(0)
        self.assertEqual(self.todo_manager.view_completed_tasks(), "Completed Tasks:\n1. Test Task 1 - Done - Due Date: No due date")

    def test_set_due_date(self):
        self.todo_manager.add_task("Test Task")
        self.todo_manager.set_due_date(0, "2023-01-15")
        self.assertEqual(self.todo_manager.tasks[0]['due_date'], "2023-01-15")

    def test_search_tasks(self):
        self.todo_manager.add_task("Test Task 1")
        self.todo_manager.add_task("Test Task 2")
        self.assertEqual(self.todo_manager.search_tasks("task"), "Tasks matching 'task':\n1. Test Task 1 - Pending - Due Date: No due date\n2. Test Task 2 - Pending - Due Date: No due date")

    def test_save_and_load_tasks(self):
        self.todo_manager.add_task("Test Task 1")
        self.todo_manager.add_task("Test Task 2")
        self.todo_manager.save_tasks_to_file("test_tasks.json")

        # Clear tasks
        self.todo_manager.tasks = []

        self.todo_manager.load_tasks_from_file("test_tasks.json")
        self.assertEqual(len(self.todo_manager.tasks), 2)


if __name__ == '__main__':
    unittest.main()
