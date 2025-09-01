employees = []
while True:
    employee = input("Enter an employee's name:")
    employees.append(employee)
    for item in employees:
        print(item.capitalize())
        