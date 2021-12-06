import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
brics = pd.read_csv('housing_data.csv', index_col = 0)
#print(brics.shape)
#print(brics.describe())
#print(brics.info())
#print(brics.values)
#print(type(brics.values))
#print(brics[brics['sqft_lot15']>10000])
term = brics.sort_values('price')
#print(term.head()) 
terms = brics.sort_values(['price', 'sqft_lot15'], ascending=[False, True])
#print(terms.head())
#print(brics[brics['price']>300000])
print(brics[(brics['condition']==5) & (brics['price']>600000)])
