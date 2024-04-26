tasks = []
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")
def display_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Quit")
    ch = input("Enter your choice: ")
    if ch == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif ch == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif ch == "3":
        display_tasks()
    elif ch == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
