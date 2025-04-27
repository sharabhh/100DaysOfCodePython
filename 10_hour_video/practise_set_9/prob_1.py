'''
Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.
'''

f = open("poems.txt", "r")
data = f.read()
def find_word(word):
    if word in data:
        return True
    else:
        return False
bool = find_word("twinkle")
f.close()
print(bool)