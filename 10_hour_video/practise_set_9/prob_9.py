# Write a program to find out whether a file is identical & matches the content of
# another file.

with open("copy_file/original.txt", "r") as f:
    content = f.read()

with open("copy_file/copy_of_original.txt", "r") as f:
    content2 = f.read()

if content == content2:
    print("identical files")
else:
    print("different files")