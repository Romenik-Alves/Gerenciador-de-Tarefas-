import json

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            self.save_tasks()

    def show_tasks(self):
        for index, task in enumerate(self.tasks):
            status = '✓' if task['completed'] else '✗'
            print(f"{index}: [{status}] {task['task']}")

def main():
    manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Complete Task\n4. Show Tasks\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            manager.add_task(task)
        elif choice == '2':
            index = int(input("Enter task index to remove: "))
            manager.remove_task(index)
        elif choice == '3':
            index = int(input("Enter task index to complete: "))
            manager.complete_task(index)
        elif choice == '4':
            manager.show_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()