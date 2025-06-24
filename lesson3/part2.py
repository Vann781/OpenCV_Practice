#here we will we using different things which will really be interestng
import cv2
img = cv2.imread("A:\OpenCV_Practice\images\img (3).jpeg")
img_resized = cv2.resize(img, (600, 300))

#if we want our image to be seen have colors of our defined properties 
#like if we want to access the image with only blue color then we will use :
#img_resized[:, :, 0]  :  it access  the blue color of the image

#lets set it 0 : by setting it 0 our image will remove the blye component from it 

img_resized[:, :, 0] = 0
cv2.imshow("image without blue color", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("destroyed")