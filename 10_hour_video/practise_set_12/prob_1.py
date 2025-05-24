# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

with (open("text_files/text1.txt") as f1, open("text_files/text2.txt") as f2, open("text_files/text33.txt") as f3):
    try:
        result1 = f1.read()
        result2 = f2.read()
        result3 = f3.read()
        print("all files exist")
    except FileNotFoundError as e:
        print(e)