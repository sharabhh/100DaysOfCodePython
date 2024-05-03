# reading lines

# f = open("day_5/marks.txt", "r")
# i=0
# while True:
#     i=i+1
#     line = f.readline()
#     if not line:
#         break
#     # print(line.split(","))
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of student {i} in Maths is : {m1}")
#     print(f"Marks of student {i} in English is : {m2}")
#     print(f"Marks of student {i} in SST is : {m3}")


# writing files

f = open("day_5/marks.txt", "w")
lines = ["line 1\n", "line 2\n", "line 3\n"]
f.writelines(lines)
f.close()
