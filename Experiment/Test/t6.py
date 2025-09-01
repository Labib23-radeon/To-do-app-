members = []
while True:
    member = input("Enter a member's name: ")
    members.append(member)
    for item in members:
        print(item.capitalize())