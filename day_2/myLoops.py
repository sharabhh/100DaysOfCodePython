hobbies = ['read', 'workout', 'code', 'dogs']

for hobby in hobbies:
    print(hobby)
    if hobby == 'workout':
        print('do burpees right now')
    elif hobby == 'dogs':
        print('what about cats?')
        
        
# range has 3 parameters range(start, stop, step)  start is where to start 'not mandatory'. This is inclusive, stop is where to go not inclusive of it. step is how much to incement or decrement
for idx in range(1,10,1):
    print(idx)
    
    
# while loop
print('starting while loop here')
count = 5
while(count > 0):
    print(count)
    count -= 1
else:
    print("I'm outside while loop")