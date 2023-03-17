import pandas as pd 
import numpy as np
import os
import glob

s = pd.Series(np.random.randn(5), index=["a","b","c","d","e"])
s.index
print(s)
print(s.index)

# por defecto ordena los indices
d = {'b':1, 'a':0, 'c':2}
s = pd.Series(d)
print(s)

# Cuando yo quiero ordenar:
d = {'b':1, 'a':0, 'c':2}
s = pd.Series(d, index=["b","c","d","a"])
print(s)

current = os.getcwd()
file = glob.glob(current+'/*.csv')
print(file)
mmse = pd.read_csv(file[0], sep=';')
print(mmse)