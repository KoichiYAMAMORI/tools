# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:27:56 2020

@author: kouit
"""

import pandas as pd
import os


input='C:/Users/kouit/Desktop/result20201019.txt'


lst=[]
with open (input) as f:
    for line in f:
        lst.append(line)

q_name=[]
q_posi=[]
length=[]      
hit=[]  

for i in range (len(lst)):
    if 'Query=' in lst[i]:
        q_name.append(lst[i])
        q_posi.append(i)   
        length.append(lst[i+2][-3:])
q_posi.append(len(lst))

result_chr=[]
SBJCT=[]
for n in range(len(length)):
    query=lst[q_posi[n]:q_posi[n+1]]
    chr_lst=[]
    sbjct=[]
    for q in range(len(query)):
        if '>' in query[q]:
            chr_lst.append(query[q])
        if 'Sbjct' in query[q]:
            if float(len(query[q].split()[2])) >= float(length[n].split('\n')[0])*0.8:  
                sbjct.append(query[q])
    SBJCT.append(sbjct) 
    hit.append(len(sbjct))
    result_chr.append(chr_lst)
q_posi=q_posi[:-1]    
    
df=pd.DataFrame({'name':q_name,'primer_length':length,'Hit':hit,'Hit_chr':result_chr,'sbjct':SBJCT} )
df.to_csv('C:/Users/kouit/Desktop/20201019_myb4_primer.csv',index=False)    
        
    