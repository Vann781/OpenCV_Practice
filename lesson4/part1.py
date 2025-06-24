#how to show multiple images 

#imprt numpy and cv2
import numpy as np
import cv2

# load the images
img1 = cv2.imread("A:\OpenCV_Practice\images\img (2).jpeg")
img2 = cv2.imread("A:\OpenCV_Practice\images\img (3).jpeg")
img3 = cv2.imread("A:\OpenCV_Practice\images\img (1).jpg")

# show the images
cv2.imshow("Image1", img1)
cv2.imshow("Image2", img2)
cv2.imshow("Image3", img3)
cv2.waitKey(0)
  

cv2.destroyAllWindows()
print("destroyed")