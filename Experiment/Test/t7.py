user_action = input("what will be you option? (USA/Italy/Germany): ")
match user_action:
    case "USA" | "United States":
        print("Hello, American!")
    case "Italy":
        print("Ciao, Italiano!")
    case "Germany":
        print("Hallo, Deutscher!")
    case exit:
        print("Exiting the program.")

