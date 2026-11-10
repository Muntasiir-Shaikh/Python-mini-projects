
tasks = []

print("Welcome to My Todo List")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks available")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task)

    elif choice == "3":
        print("Thank you for using Todo List!")
        break

    else:
        print("Invalid choice!")
