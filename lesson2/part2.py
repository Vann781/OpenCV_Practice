#CHECKING IMAGE TYPE AND SHAPE 
import cv2
import numpy as np
# Load the image
img  = cv2.imread("A:\OpenCV_Practice\images\img (4).jpeg")
print("\n\ntype of image : ")
print(type(img))
print("\n\nshape of image : ")
print(img.shape)