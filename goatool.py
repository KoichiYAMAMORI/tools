# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:20:55 2020

@author: Koichi YAMAMORI
"""

from goatools.base import download_go_basic_obo
obo_fname=download_go_basic_obo()

from goatools.obo_parser import GODag
obodat=GODag('go-basic.obo')

from goatools.godag_plot import plot_gos, plot_results, plot_goid2goobj

goid_subset = ['GO:0005737', 'GO:0005634' ]
plot_gos("SacchaGo_Subset.png", goid_subset,obodat)