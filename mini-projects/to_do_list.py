
tasks = []

while True:
    task = input("Add task (or quit): ")

    if task == "quit":
        break

    tasks.append(task)

print("Tasks:", tasks)