# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

dictionary = {
    "madad": "help",
    "pyaar": "love",
    "dost": "friend"
}
search_term = str(input("Enter a Hindi word to search for its English translation: "))
print(dictionary[search_term]); 