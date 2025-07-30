import json
from datetime import datetime

class TaskAgent:
    def __init__(self, data_file):
        self.data_file = data_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                return json.load(file)['tasks']
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump({'tasks': self.tasks}, file, indent=2, ensure_ascii=False)

    def suggest_priority(self, task):
        today = datetime.now().strftime('%Y-%m-%d')
        due_date = datetime.strptime(task['due'], '%Y-%m-%d')
        days_left = (due_date - datetime.now()).days
        if task['priority'] == 'high' or days_left <= 2:
            return f"Task '{task['title']}' is urgent, please complete it today!"
        return f"Task '{task['title']}' can be completed by {task['due']}."

    def add_task(self, title, priority, due):
        new_id = max([task['id'] for task in self.tasks], default=0) + 1
        new_task = {"id": new_id, "title": title, "priority": priority, "due": due}
        self.tasks.append(new_task)
        self.save_tasks()
