import cv2
import numpy as np

#level of intensity
bright = [110,140,170,200,230,255]

for b in bright:
    img = cv2.imread('misc/white.jpg') #load rgb image

    #Isolate the areas where the color is black(every channel=0) and white (every channel=255)
    black=np.where((img[:,:,0]==0) & (img[:,:,1]==0) & (img[:,:,2]==0))
    white=np.where((img[:,:,0]>200) & (img[:,:,1]>200) & (img[:,:,2]>200))

    #Turn black pixels to white and vice versa
    img[black]=(0,0,0)
    img[white]=(bright,bright,bright)


    cv2.imwrite("white_proced_b{}.jpg".format(b), img)