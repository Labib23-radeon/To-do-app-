files = open("easy.txt", "r")
content = files.read()
files.close()
print(content.title())
