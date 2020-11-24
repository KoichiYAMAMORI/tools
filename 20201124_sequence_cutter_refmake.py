# -*- coding: utf-8 -*-
"""
Created on Thu May 28 09:47:28 2020

@author: Koichi YAMAMORI
"""


import pandas as pd

chro=['>chr00','>chr01','>chr02','>chr03','>chr04','>chr05','>chr06','>chr07','>chr08', '>chr09','>chr10','>chr11','>chr12']
input='REF/IRGSP-1.0_genome.fasta'

lst=[i for i in range(721184)]
df=pd.DataFrame(lst)
i=0
lst=[]
with open (input) as f:
    for line in f:
         
         if line.startswith('>'):
             
             length=721184-len(lst)
             for n in range(length):
                 lst.append(n)
            
             df[chro[i]]=lst
             lst=[]
             print('completed')
             i=i+1
         else:
             lst.append(line)
             
    length=721184-len(lst)
         
         
    for n in range(length):
        lst.append(n)
    df[chro[i]]=lst
    lst=[]
    print('fin')
f=0

df.iloc[:,[2,3,4,5,6,7,8,9,10,11,12,13]].to_csv('REF/IRGSP-1.0_genome.csv',index=False)

                
            