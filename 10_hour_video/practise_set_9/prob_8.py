# Write a program to make a copy of a text file “this. txt”

with open("copy_file/original.txt", "r") as f:
    content = f.read()

with open("copy_file/copy_of_original.txt", "x") as f:
    f.write(content)

print(content)