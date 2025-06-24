#lets compare all the images we generated oin lesson 3 those without colors
import cv2
import numpy as np
img = cv2.imread("A:\OpenCV_Practice\images\img (3).jpeg")
img_resized = cv2.resize(img, (300, 300))
imgBLUE=img_resized[:, :, 0] 
imGren=img_resized[:, :, 2] 
imgRED=img_resized[:, :, 1] 
new_img = np.hstack((imgBLUE,imGren,imgRED))  
cv2.imshow("differece",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("destroyed")