import json
from task import Task

class Storage:
    FILE_NAME = "tasks.json"

    def load_tasks(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self, tasks):
        with open(self.FILE_NAME, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)
