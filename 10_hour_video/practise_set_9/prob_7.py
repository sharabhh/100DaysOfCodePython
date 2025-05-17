# Write a program to find out the line number where python is present from ques 6.
word = "python"

with open("log.txt", "r") as f:
    lines = f.readlines()
    lineNo = 1
for line in lines:
    if word in line:
        print(f"{word} is present in line number: {lineNo}")
        break

    lineNo += 1

else:
    print(f"{word} is not present")
# print(content[1])