# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter marks: "))
if(marks >= 90 and marks <= 100):
    print("Grade Ex")
elif(marks >=80 and marks < 90):
    print("Grade A")
elif(marks >=70 and marks < 80):
    print("Grade B")
elif(marks >=60 and marks < 70):
    print("Grade C")
elif(marks >=50 and marks < 60):
    print("Grade D")
else:
    print("Grade F")