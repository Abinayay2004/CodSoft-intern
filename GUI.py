import json

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.description} [{status}]"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Added task: {description}")

    def update_task(self, index, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description
            print(f"Updated task {index + 1} to: {description}")
        else:
            print("Task not found.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task.description}")
        else:
            print("Task not found.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Completed task: {self.tasks[index].description}")
        else:
            print("Task not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [{'description': task.description, 'completed': task.completed} for task in self.tasks]
            json.dump(tasks_data, file)
            print(f"Tasks saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(data['description']) for data in tasks_data]
                for task, data in zip(self.tasks, tasks_data):
                    task.completed = data['completed']
                print(f"Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"No such file: {filename}")

def main():
    todo_list = ToDoList()
    filename = 'tasks.json'
    todo_list.load_from_file(filename)

    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. Update task")
        print("3. Remove task")
        print("4. Complete task")
        print("5. Display tasks")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            description = input("Enter new task description: ")
            todo_list.update_task(index, description)
        elif choice == '3':
            index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '4':
            index = int(input("Enter task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == '5':
            todo_list.display_tasks()
        elif choice == '6':
            todo_list.save_to_file(filename)
        elif choice == '7':
            todo_list.load_from_file(filename)
        elif choice == '8':
            todo_list.save_to_file(filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
