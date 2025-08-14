filenames = ["main.py", "bonus7.1.py"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)