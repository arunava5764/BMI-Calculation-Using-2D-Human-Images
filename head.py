import cv2 
import numpy as np
import matplotlib.pyplot as plt 
image=cv2.imread('SHAHZEB_FRONT_EDIT.jpg',0)
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
print(end1-start1-1)
newend=start1+2*((end1-start1)//4)//4
newstart=start1
staff=image[newstart:newend][:]
print(start1)
maximum=-1
index=-1
print(newstart,newend)
for i in range(newstart,newend+1,1):
    if maximum < np.count_nonzero(image[i][:]):
        maximum=np.count_nonzero(image[i][:])
        index=i
        
left=-1
right=-1
for i in range(300):
    if image[index][i]>50:
        left=i
        break
for i in range(299,-1,-1):
    if image[index][i]>50:
        right=i
        break
print(right-left)
cv2.line(image,(left,index),(right,index),(100),2)
cv2.imshow("ans3",image)
#cv2.imshow("staff",staff)
cv2.waitKey(0)
cv2.destroyAllWindows()