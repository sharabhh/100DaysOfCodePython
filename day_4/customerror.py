a = int(input('Enter any number between 5 and 9: '))

if( a<5 or a>9):
    raise ValueError("Incorrect value")
else:
    print("The number is:", a)