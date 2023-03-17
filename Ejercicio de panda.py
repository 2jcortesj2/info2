import pandas as pd 
import numpy as np

s = pd.Series(np.random.randn(5), index=["a","b","c","d","e"])
s.index
print(s)
print(s.index)

d = {'b':1, 'a':0, 'c':2}
s = pd.Series(d)
print(s)