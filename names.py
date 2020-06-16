import os, glob

folder = "../Video1/video-to-test/"
print("doing")
with open ("darknet/data/train.txt","w") as f:
    for file in sorted(glob.glob(folder+"*.jpg")):
        # print(os.path.abspath(os.getcwd())+"/"+file+"\n")
        f.write(os.path.abspath(file)+"\n")

