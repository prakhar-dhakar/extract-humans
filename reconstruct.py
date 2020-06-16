import json
import cv2
import matplotlib.pyplot as plt

data = json.load(open("darknet/result.json"))


hid=0
alpha=0.5
for i in data:
    image_name = i['filename'].split("/")[-1]
    # print(image_name)
    objects = i['objects']
    im = cv2.imread("testingimages/"+image_name)
    img= im.copy()
#     plt.imshow(img)
    height_img = img.shape[0]
    width_img = img.shape[1]
    for j in objects:
        if(j['class_id']==0):
            img2 = cv2.imread("poses/"+ "{:06d}".format(hid) + '.jpg')
            centerx = j['relative_coordinates']['center_x']
            centery = j['relative_coordinates']['center_y']
            width_box = min(1.0,j['relative_coordinates']['width'])
            height_box = min(1.0,j['relative_coordinates']['height'])            
            leftx = max(0,int((centerx - width_box/2)*width_img))
            rightx = max(int((centerx + width_box/2)*width_img),0)
            lefty = max(int((centery - height_box/2)*height_img),0)
            righty = max(int((centery + height_box/2)*height_img),0)
            background = img[lefty:righty, leftx:rightx].copy()
            # print((img[lefty:righty, leftx:rightx]).shape) 
#             print(img2.shape)
            if (img[lefty:righty, leftx:rightx].shape[0]<=10 or img[lefty:righty, leftx:rightx].shape[1]<=10) or (width_box)>0.8 :
                continue
            else:
                # print(background.shape,img2.shape)
                overlay=cv2.addWeighted(background,1-alpha,img2,alpha,0)                
                img[lefty:righty, leftx:rightx] = overlay
    #             plt.imshow(crop_img)
    #             cv2.imwrite("Objects/"+image_name.split(".")[0]+"h"+str(hid)+".jpg",crop_img)            
                cv2.imwrite("Output/"+ image_name.split(".")[0] +"recon-trans.jpg",img) 
                hid+=1
    
            
            
                        