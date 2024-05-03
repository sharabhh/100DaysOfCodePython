import time

x = int(time.strftime("%H"))
print(x)

if x > 0 and x <= 12:
    print("it's morning")
elif x > 12 and x <= 15:
    print("it's afternoon")
elif x > 15 and x <= 19:
    print("it's evening")
else:
    print("i's night")
