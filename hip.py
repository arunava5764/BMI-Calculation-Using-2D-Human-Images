import cv2 
import numpy as np
import matplotlib.pyplot as plt 
image=cv2.imread('RAJARSHI_FRONT_EDIT.jpg',0)
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
#print(end1-start1+1)
newend=((end1-start1)//4)+start1
p=start1
#print(newend)
start1=newend
newend=((end1-newend)//3)+newend
p=start1
start1=newend
newend=((end1-newend)//2)+newend
#newend=((end1-newend)//2)+newend
#print(newend,start1)
cv2.line(image,(start2,start1),(start2,end1),(100),2)
cv2.putText(image,str(start2)+","+str(start1),(start2,start1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(110),2)
cv2.putText(image,str(start2)+","+str(end1),(start2,end1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(110),2)
cv2.putText(image,str(start2)+","+str(newend),(start2,newend),cv2.FONT_HERSHEY_SIMPLEX,0.5,(110),2)
staff=image[:newend,:]
yaxisleft=[]
yaxisright=[]

for i in range(start1,newend+2):    
    for j in range(300):
        if image[i][j]==255:
            yaxisleft.append(j)
            break
for i in range(start1,newend+2):    
    for j in range(299,-1,-1):
        if image[i][j]==255:
            yaxisright.append(j)
            break
yaxisleft=np.array(yaxisleft).reshape(start1-newend+1)
yaxisright=np.array(yaxisright).reshape(start1-newend+1)
distances=yaxisright-yaxisleft

xaxis=np.arange(start1,newend+2).reshape(((end1-p)//3)+2)
#print(xaxis)
distances=np.array(distances).reshape(((end1-p)//3)+2)
# =============================================================================
# yaxisleft=np.array(yaxisleft).reshape(((end1-start1)//4)+2)
# yaxisright=np.array(yaxisright).reshape(((end1-start1)//4)+2)
# =============================================================================
#print(distances)
xreq=xaxis[:]
#print(xreq)
yreq=distances[:]
STRAND=7
firstslope=[]
last=None
# =============================================================================
# for i in range(0,len(yreq)-STRAND,STRAND):
#     firstslope.append(abs((yreq[i+STRAND]-yreq[i])/(xreq[i+STRAND]-xreq[i])))
#     last=i
# last=last+STRAND
# if last<len(yreq)-1:
#     firstslope.append(abs((yreq[len(yreq)-1]-yreq[last])/(xreq[len(yreq)-1]-xreq[last])))
# =============================================================================
for i in range(0,len(yreq)-STRAND,STRAND):
    firstslope.append(abs((yreq[i+STRAND]-yreq[i])))
    last=i
last=last+STRAND
if last<len(yreq)-1:
    firstslope.append(abs((yreq[len(yreq)-1]-yreq[last])))
# =============================================================================
# firstslope=np.diff(yreq)//np.diff(xreq)
# =============================================================================
points=[]
lineleft=[]
lineright=[]
for i in range(0,len(xreq)-STRAND,STRAND):
    points.append(str(xreq[i])+"-"+str(xreq[i+STRAND]))
    last=i
last=last+STRAND
if last<len(xreq)-1:
    points.append(str(xreq[last])+"-"+str(xreq[len(xreq)-1]))

index=None
maxi=-1
for i in range(len(firstslope)):
    if maxi<=firstslope[i]:
        maxi=firstslope[i]
        index=i
#print(points[index])
stop=-1
for i in range(len(points[index])):
    if points[index][i]=="-":
        stop=i

point=int(points[index][stop+1:])
plt.figure(figsize=(20,15))
plt.bar(points,firstslope)
plt.show()
cv2.putText(image,str(start2)+","+str(point),(start2,point),cv2.FONT_HERSHEY_SIMPLEX,0.5,(110),2)   
cv2.line(image,(yaxisleft[point-start1],point),(yaxisright[point-start1],point),(100),2)
cv2.imshow("ans2",image)
#cv2.imshow("ans3",staff)
cv2.waitKey(0)
cv2.destroyAllWindows()


