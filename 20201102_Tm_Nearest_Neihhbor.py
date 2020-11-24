# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:03:58 2020

@author: kouit
"""

import numpy as np
import pandas as pd
import math

para=np.array([['AA', -9.1, -24.0],
               ['TT', -9.1, -24.0],
               ['AT', -8.6, -23.9],
               ['TA', -6.0, -16.9],
               ['CA', -5.8, -12.9],
               ['TG', -5.8, -12.9],
               ['GT', -6.5, -17.3],
               ['AC', -6.5, -17.3],
               ['CT', -7.8, -20.8],
               ['AG', -7.8, -20.8],
               ['GA', -5.6, -13.5],
               ['TC', -5.6, -13.5],
               ['CG', -11.9, -27.8],
               ['GC', -11.1, -26.7],
               ['GG', -11.0, -26.6],
               ['CC', -11.0, -26.6]])

df=pd.DataFrame(para)
df.columns=['pro_seq','ΔH','ΔS']


seq=input()

def TM_cal(x):
    h=0
    s=0
    for i in range(len(seq)-1):
        pro_seq=x[i:i+2]
        h=h+float(df['ΔH'].loc[df['pro_seq']==pro_seq].values)
        s=s+float(df['ΔS'].loc[df['pro_seq']==pro_seq].values)


    Tm=(1000*h)/(-10.8+s+1.987*math.log(0.0000005/4))-273.15+16.6*math.log10(0.05)
    return(abs(Tm))

print(TM_cal(seq))