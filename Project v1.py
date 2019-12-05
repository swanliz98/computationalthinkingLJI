# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:45:52 2019

@author: Jessica Tse
"""

import pandas as pd

import os
directory = r'C:\Users\Jessica Tse\Desktop\Computational Thinking\2018'


filenames = []
for filename in os.listdir(directory):
    filenames.append(filename)
print(filenames)

for name in filenames:
    if 'csv' in name:
        name = pd.read_csv(filename)
    #for num in range(len(directory)):
        
        #if '.csv' in filename:
         #   df = pd.read_csv(filename)
           
    
    