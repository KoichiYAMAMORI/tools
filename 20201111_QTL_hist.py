# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:27:24 2020

@author: kouit
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from statistics import mean


Dire=os.listdir('bin/')

for dire in Dire:
    df=pd.read_excel('bin/'+dire,index_col=0)
    lst=[]
    for i in range(len(df.columns)-2):
        x=df.iloc[:,i].dropna(how='all').values.tolist()
        lst=lst+x
    #親系統=p1&p2   
    p1=df.iloc[:,-2].dropna(how='all').values.tolist()
    p1_ave=mean(p1)
    p1_max=max(p1)
    p1_min=min(p1)
    
    p2=df.iloc[:,-1].dropna(how='all').values.tolist()
    p2_ave=mean(p2)
    p2_max=max(p2)
    p2_min=min(p2)
    
    lst_max=max(lst)
    lst_min=min(lst)
    #Bin数は2ごとでまとめた時の数

    Bins=np.linspace(lst_min-2,lst_max,int(-(-(lst_max-lst_min)//2))+2,dtype = 'int')
    #Y軸の上限を決定
    plant_num_lst=[]
    for b in range (int(-(-(lst_max-lst_min)//2))):
        plant_num=len([p for p in lst if (p >=int(lst_min)+b*2 ) & ( p < int(lst_min)+(b+1)*2)])
        plant_num_lst.append(plant_num)
    ylim=((-(-max(plant_num_lst)//10))+(-(-max(plant_num_lst)//10)//7))*10
    
    fig = plt.figure()
    ax = plt.axes()
    #ヒストグラム
    plt.xticks(np.arange(lst_min, lst_max+2, 2.0))
    plt.xlim(lst_min-2,lst_max+2)
    
    plt.hist(lst,color='c',bins=Bins,ec='black')
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
  
        
    plt.xlabel('Tiller number',fontsize=16)
    plt.ylabel('Number of plants',fontsize=16)
    #p1の平均と最大最小値のバー
    p1_r = patches.Rectangle(xy=(p1_min, ylim-(ylim/80)*6), width=p1_max-p1_min, height=0.005, ec='#000000', fill=False)
    ax.add_patch(p1_r)
    p1_e = patches.Polygon(xy=[(p1_ave,ylim-(ylim/80)*10),(p1_ave-0.5,ylim-(ylim/80)*4),(p1_ave+0.5,ylim-(ylim/80)*4)],color='w',ec='black')
    ax.add_patch(p1_e)
    p1_h1=patches.Rectangle(xy=(p1_min, ylim-(ylim/80)*8.5), width=0.005, height=(ylim/80)*5, ec='#000000', fill=False)
    ax.add_patch(p1_h1)
    p1_h2=patches.Rectangle(xy=(p1_max, ylim-(ylim/80)*8.5), width=0.005, height=(ylim/80)*5, ec='#000000', fill=False)
    ax.add_patch(p1_h2)
    #p2の平均と最大最小値のバー
    p2_r = patches.Rectangle(xy=(p2_min, ylim-(ylim/80)*2), width=p2_max-p2_min, height=0.005, ec='#000000', fill=False)
    ax.add_patch(p2_r)
    p2_e = patches.Polygon(xy=[(p2_ave,ylim-(ylim/80)*5),(p2_ave-0.5,ylim+(ylim/80)*1),(p2_ave+0.5,ylim+(ylim/80)*1)],color='black')
    ax.add_patch(p2_e)    
    p2_h1=patches.Rectangle(xy=(p2_min, ylim-(ylim/80)*3), width=0.005, height=(ylim/80)*5, ec='#000000', fill=False)
    ax.add_patch(p2_h1)
    p2_h2=patches.Rectangle(xy=(p2_max, ylim-(ylim/80)*3), width=0.005, height=(ylim/80)*5, ec='#000000', fill=False)
    ax.add_patch(p2_h2)    
    
    #ここでyaxisを数列で定義###################################################
    #plt.yticks(np.linspace(0, ylim+1,ylim//10))
    
    plt.yticks([i*10 for i in range (1+(ylim//10))])
    ax.set_ylim(bottom=0, top=ylim)
    fig.savefig(dire.split('.')[0]+'.png')