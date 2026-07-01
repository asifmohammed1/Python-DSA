from task import Task

class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task_id = len(self.tasks) + 1

        task_name = input("Enter Task Name: ")
        priority = input("Enter Priority (High/Medium/Low): ")
        due_date = input("Enter Due Date (DD-MM-YYYY): ")

        task = Task(
            task_id,
            task_name,
            priority,
            due_date,
            "Pending"
        )

        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):

        if len(self.tasks) == 0:
            print("No tasks available.")
            return

        for task in self.tasks:
            task.display_task()
            print("----------------------")

    def search_task(self):

        search_id = int(input("Enter Task ID to search: "))

        for task in self.tasks:
            if task.task_id == search_id:
                task.display_task()
                return
        print("Task not found.")

    def update_task(self):

        search_id = int(input("Enter Task ID to update: "))

        for task in self.tasks:

            if task.task_id == search_id:
                new_name = input("Enter New Task Name: ")
                new_priority = input("Enter New Priority: ")
                new_due_date = input("Enter New Due Date: ")

                task.update_task(
                    new_name,
                    new_priority,
                    new_due_date
                )
                print("Task updated successfully!")
                return
        print("Task not found.")

    def mark_completed(self):

        search_id = int(input("Enter Task ID to mark as completed: "))

        for task in self.tasks:
            if task.task_id == search_id:
                if task.status == "Completed":
                    print("Task is already completed.")
                else:
                    task.mark_completed()
                    print("Task marked as completed!")
                return
        print("Task not found.")

    def delete_task(self):

        search_id = int(input("Enter Task ID to delete: "))

        for task in self.tasks:
            if task.task_id == search_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found.")

    def pending_tasks(self):

        print("Pending Tasks:")

        for task in self.tasks:
            if task.status == "Pending":
                task.display_task()
                print(" ")

    def completed_tasks(self):
        print("Completed tasks:")

        for task in self.tasks:
            if task.status == "Completed":
                task.display_task()
                print("")

    def menu(self):
        while True:
            print("\n===== TO-DO LIST =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Search Task")
            print("4. Update Task")
            print("5. Mark as Completed")
            print("6. Delete Task")
            print("7. View Pending Tasks")
            print("8. View Completed Tasks")
            print("9. Exit")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                self.search_task()
            elif choice == 4:
                self.update_task()
            elif choice == 5:
                self.mark_completed()
            elif choice == 6:
                self.delete_task()
            elif choice == 7:
                self.pending_tasks()
            elif choice == 8:
                self.completed_tasks()
            elif choice == 9:
                print("Thank you for using To-Do List Manager!")
                break
            else:
                print("Invalid choice! Please try again.")