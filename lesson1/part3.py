# RESIZE THE Image
# Resize the image to the specified size
#sometimes the image that we open is too big to fit in the window for that we use a funtion : cv2.resize(image_variable,(width,height))
import cv2
img = cv2.imread("A:\OpenCV_Practice\images\img (3).jpeg")
resized_img=cv2.resize(img,(600,300))
cv2.imshow("resized_img",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows
print("all windows closed")