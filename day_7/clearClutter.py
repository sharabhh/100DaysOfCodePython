# Challenge #7
import os

folderPath = "day_7/wallpapers"

if(os.path.exists(f"{folderPath}")):
    files = os.listdir(f"{folderPath}")
    # print(files)    #type is list

    length = []
    number = 1
    for index,file in enumerate(files):
        # print(file)
        if(file.endswith(".jpg")):
            os.rename(f"{folderPath}/{file}",f"{folderPath}/{number}.jpg")
            number+=1
            length.append(file)
            print(file)
        print(len(length))
        print(files)
    print("exists")
else:
    print("specified path doesn't exist.")