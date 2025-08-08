todos = []

while True:

    user_action = input("Type add, show or exit todo:")
    user_action = user_action.strip()
    
    match user_action:
        case "add":
            todo = input("Enter your todo:")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                print(item)
        case "exit":
            break
        case whatever:
            print("Hey, you entered wrong command")

print("Goodbye!")
    
    