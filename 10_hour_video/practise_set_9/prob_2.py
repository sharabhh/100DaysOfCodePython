import random

def game():
    rndNum = random.randint(1, 100)
    return rndNum

randomNumber = game()
def update_number():
    try:
        f = open("Hi-score.txt", "r")
        data = f.read()
        f.close()
        if data == "":
            highscore = 0
        else:
            highscore = int(data)
    except FileNotFoundError:
        highscore = 0
    
    if randomNumber > highscore:
        f = open("Hi-score.txt", "w")
        f.write(str(randomNumber))
        f.close()
        print("New High Score")
    else:
        print("No New High Score")

update_number()
print(randomNumber)