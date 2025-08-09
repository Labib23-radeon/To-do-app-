todos = []

while True:

    user_action = input("Type add, show, edit or exit todo:")
    user_action = user_action.strip()
    
    match user_action:
        case "add":
            todo = input("Enter your todo:")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = int(input("Enter the number of the todo to edit:"))
            number = number -1 
            new_todo = input("Enter the new todo:")
            todos[number] = new_todo
            print("Todo updated successfully.")
        case "exit":
            break
print("Goodbye!")
    
    