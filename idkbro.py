import os
from PIL import Image

def convdel(path, FolderName):
    print("path for the folder", path)

    conv=0
    length = len(os.listdir(path))
    item = os.listdir(path)



    for i in range(length):                                          
        index = item[i].split(".")
        if index[1] == "webp":
            intended_word = (path+item[i])
            im= Image.open(path+item[i]).convert("RGB")
            im.save(path+index[0]+".png","png")
            os.remove(intended_word)
            conv+=1


    if conv==1:                                                       #prints the number of converted files 
        print("Converted",1,"File")
    elif conv==0:
        print("No Changes were made")
    else:
        print("Converted",conv," Files")    