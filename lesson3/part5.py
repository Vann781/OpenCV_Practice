#lets set all colors == 0 
import cv2
img = cv2.imread("A:\OpenCV_Practice\images\img (3).jpeg")
img_resized = cv2.resize(img, (600, 300))

img_resized[:, :, 0] = 0
img_resized[:, :, 1] = 0
img_resized[:, :, 2] = 0
cv2.imshow("image without blue color", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("destroyed")


# OUTPUT---------->>> A BLACK image
