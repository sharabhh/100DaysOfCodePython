# reading a file

# f = open("day_5/myfile.txt", 'r')
# text = f.read()
# print(text)
# f.close()

# writing in a file

# f = open("day_5/myfile.txt", "w")
# f.write(" Hello world")
# f.close()

# using with keyword

with open("day_5/myfile.txt", "a") as f:
    f.write(" final addition")