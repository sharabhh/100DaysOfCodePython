# Write a program to mine a log file and find out whether it contains ‘python’.

word = "python"

with open("log.txt", "r") as f:
    content = f.read()

if word in content:
    print("python is present")
else:
    print("python is not present")
