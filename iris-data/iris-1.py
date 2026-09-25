"""Recupérer et afficher les données d'iris"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris 

datas_iris = load_iris()

x = datas_iris.data
y = datas_iris.target
names = list(datas_iris.target_names)

print(x)
print(y)
print(names)

