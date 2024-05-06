import random

print("Choose your move: \n 1. for Rock\n 2. for Scissor\n 3. for Paper\n")
userInput = int(input("Enter your choice:"))

if(userInput <1 or userInput > 3):
    raise ValueError("Please select a value from the following")
else:
    # computerChoice = random.randrange(1,4)
    computerChoice = random.randrange(0,3)
    print("Computer choice is: ",computerChoice+1)

    matrix = [[0,-1,1], [1,0,-1], [-1,1,0]]
    # print(matrix)

    # computerMove = matrix[computerChoice][userInput]

    if(matrix[computerChoice][userInput-1] == 0):
        print("It's a draw")
    elif(matrix[computerChoice][userInput-1] == 1):
        print("you lost")
    elif(matrix[computerChoice][userInput-1] == -1):
        print("You won!")

    # for computer 0 is rock, 1 is paper, 2 is scissor

    # How the matrix should function
    #     R  P  S
    # R   0 -1  1
    # P   1  0 -1
    # S  -1  1  0