with open("day_6/text.txt", "r") as f:
    # seek takes the cursor to that number of character
    f.seek(10)

    # tells the position of the cursor
    print(f.tell())
    print(f.read(5))

with open("day_6/truncate.txt", "w") as t:
    t.write("Hello, I am a truncate method")
    # truncate makes the file size to whatever is specified inside it. i.e. 10 characters here
    t.truncate(10)
