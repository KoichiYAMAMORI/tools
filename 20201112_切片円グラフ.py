# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:28:16 2020

@author: kouit
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/kouit/Desktop/1112.csv')
val=list(set(df.iloc[:,1].values.tolist()))
condition=['N','L']
for v in val:
    df_v=df.loc[df.iloc[:,1]==v]
    for s in range(2):
        Datas=df_v.iloc[:,[3+5*s,4+5*s]]
        for c in range (2):
            data=Datas.iloc[:,c].values.tolist()[::-1]
            if s==0:
                #BOOTING {正常: 'gold', 剥離:'darkgreen' , 肥大: 'red', 未分化: 'deepskyblue', 崩壊:'darkviolet' , その他: 'darkgray'}
                colors = ['gold', 'darkgreen', 'red', 'deepskyblue','darkviolet' , 'darkgray']
                fig = plt.figure()
                plt.pie(data, colors=colors[::-1], startangle=450)
                fig.savefig('C:/Users/kouit/Desktop/円グラフ/booting/'+v+'_'+condition[c]+'_b.png',bbox_inches='tight')
                
            else:
                #FLOURING {正常: gold, tiny: yellowgreen, tdr: firebrick,  未分化: 'deepskyblue', 崩壊:'darkviolet' , その他: 'w'}
                colors= ['gold','coral','firebrick','deepskyblue','darkviolet' , 'darkgray']
                fig = plt.figure()
                plt.pie(data, colors=colors[::-1], startangle=450)
                fig.savefig('C:/Users/kouit/Desktop/円グラフ/flouring/'+v+'_'+condition[c]+'_f.png',bbox_inches='tight')







