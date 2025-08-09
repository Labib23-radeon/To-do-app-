filenames = ["1.raw data.txt", "2.raw data.txt", "3.raw data.txt", "4.raw data.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)