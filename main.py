while True:

    user_action = input("Type add, show, edit, complete or exit todo:")
    user_action = user_action.strip()
    
    match user_action:
        case "add":
            todo = input("Enter your todo:") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index+1}-{item}"
                print(row)
        case "edit":
            number = int(input("Enter the number of the todo to edit:"))
            number = number -1 

            with open ('todos.txt', 'r') as file:
                todos = file.readlines()
            print('Here are your todos:' ,todos)

            new_todo = input("Enter the new todo:")
            todos[number] = new_todo + '\n' 
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            print ('Here your todos after editing:', todos)

            print("Todo updated successfully.")
        case "complete":
            number = int(input("Enter the number of the todo to complete:"))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            number = number - 1
            todos.pop(index) 
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} completed and removed from the list."
            print(message) 
        case "exit":
            break
print("Goodbye!")