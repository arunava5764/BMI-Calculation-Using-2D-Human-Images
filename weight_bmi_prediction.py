import numpy as np
import pandas as pd
import pickle
weights=[]
b=[]
with open('final_weight.list', 'rb') as config_dictionary_file:
    weight_temp = pickle.load(config_dictionary_file)
    weights=weight_temp
with open('final_b.list', 'rb') as config_dictionary_file:
    b_temp = pickle.load(config_dictionary_file)
    b=b_temp
df=pd.read_csv("scaledData_new_modifiedWork.csv")
df=df.drop(["ShWR","ShHpR","ShThR"],axis=1)
train=df
tr=len(train)
trainx=train.drop(["WEIGHT"],axis=1)
trainy=train["WEIGHT"]
trainx=np.array(trainx).reshape(len(trainx),len(trainx.columns))
trainy=np.array(trainy).reshape(len(trainy),1)
a=[]
z=[]
a.append(trainx)
z.append(np.nan)
for i in range(1,layers+1):
    temp_z=np.dot(a[len(a)-1],weights[i].T)+b[i].T
    temp_a=abs(temp_z)
    z.append(temp_z)
    a.append(temp_a)
ans=a[layers]
df1=pd.read_excel("Data_new_modifiedWork.xlsx")
df1["weight_predicted"]=ans
df1["BMI predicted"]=df1["weight_predicted"]/((df1["HEIGHT"]/100)**2)
df1.to_csv("answer.csv",index=False)