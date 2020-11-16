# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:44:43 2020

@author: kouit
"""

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

df=pd.DataFrame(['ID','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag',
                 'tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag','tag',
                 
                 ])

gene=pd.read_csv('C:/Users/kouit/OneDrive/デスクトップ/gene.csv')['0'].tolist()

for Gene in gene:


    html=requests.get('https://funricegenes.github.io/'+Gene+'/')
    soup = BeautifulSoup(html.content, "html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text_lst=text.split('\n')
    
    
    
    for lst in range(len(text_lst)):
        if text_lst[lst] =='Tags':
            tagstart=lst
        if text_lst[lst] =='Information':
            tagsend=lst
        
        
        if 'Symbol' in text_lst[lst] :  
            name=text_lst[lst].split()[1]
        if 'RAPdb' in text_lst[lst] : 
            geneid=text_lst[lst].split()[1]
    tags=[]
    for i in range(tagstart+1,tagsend):
        tags.append(text_lst[i])    
    
    info=[geneid]
    for t in tags:
        info.append(t)
    null=35-len(info)
    if null !=0:
        for n in range(null):
            info.append('null')
    df[name]=info
df.T.to_csv('C:/Users/kouit/OneDrive/デスクトップ/cold_related_funricegenes.csv')
    
    