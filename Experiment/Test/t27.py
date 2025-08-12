files = open("file.txt", "r")
content = files.read()
files.close()

num_char = len(content)
print("Number of characters:", num_char)