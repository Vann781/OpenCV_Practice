#to show a image first you have to make open cv read the image
#do same steps as before
import cv2
img = cv2.imread(r"A:\OpenCV_Practice\images\img (2).jpeg")
#readig is done 
#to show a image use function :  cv2.imshow("Window Name",pass the variable in which you stored image or you can pass the image path directly )
cv2.imshow("image",img)
#before running this code make sure that you should set a time limit , here time limit means when the image wil  pop up then for how much time it will be visible 
#after the time limit the image windw will close automatically
cv2.waitKey(0)       #here 3000 means 3000 ms = 3 sec our window will be visible to us for 3 sec   
#run the code and see the image for 3 sec

#### NOTE1 :  if you use cv2.waitKey(0) then there is no timelimit , 
 # to close the window press any key of keyboard
 # 
 # NOTE2 :  use cv2.destroyAllWindows() to close all the windows at once
 #to close particular windows at once use cv2.destroyWindow()

 #because when we usA:\OpenCV_Practice\images\img (2).jpege waitKey() this function only wait till any key is pressed it do not actually kill the or closes the window , 
    #when you press any key the window disappears but it is not closed it is still running in the background ,
  #so if you want to close the window then you have to use destroyAllWindows() or destroyWindow

cv2.destroyAllWindows()  #closes all opened windows
print("all windows closed")

# cv2.destroyWindow()     #closes particular window  #use this function to close particular window at once