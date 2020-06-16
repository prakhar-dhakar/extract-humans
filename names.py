import os, glob

folder = "testingimages/"
print("doing")
with open ("darknet/data/train.txt","w") as f:
    for file in sorted(glob.glob(folder+"*.jpg")):
        # print(os.path.abspath(os.getcwd())+"/"+file+"\n")
        f.write(os.path.abspath(file)+"\n")

