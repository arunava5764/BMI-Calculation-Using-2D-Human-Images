import cv2
import numpy as np
def func(effect,x,y,flag,para):
    if effect==cv2.EVENT_LBUTTONDOWN:
        cv2.line(img,(x,y),(x,y),(0,0,176),5)
        cv2.putText(img,str(x)+","+str(y),(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,176),2)
        cv2.imshow("window",img)
img=cv2.imread("ANKITA_SIDE_EDIT.jpg",1)
img=cv2.resize(img,(300,700))
img1=img
cv2.imshow("window2",img1)
img2=img
cv2.imshow("window",img)
cv2.setMouseCallback("window",func)
cv2.waitKey(0)
cv2.destroyAllWindows()