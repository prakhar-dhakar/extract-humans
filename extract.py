import json
import cv2
import matplotlib.pyplot as plt

data = json.load(open("darknet/result.json"))

# data

hid=0
for i in data:
    image_name = i['filename'].split("/")[-1]
    # print(image_name)
    objects = i['objects']
    img = cv2.imread("testingimages/"+image_name)
    height_img = img.shape[0]
    width_img = img.shape[1]
    for j in objects:
        if(j['class_id']==0):
            centerx = j['relative_coordinates']['center_x']
            centery = j['relative_coordinates']['center_y']
            width_box = min(1.0,j['relative_coordinates']['width'])
            height_box = min(1.0,j['relative_coordinates']['height'])
            leftx = max(0,int((centerx - width_box/2)*width_img))
            rightx = max(int((centerx + width_box/2)*width_img),0)
            lefty = max(int((centery - height_box/2)*height_img),0)
            righty = max(int((centery + height_box/2)*height_img),0)
            if (img[lefty:righty, leftx:rightx].shape[0]<=10 or img[lefty:righty, leftx:rightx].shape[1]<=10) or (width_box)>0.8 :
                continue
            else:
    #             print(leftx,rightx,lefty,righty)
                crop_img = img[lefty:righty, leftx:rightx].copy()  
#                 print((img[lefty:righty, leftx:rightx]).shape)  
                # print(hid,(img[lefty:righty, leftx:rightx]).shape, leftx,rightx,lefty,righty)
    #             plt.imshow(crop_img)
    #             cv2.imwrite("Objects/"+image_name.split(".")[0]+"h"+str(hid)+".jpg",crop_img)            
                cv2.imwrite("Objects/V1-"+ "{:06d}".format(hid) + '.jpg',crop_img) 
                hid+=1
    
            
            
                        