import cv2 
import numpy as np
image=cv2.imread('RHN_2540 (1).jpg')

                         
		
HSV_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
YCbCr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
binary_mask_image = HSV_image
#================================================================================================================================


#================================================================================================================================
#Apply a threshold to an HSV and YCbCr images, the used values were based on current research papers along with some
# empirical tests and visual evaluation

lower_HSV_values = np.array([0, 40, 0], dtype = "uint8")
upper_HSV_values = np.array([25, 255, 255], dtype = "uint8")

lower_YCbCr_values = np.array((0, 138, 67), dtype = "uint8")
upper_YCbCr_values = np.array((255, 173, 133), dtype = "uint8")

#A binary mask is returned. White pixels (255) represent pixels that fall into the upper/lower.
mask_YCbCr = cv2.inRange(YCbCr_image, lower_YCbCr_values, upper_YCbCr_values)
mask_HSV = cv2.inRange(HSV_image, lower_HSV_values, upper_HSV_values) 

binary_mask_image = cv2.add(mask_HSV,mask_YCbCr)

#================================================================================================================================
#Function that applies Watershed and morphological operations on the thresholded image
	
#morphological operations
image_foreground = cv2.erode(binary_mask_image,None,iterations = 3)     	#remove noise
dilated_binary_image = cv2.dilate(binary_mask_image,None,iterations = 3)   #The background region is reduced a little because of the dilate operation
ret,image_background = cv2.threshold(dilated_binary_image,1,128,cv2.THRESH_BINARY)  #set all background regions to 128

image_marker = cv2.add(image_foreground,image_background)   #add both foreground and backgroud, forming markers. The markers are "seeds" of the future image regions.
image_marker32 = np.int32(image_marker) #convert to 32SC1 format

cv2.watershed(image,image_marker32)
m = cv2.convertScaleAbs(image_marker32) #convert back to uint8 

#bitwise of the mask with the input image
ret,image_mask = cv2.threshold(m,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
output = cv2.bitwise_and(image,image,mask = image_mask)
		
#show the images

#================================================================================================================================
def show_image(image):
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyWindow("Image")
#================================================================================================================================
#show_image(image)
show_image(image_mask)
#show_image(output)
