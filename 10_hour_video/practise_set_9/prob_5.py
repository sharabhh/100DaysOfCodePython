# Repeat program 4 for a list of such words to be censored

cuss_list = ["fuckin", "shit", "bastard", "cunt", "bitch"]

with open("cuss_file.txt", "r") as f:
    content = f.read()

for word in cuss_list:
    content = content.replace(word, '*' * len(word))

with open("cuss_file.txt", "w") as f:
    f.write(content)