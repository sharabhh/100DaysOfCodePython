x = "a"
try:
    print(int(x))
except Exception as e:
    print(e)
finally:
    print("I am always exceuted")

# finally section is always executed even if gets an error form try except
# there are multiple types of except keywords like ValueError, IndexError etc
