todos = []

while True:

    user_action = input("Type add, show, edit, complete or exit todo:")
    user_action = user_action.strip()
    
    match user_action:
        case "add":
            todo = input("Enter your todo:")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case "edit":
            number = int(input("Enter the number of the todo to edit:"))
            number = number -1 
            new_todo = input("Enter the new todo:")
            todos[number] = new_todo
            print("Todo updated successfully.")
        case "complete":
            number = int(input("Enter the number of the todo to complete:"))
            number = number - 1
            todos.pop(number)
            print("Todo completed successfully.")
        case "exit":
            break
print("Goodbye!")
    
    