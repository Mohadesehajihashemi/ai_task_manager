from models.agent import TaskAgent

agent = TaskAgent('data/tasks.json')

print("=== AI Task Manager ===")
print("Current Tasks:")
for task in agent.tasks:
    suggestion = agent.suggest_priority(task)
    print(f"- {task['title']} (Priority: {task['priority']}, Due: {task['due']}) - Suggestion: {suggestion}")

print("\nUrgent Reminders:")
for task in agent.tasks:
    if "urgent" in agent.suggest_priority(task):
        print(f"- {task['title']} requires immediate attention!")

while True:
    action = input("\nEnter 'add' to add a task, 'exit' to quit: ").strip().lower()
    if action == 'exit':
        print("Goodbye!")
        break
    elif action == 'add':
        try:
            title = input("Task title: ").strip()
            priority = input("Priority (high/medium/low): ").strip().lower()
            if priority not in ['high', 'medium', 'low']:
                print("Invalid priority! Please use 'high', 'medium', or 'low'.")
                continue
            due = input("Due date (e.g., 2025-08-01): ").strip()
            try:
                datetime.strptime(due, '%Y-%m-%d')  # چک کردن فرمت تاریخ
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD (e.g., 2025-08-01).")
                continue
            agent.add_task(title, priority, due)
            print(f"Task '{title}' added!")
            print("\nUpdated Tasks:")
            for task in agent.tasks:
                suggestion = agent.suggest_priority(task)
                print(f"- {task['title']} (Priority: {task['priority']}, Due: {task['due']}) - Suggestion: {suggestion}")
        except Exception as e:
            print(f"Error adding task: {e}")
    else:
        print("Invalid command! Use 'add' or 'exit'.")
