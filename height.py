import cv2 
import numpy as np
import matplotlib.pyplot as plt 
image=cv2.imread('ANKITA_SIDE_EDIT.jpg',0)
start1=0
start2=0
end1=0
end2=0
flag=0
for i in range(700):
    for j in range(300):
        if image[i][j]==255:
            start1=i
            start2=j
            flag=1
            break
    if flag==1:
        break
flag=0
for i in range(699,-1,-1):
    for j in range(299,-1,-1):
        if image[i][j]==255:
            end1=i
            end2=j
            flag=1
            break
    if flag==1:
        break
print(end1-start1+1)
newend=((end1-start1)//4)+start1
cv2.line(image,(start2,start1),(start2,end1),(100),2)
cv2.putText(image,str(start2)+","+str(start1),(start2,start1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(110),2)
cv2.putText(image,str(start2)+","+str(end1),(start2,end1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(110),2)
cv2.putText(image,str(start2)+","+str(newend),(start2,newend),cv2.FONT_HERSHEY_SIMPLEX,0.5,(110),2)
cv2.imshow("ans2",image)
cv2.waitKey(0)
cv2.destroyAllWindows()