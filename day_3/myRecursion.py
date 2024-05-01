# factorial

# def factorial(n):
#     if (n==1 or n==0):
#         return 1
#     return n * factorial(n-1)

# x = int(input("Enter the number: "))
# print(factorial(x)) 


# fibonacci sequence

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1 or n==2):
        return 1   
 
    return fibonacci(n-1) + fibonacci(n-2)

# list = [0,1]

x = int(input("Enter the length of fibonacci sequence: ")) 
print(fibonacci(x))
