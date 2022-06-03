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
print(end1-start1+1)
newend=end1-(2*(end1-start1)//4)
newstart=(((end1-start1)//4))+start1
#hips#
hipleft=None
hipright=None
for i in range(start2,300,1):
    if image[newend+3][i]==0:
        hipright=i
        break
for i in range(start2-1,0,-1):
    if image[newend+3][i]==0:
        hipleft=i
        break
#optional#
# =============================================================================
# hipleft=hipleft+18
# hipright=hipright-18
# =============================================================================
#optional#
print("this is hip ",hipright-hipleft)
#cv2.line(image,(hipleft,newend+3),(hipright,newend+3),(100),2)
#end hips#

#waist#
waistleft=None
waistright=None
for i in range(start2,300,1):
    if image[newend-(((end1-start1)//4)//3)][i]==0:
        waistright=i
        break
for i in range(start2-1,0,-1):
    if image[newend-(((end1-start1)//4)//3)][i]==0:
        waistleft=i
        break
#optional#
waistleft=waistleft+3
waistright=waistright-31
#optional#
print("this is THIGH ",waistright-waistleft)
cv2.line(image,(waistleft,newend+(((end1-start1)//4)//3)),(waistright,newend+(((end1-start1)//4)//3)),(100),2)
#waist ends#

# =============================================================================
# cv2.line(image,(left,newend),(right,newend),(100),2)
# =============================================================================
# =============================================================================
# cv2.putText(image,str(newend)+","+str(start2),(start2,newend),cv2.FONT_HERSHEY_SIMPLEX,0.5,(110),2)
# =============================================================================

# =============================================================================
# cv2.line(image,(handleft,newend+3),(handright,newend+3),(100),2)
# =============================================================================
# =============================================================================
# cv2.putText(image,str(start2)+","+str(end1),(right,newend),cv2.FONT_HERSHEY_SIMPLEX,0.5,(110),2)
# cv2.putText(image,str(start2)+","+str(newend),(left,newend),cv2.FONT_HERSHEY_SIMPLEX,0.5,(110),2)
# =============================================================================

staff=image[newstart:newend,:]
# =============================================================================
# print(right-left)
# =============================================================================
# =============================================================================
# print(handright-handleft)
# =============================================================================
cv2.imshow("ans2",image)
# =============================================================================
# cv2.imshow("ans3",staff)
# =============================================================================
cv2.waitKey(0)
cv2.destroyAllWindows()