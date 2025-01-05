from task import Task
from storage import Storage

class TaskManager:
    def __init__(self):
        self.storage = Storage()
        self.tasks = self.storage.load_tasks()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        print("Task added.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "✓" if task.completed else "✗"
                print(f"{idx}. {task.description} [{status}]")

    def complete_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            self.tasks[task_id - 1].completed = True
            self.storage.save_tasks(self.tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task ID.")

    def delete_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            self.tasks.pop(task_id - 1)
            self.storage.save_tasks(self.tasks)
            print("Task deleted.")
        else:
            print("Invalid task ID.")
