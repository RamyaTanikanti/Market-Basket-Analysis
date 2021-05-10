#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('AssociationRules.csv')

# Function to return Consequents from Association Rules dataset, based on Antecedent selected
def mba():
    
    product = input('Select a product:')
    
    subset = rules_new[rules_new['antecedents']==product]
    subset = subset.sort_values(by='lift', ascending=False).head()
    
    consequentCount = subset['consequents'].nunique()

    if consequentCount == 5:
        consequent1 = subset['consequents'][0:1]
        consequent1 = consequent1.to_string(index=False)
    
        consequent2 = subset['consequents'][1:2]
        consequent2 = consequent2.to_string(index=False)
    
        consequent3 = subset['consequents'][2:3]
        consequent3 = consequent3.to_string(index=False)
    
        consequent4 = subset['consequents'][3:4]
        consequent4 = consequent4.to_string(index=False)
    
        consequent5 = subset['consequents'][4:]
        consequent5 = consequent5.to_string(index=False)
    
        print('Products frequently bought along with {}\n 1.{}\n 2.{}\n 3.{}\n 4.{}\n 5.{}'.format(product,consequent1,
                                                                consequent2,consequent3,consequent4,consequent5))
       
    if consequentCount == 4:
        consequent1 = subset['consequents'][0:1]
        consequent1 = consequent1.to_string(index=False)
    
        consequent2 = subset['consequents'][1:2]
        consequent2 = consequent2.to_string(index=False)
    
        consequent3 = subset['consequents'][2:3]
        consequent3 = consequent3.to_string(index=False)
    
        consequent4 = subset['consequents'][3:4]
        consequent4 = consequent4.to_string(index=False)
    
        print('Products frequently bought along with {}\n 1.{}\n 2.{}\n 3.{}\n 4.{}'.format(product,consequent1,
                                                                consequent2,consequent3,consequent4))
       
    if consequentCount == 3:
        consequent1 = subset['consequents'][0:1]
        consequent1 = consequent1.to_string(index=False)
    
        consequent2 = subset['consequents'][1:2]
        consequent2 = consequent2.to_string(index=False)
    
        consequent3 = subset['consequents'][2:3]
        consequent3 = consequent3.to_string(index=False)
    
        print('Products frequently bought along with {}\n 1.{}\n 2.{}\n 3.{}'.format(product,consequent1,consequent2,
                                                                                     consequent3))
        
    if consequentCount == 2:
        consequent1 = subset['consequents'][0:1]
        consequent1 = consequent1.to_string(index=False)
    
        consequent2 = subset['consequents'][1:2]
        consequent2 = consequent2.to_string(index=False)
    
        print('Products frequently bought along with {}\n 1.{}\n 2.{}'.format(product,consequent1,consequent2))
        
    if consequentCount == 1:
        consequent1 = subset['consequents'][0:1]
        consequent1 = consequent1.to_string(index=False)
    
        print('Products frequently bought along with {}\n 1.{}'.format(product,consequent1))
        
mba()

