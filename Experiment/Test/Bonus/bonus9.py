password = input("Enter the password:")

result = {}

if len(password) >=8:
    result["length"] = True
else:
    result["length"] = False
    digit = False
    for i in password:
        if i.isdigit():
            digit = True
result["digits"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True
result["upper-case"] = upper

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password") 