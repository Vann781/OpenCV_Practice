#convert a image into gray scale /gray color 
import cv2
img = cv2.imread("A:\OpenCV_Practice\images\img (3).jpeg")
img_resized = cv2.resize(img, (600, 300))
gray_image = cv2.cvtColor(img_resized,cv2.COLOR_BGR2GRAY)            # use these funtion convert image into gray scale "" cv2.cvtColor(Variable name,cv2.COLOR_BGR2GRAY)  ""
cv2.imshow("Gray Image",gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows
print("destoryed")