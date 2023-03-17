import pandas as pd 
import numpy as np
import os
import glob

# s = pd.Series(np.random.randn(5), index=["a","b","c","d","e"])
# s.index
# print(s)
# print(s.index)

# por defecto ordena los indices

# d = {'b':1, 'a':0, 'c':2}
# s = pd.Series(d)
# print(s)

# Cuando yo quiero ordenar:

# d = {'b':1, 'a':0, 'c':2}
# s = pd.Series(d, index=["b","c","d","a"])
# print(s)

current = os.getcwd() # Toma la dirección de la carpeta actual

file = glob.glob(current+'/*.csv') # Obtiene una lista con todos los  .csv

mmse = pd.read_csv(file[0], sep=';') # Se optiene la tabla en panda

# print(mmse['Escolaridad']) # Imprime la colummna escolaridad sin encabezado
# print(mmse['Escolaridad'].describe()) # Imprime estadísticas varias de Escolaridad

mmse_copy = mmse.set_index('Codigo')
print(mmse_copy)
print(mmse.iloc[1])
print('\n')
print(mmse_copy.loc['CTR_004'])