'''
Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.
'''


for i in range(2, 21):
    stringData = ""
    for j in range(1, 11):
        stringData += f"{i} * {j} = {i * j}\n"

    f = open(f"tables/table_of_{i}.txt", "w")
    f.write(stringData)
    f.write("\n")
    f.close()


print("Multiplication table of 2 to 20 generated successfully.")