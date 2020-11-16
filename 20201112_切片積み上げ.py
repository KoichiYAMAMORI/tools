# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:57:07 2020

@author: kouit
"""

import pandas as pd
import matplotlib.pyplot as plt
val_name=['HSY','KSH','NIP','T65','Kas']
df=pd.read_excel('C:/Users/kouit/Desktop/Book2.xlsx',index_col=0)
for v in range(5):
    val=df.iloc[:,[0+2*v,1+2*v]]
    for s in range(2):
        #0=b,1=f
        if s==0:
            dataset=val.iloc[0:5]
            #BOOTING {正常: 'gold', 剥離:'darkgreen' , 肥大: 'red', 未分化: 'deepskyblue', 崩壊:'darkviolet' , その他: 'darkgray'}
            colors = ['gold', 'darkgreen', 'red', 'deepskyblue','darkviolet' ]

        else:
            dataset=val.iloc[5:]
            #FLOURING {正常: gold, tiny: teal, tdr: firebrick,  未分化: 'deepskyblue', 崩壊:'darkviolet' , その他: 'w'}
            colors= ['gold','firebrick','deepskyblue','darkviolet' ]

        fig, ax = plt.subplots(figsize=(10, 8))
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        ax.tick_params(labelleft=False)
        ax.tick_params(labelbottom=False)
        ax.tick_params(left=False)

        dataset.T.plot(kind='bar', stacked=True, ax=ax,color=colors)
        ax.get_legend().remove()
        if s==0:
            fig.savefig('C:/Users/kouit/Desktop/積み上げ/booting/'+val_name[v]+'_b.png')
        else:
            fig.savefig('C:/Users/kouit/Desktop/積み上げ/flouring/'+val_name[v]+'_f.png')