import string
import random

x = int(input("Type '1' if you want to decode and '0' if want to encode: "))

# Here is the logic of coding
if x == 1:
    word = input("Enter the word to decode: ")
    if len(word) <= 3:
        word = word[::-1]
        print(word)
    else:
        lengthOfWord = len(word)
        useableWord = word[3:-3]
        lastLetter = useableWord[-1]
        useableWord = lastLetter + useableWord
        useableWord = useableWord[:-1]
        print(useableWord)
# Here is the logic for encoding
elif x == 0:
    # pass
    word = input("Enter the word to encode: ")
    if len(word) <= 3:
        word = word[::-1]
        print("Encoded word is:", word)
    else:
        firstLetter = word[0]
        word = word.replace(firstLetter, "")
        # print(word)
        word = word + firstLetter
        print(word)

        def randomLetterGenerator():
            list = []
            for i in range(3):
                list.append(random.choice(string.ascii_lowercase))

            return list

        randomletters = randomLetterGenerator()
        for i in randomletters:
            word = i + word + i

    print(word)
