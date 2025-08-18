date = input("Enter the date (YYYY-MM-DD): ")
mood = input("Enter your mood today rated from 1 to 10: ")
thoughts = input("Write your journal entry:\n ")

with open("../journal/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)