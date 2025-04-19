# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

subject1 = int(input("Enter marks of subject 1: "))
subject2 = int(input("Enter marks of subject 2: "))
subject3 = int(input("Enter marks of subject 3: "))

avg_percent = ((subject1 + subject2 + subject3) / 3) *100
subject1_percent = (subject1 / 100) * 100
subject2_percent = (subject2 / 100) * 100
subject3_percent = (subject3 / 100) * 100

if((avg_percent >= 40) and (subject1_percent >= 33) and (subject2_percent >= 33) and (subject3_percent >= 33)):
    print("You have passed")
else:
    print("You have failed")