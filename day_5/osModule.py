import os

if(not os.path.exists("day_5/data")):
    print("data is being created")
    os.mkdir(f"day_5/data")

for i in range(100):
    os.mkdir(f"day_5/data/Day {i+1}")
    os.rename(f"day_5/data/Day {i+1}", f"day_5/data/Tutorial {i+1}")


# This will list all of the files
folders = os.listdir("day_5/data")
for folder in folders:
    print(os.listdir(f"day_5/data/{folder}"))
    