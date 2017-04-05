#interchanging Red and Blue colors
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('testImage1.jpg');
img1=np.copy(img);  #output image
x=25;
y=58;

#drawing a circle around a point and printing its BGR value.
#cv2.circle(img,(x,y),5,(255,255,255),2);
print(img[y,x])
print(img.shape);
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        
        #checking range of blue and green pixel values
        if img[i][j][0]>100 and img[i][j][1]<120: 
            img1[i][j][0]=0;
            img1[i][j][2]=190;
        #checking range of red and green pixel values
        if img[i][j][2]>100 and img[i][j][1]<120: 
            img1[i][j][2]=0;
            img1[i][j][0]=190;

#cv2.imshow('window1',img1);
#cv2.imshow('window2',img);
#cv2.waitKey(0);
plt.imshow(img1, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
