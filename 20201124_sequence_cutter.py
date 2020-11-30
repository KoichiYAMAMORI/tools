# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:19:41 2020

@author: Koichi YAMAMORI
"""

import pandas as pd
import os
#file {'geneID','chr','position'}

Files=os.listdir('bin')
chro=['chr01','chr02','chr03','chr04','chr05','chr06','chr07','chr08', 'chr09','chr10','chr11','chr12']

#for test
#selected_gene=['all_Down.csv']
#chro=['chr01']

for file in Files:
    gene_df=pd.read_csv('bin/'+file,index_col='geneID')
    
    for c in chro:
        ch=gene_df.loc[gene_df['chr']==c]
        seq=[]
        for g in range(len(ch)):
            forward=ch.iloc[g,1]-150
            reverse=ch.iloc[g,1]+150
            
            f_block=forward//60
            r_block=reverse//60
            
            f_num=forward-f_block*60
            r_num=reverse-r_block*60
            
            ref=pd.read_csv('REF/IRGSP-1.0_genome.csv',usecols=['>'+c])
            
            
            seq_head=ref.iloc[r_block].values.tolist()[0][(r_num-1):].strip('\n')
            #block=0を定義しないとspyderがエラーを吐く
            block=0
            for block in range(r_block,f_block-1):
                seq_head=seq_head+ref.iloc[block].values.tolist()[0].strip('\n')
                
            seq_head=seq_head+ref.iloc[block+1].values.tolist()[0][:f_num].strip('\n')
            seq.append(seq_head)
        ch['seq']=seq
        ch.to_csv('results/'+file+'_'+c+'.csv')
        print()
        print()
        print(file+'の'+c+'が終わりました')
        print()
        print()