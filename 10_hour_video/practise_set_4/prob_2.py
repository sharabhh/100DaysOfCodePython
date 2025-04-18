# Write a program to accept marks of 6 students and display them in a sorted manner.

list = []
mark_1 = int(input("Enter first student marks: "))
list.append(mark_1)
mark_2 = int(input("Enter second student marks: "))
list.append(mark_2)
mark_3 = int(input("Enter third student marks: "))
list.append(mark_3)
mark_4 = int(input("Enter fourth student marks: "))
list.append(mark_4)
mark_5 = int(input("Enter fifth student marks: "))
list.append(mark_5)
mark_6 = int(input("Enter sixth student marks: "))
list.append(mark_6)
list.sort()
print("The marks are: ", list)