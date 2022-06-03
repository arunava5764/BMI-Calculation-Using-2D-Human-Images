import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import random as rd
import math
# data entry #
df=pd.read_csv("scaledData_new_modifiedWork.csv")
df=df.drop(["ShWR","ShHpR","ShThR"],axis=1)
train=df.sample(frac=0.7,random_state=100)
test=df.drop(train.index)
tr=len(train)
te=len(test)
trainx=train.drop(["WEIGHT"],axis=1)
trainy=train["WEIGHT"]
testx=test.drop(["WEIGHT"],axis=1)
testy=test["WEIGHT"]
trainx=np.array(trainx).reshape(len(trainx),len(trainx.columns))
trainy=np.array(trainy).reshape(len(trainy),1)
testx=np.array(testx).reshape(len(testx),len(testx.columns))
testy=np.array(testy).reshape(len(testy),1)
# data entry ends #

# user input #
index=[]
layers=0
check=True
while(check):
    layers=int(input("Enter the nummber of layers "))
    index=input("Enter the number of nodes for each ").split(" ")
    index=list(map(int,index))
    if len(index)>layers or len(index)<layers:
        print("Inconsistant")
    else:
        check=False
        
# user input end #

# declaration #
index.append(1)
layers+=1
weights=[]
a=[]
z=[]
b=[]
dw=[0]*(layers+1)
db=[0]*(layers+1)
weights.append(np.nan)
a.append(trainx)
z.append(np.nan)
b.append(np.nan)
dw[0]=np.nan
db[0]=np.nan
loss=[]
it=[]
# declaration ends #

# weight and bias input #
columns=(a[0].shape)[1]
for i in range(1,layers+1):
    rows=index[i-1]
    weight_temp=[] #weight for each node of a layer#
    b_temp=[] #bias for each node of a layer#
    for j in range(rows):
        weight_temp_row=[] # each weight of each node #
        for k in range(columns):
            weight_temp_row.append(rd.random())
        weight_temp.append(weight_temp_row)
        b_temp.append(rd.random())
    weight_temp=np.array(weight_temp).reshape(rows,columns)
    b_temp=np.array(b_temp).reshape(rows,1)
    weights.append(weight_temp)
    b.append(b_temp)
    columns=rows

    
# weight and bias input ends #

# forward propagation once for filling z,a since z and a is empty #
for i in range(1,layers+1):
    temp_z=np.dot(a[len(a)-1],weights[i].T)+b[i].T
    temp_a=abs(temp_z)
    z.append(temp_z)
    a.append(temp_a)

# forward propagation once for filling z,a since z and a is empty #

# main iteration (FORWARD PROPAGATION and BACK PROPAGATION ) #
for iteration in range(115000):
    # forward propagation #
    for i in range(1,layers+1):
        z[i]=np.dot(a[i-1],weights[i].T)+b[i].T
        a[i]=abs(z[i])
    # forward propagation end #
    
    # back propagation #
    da=a[len(a)-1]-trainy
    dz=da*(z[len(z)-1]/abs(z[len(z)-1]))
    m=np.dot(a[len(a)-2],weights[len(weights)-1].T)+b[len(b)-1].T
    n=abs(np.dot(a[len(a)-2],weights[len(weights)-1].T)+b[len(b)-1].T)
    dw[len(dw)-1]=np.dot((da*(m/n)).T,a[len(a)-2])/tr
    db[len(db)-1]=np.sum(dz,axis=0)/tr
    db[len(db)-1]=db[len(db)-1].reshape(len(db[len(db)-1]),1)
    for i in range(layers-1,0,-1):
        da=np.dot(dz,weights[i+1])
        dz=da*(z[i]/a[i])
        m=np.dot(a[i-1],weights[i].T)+b[i].T
        n=abs(np.dot(a[i-1],weights[i].T)+b[i].T)
        dw[i]=np.dot((da*(m/n)).T,a[i-1])/tr
        db[i]=np.sum(dz,axis=0)/tr
        db[i]=db[i].reshape(len(db[i]),1)
        
    # back propagation end #   
    
    # decreament #
    alpha=0.000315
    for i in range(1,len(weights)-1):
        weights[i]-=alpha*dw[i]
        b[i]-=alpha*db[i]
    
    # decreament ends #
    
    loss.append(np.sum(abs(a[len(a)-1]-trainy))/tr)
    it.append(iteration)

# graph #
sns.lineplot(x=it,y=loss)
#graph end #
a[0]=testx
for i in range(1,layers+1):
    z[i]=np.dot(a[i-1],weights[i].T)+b[i].T
    a[i]=abs(z[i])
#print(a[layers].shape)
print(np.sum(abs(a[layers]-testy))/te)
#print(a[layers]-testy)
#print(a[layers].T)
#print(testy.T)
a[0]=trainx
for i in range(1,layers+1):
    z[i]=np.dot(a[i-1],weights[i].T)+b[i].T
    a[i]=abs(z[i])

print(np.sum(abs(a[layers]-trainy))/tr)
 
# =============================================================================
# import pickle 
# with open('final_weight.list', 'wb') as config_dictionary_file:
#     pickle.dump(weights, config_dictionary_file)
# with open('final_b.list', 'wb') as config_dictionary_file:
#     pickle.dump(b, config_dictionary_file)
# =============================================================================


        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    