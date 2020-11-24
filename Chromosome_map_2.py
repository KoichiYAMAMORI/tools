# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:19:53 2020

@author: Koichi YAMAMORI
"""

from PIL import Image, ImageDraw
import pandas as pd
import os
#im=Image.new('RGB' or 'L(グレースケール)', (サイズ),(R,G,B))
im = Image.new('RGB', (1100, 500), (255, 255, 255))
draw = ImageDraw.Draw(im)

    #01Mb=1で染色体の全長
length=[450,368,373,361,301,321,304,285,239,237,312,277]
x=40

for i in length:
    #draw.rectangle((左上のx座標,左上のy座標,右下のx座標,右下のy座標),fill=(R,G,B),outline=())
    draw.rectangle((x, 30, x+30, i+30), fill=(255, 255, 255), outline=(0, 0, 0))
    #draw.chord((x, 30, x+30, i),start=0,end=360, fill=(255, 255, 255),outline=(0,0,0))
    x=x+80
    
#10Mbラダー
draw.rectangle((1050, 70, 1070, 170), fill=(255, 255, 255), outline=(0, 0, 0))



file=os.listdir('C:/Users/Koichi YAMAMORI/Desktop/bot')

col=[255,0,0,0,255,0,0,128,0,0,255,0,128,0,128]

for z in range(len(file)):
    name=file[z].split('.')[0]
    df=pd.read_csv('C:/Users/Koichi YAMAMORI/Desktop/bot/'+name+'.csv')
    
    
    chro=[i for i in range(len(df)) if df.iloc[i,0].startswith('>')]

    for n in range(len(chro)):
        c=int(df.iloc[chro[n],0][4:])-1
        if n+1!=len(chro):         
            chr_select=df['start'].iloc[chro[n]+1:chro[n+1]] 
        else:
            chr_select=df['start'].iloc[chro[n]+1:]
        #遺伝子名？
    
        for chromosome in chr_select:
            draw.line((35+80*c,int(chromosome)/100000+30,75+80*c,int(chromosome)/100000+30),fill=(col[z*3],col[z*3+1],col[z*3+2]),width=1)

im.save('C:/Users/Koichi YAMAMORI/Desktop/test.jpg')
    
    