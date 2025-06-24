#in this we will be removing grreen color 
import cv2
img = cv2.imread("A:\OpenCV_Practice\images\img (3).jpeg")
img_resized = cv2.resize(img, (600, 300))

#like if we want to access the image's only green color then we will use :
#img_resized[:, :, 1]  :  it access  the Green color of the image

#lets set it 0 : by setting it 0 our image will remove the blye component from it 

img_resized[:, :, 1] = 0
cv2.imshow("image without blue color", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("destroyed")