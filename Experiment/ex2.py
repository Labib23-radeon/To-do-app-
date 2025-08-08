user_prompt = "Enter whats your todo:"

todos = []
while True:
    todo= input(user_prompt)
    print(todo.title())
    todos.append(todo)
    print(todos)
    