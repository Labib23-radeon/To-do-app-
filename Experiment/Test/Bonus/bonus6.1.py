contents = ['jump like a frog', 'eat like a pig', 'sleep like a dog']
files = ['file1.txt', 'file2.txt', 'file3.txt']

for content, file1 in zip(contents, files):
    file = open(f"../file/{file1}", 'w')
    file.write(content)