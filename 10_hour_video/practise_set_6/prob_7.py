# Write a program to find out whether a given post is talking about “Harry” or not.
post = str(input("Enter the post: "))

if(post.find("Harry") == -1):
    print("Post does not contain Harry")
else:
    print("Post contains Harry")