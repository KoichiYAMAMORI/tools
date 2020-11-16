# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:43:05 2020

@author: kouit
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('C:/Users/kouit/Desktop/nip_ksh.xlsx',index_col=0)
cond=['C','L']
val=['Nip','KSH']
stage=['B','F']
position=['large_up','larege_mid','large_down','small_up','small_mid','small_down']

for v in range(2):
    df_v=df.iloc[:,0+v*12:12+v*12]
    for s in range(2):
        if s==0:
            df_s=df_v.iloc[0:5]
            #BOOTING {正常: 'gold', 剥離:'darkgreen' , 肥大: 'red', 未分化: 'deepskyblue', 崩壊:'darkviolet' , その他: 'darkgray'}
            colors = ['gold', 'darkgreen', 'red', 'deepskyblue','darkviolet' ]
        else:
            df_s=df_v.iloc[5:9]
            #FLOURING {正常: gold, tiny: teal, tdr: firebrick,  未分化: 'deepskyblue', 崩壊:'darkviolet' , その他: 'w'}
            colors= ['gold','firebrick','deepskyblue','darkviolet' ]
            
        for c in range(2):
            df_c=df_s.iloc[:,0+c*6:6+c*6]
            for p in range(6):
                df_p=df_c.iloc[:,p].values.tolist()[::-1]
                fig = plt.figure()
                plt.pie(df_p, colors=colors[::-1], startangle=450)
                if s==0:
                    fig.savefig('C:/Users/kouit/Desktop/円グラフ_位置ごと/booting/'+val[v]+'_'+cond[c]+'_'+position[p]+'_b.png',bbox_inches='tight')
                else:
                    fig.savefig('C:/Users/kouit/Desktop/円グラフ_位置ごと/flowering/'+val[v]+'_'+cond[c]+'_'+position[p]+'_f.png',bbox_inches='tight')
                
                