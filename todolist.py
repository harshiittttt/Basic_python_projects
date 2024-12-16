def addtask(index, array):
    """Adds a task at the specified index in the task list."""
    if 0 <= index <= len(array):  # Ensure index is within bounds
        inputtask = input("Please enter your task: ")
        array.insert(index, inputtask)
        print(f"'{inputtask}' added successfully at index {index}.")
    else:
        print("Error: Invalid index. Task could not be added.")


def removetask(index, array):
    """Removes a task at the specified index in the task list."""
    if 0 <= index < len(array):  # Ensure index is valid for removal
        task = array.pop(index)
        print(f"'{task}' removed successfully from index {index}.")
    else:
        print("Error: Invalid index. No task removed.")


def displaytasks(array):
    """Displays the current tasks in the to-do list."""
    if len(array) == 0:
        print("There are no tasks.")
    else:
        print("\nCurrent To-Do List:")
        for i, task in enumerate(array):
            print(f"{i}: {task}")
    print()  # Add a blank line for better formatting


def main():
    """Main function to manage the to-do list."""
    print("Welcome to our To-Do List!")
    taskList = []

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            displaytasks(taskList)
            try:
                index = int(input("Enter the position to add the task (0-based index): "))
                addtask(index, taskList)
            except ValueError:
                print("Error: Please enter a valid number for the index.")

        elif choice == "2":
            displaytasks(taskList)
            if len(taskList) > 0:
                try:
                    index = int(input("Enter the position of the task to remove (0-based index): "))
                    removetask(index, taskList)
                except ValueError:
                    print("Error: Please enter a valid number for the index.")
            else:
                print("Error: No tasks to remove.")

        elif choice == "3":
            displaytasks(taskList)

        elif choice == "4":
            print("Thank you for using our program. Goodbye!")
            break  # Exit the loop

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
