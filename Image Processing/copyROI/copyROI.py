import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('testImage1.JPG')
print(img.shape)
img1=np.copy(img)
green_buggy=img1[45:69,37:61];
img=cv2.line(img, (36,0),(35,90),(0,0,0), thickness=1)
img=cv2.line(img, (61,0),(61,90),(0,0,0), thickness=1)
img=cv2.line(img, (0,69),(90,69),(0,0,0), thickness=1)
img=cv2.line(img, (0,45),(90,45),(0,0,0), thickness=1)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

plt.imshow(green_buggy, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

img1[18:42,37:61]=green_buggy;

plt.imshow(img1, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

