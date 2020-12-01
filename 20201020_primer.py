# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:27:56 2020

@author: kouit
"""

import pandas as pd
import os


Files=os.listdir('bin/')
#input is result from BLAST+

for file in Files:
    input='bin/'+file



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
                Chr=query[q]
            if 'Sbjct' in query[q]:
                if float(len(query[q].split()[2])) >= float(length[n].split('\n')[0])*0.8:  
                    sbjct.append(query[q])
                    chr_lst.append(Chr)
        SBJCT.append(sbjct) 
        hit.append(len(sbjct))
        result_chr.append(chr_lst)
    q_posi=q_posi[:-1]    
    
    df=pd.DataFrame({'name':q_name,'primer_length':length,'Hit':hit,'Hit_chr':result_chr,'sbjct':SBJCT} )
    df.to_csv('bin/'+file.split('.')[0]+'.csv',index=False)    
        
    
