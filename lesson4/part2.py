#how to show multiple images in a window 
# our desired output ----->>>>>>>     [Image1][Image2][IMage3]

#imprt numpy and cv2
import numpy as np
import cv2

# load the images
img1 = cv2.imread("A:\OpenCV_Practice\images\img (2).jpeg")
r_img1= cv2.resize(img1,(200,200))
img2 = cv2.imread("A:\OpenCV_Practice\images\img (3).jpeg")
r_img2= cv2.resize(img2,(200,200))
img3 = cv2.imread("A:\OpenCV_Practice\images\img (1).jpg")
r_img3= cv2.resize(img3,(200,200))

#when the resolution of images combine is higher than size of window it will show value error
#error : ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 1600 and the array at index 1 has size 1200
    

# show the images
new_img = np.vstack((r_img1,r_img2,r_img3))        #  np.hstack is the function of numoy which is used to store things in horizotal format ; h represnt horizontal
cv2.imshow("threee images in one ", new_img)
cv2.waitKey(0)

  

cv2.destroyAllWindows()
print("destroyed")