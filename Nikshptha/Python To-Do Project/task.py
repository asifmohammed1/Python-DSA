class Task:
    def __init__(self, task_id, task_name, priority, due_date, status):
        self.task_id = task_id
        self.task_name = task_name
        self.priority = priority
        self.due_date = due_date
        self.status = status

    def display_task(self):
        print("Task ID :", self.task_id)
        print("Task Name :", self.task_name)
        print("Priority :", self.priority)
        print("Due Date :", self.due_date)
        print("Status :", self.status)

    def mark_completed(self):
        self.status = "Completed"

    def update_task(self, task_name, priority, due_date):
        self.task_name = task_name
        self.priority = priority
        self.due_date = due_date