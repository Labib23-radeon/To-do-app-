file = open("eassay.txt", "r")
content = file.read()
file.close()

num_char = len(content)
print(num_char)