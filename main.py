from task_manager import TaskManager

def main():
    task_manager = TaskManager()

    print("Task Manager CLI")
    print("Available commands: add, list, complete, delete, exit")
    
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == "add":
            task = input("Enter task description: ")
            task_manager.add_task(task)
        elif command == "list":
            task_manager.list_tasks()
        elif command == "complete":
            task_id = int(input("Enter task ID to complete: "))
            task_manager.complete_task(task_id)
        elif command == "delete":
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif command == "exit":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
