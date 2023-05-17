import numpy as np
import pandas as pd


kd_=pd.read_csv('KaggelMostVotes.csv')
kd=kd_[['Votes','Title','Sub-title','Uploader',
        'Updated on','Version','Tags','FileType',
        'License','FileSize','Kernels','Discussions','Views']]

arr=[]
for i in range(len(kd.index)):
    arr.append(kd.iloc[i,12])
for j in range(len(arr)):
    arr[j]=arr[j].replace('k','000')
    arr[j]=int(arr[j])

kd['Views']=arr
#display(kd.sort_values(
#    'Views',
#    ascending = False))

#display(kd1.sort_values(#
#    'Discussions',
#    ascending = False))