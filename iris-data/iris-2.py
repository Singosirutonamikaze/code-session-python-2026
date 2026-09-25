"""Recupérer et afficher les données d'iris avec scatter et scatterplot"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris 
import pandas as pda 
import seaborn as sns 

datas_iris = load_iris()
print(datas_iris)

df = pda.DataFrame(datas_iris.data, datas_iris.target)
x = datas_iris.data
y = datas_iris.target

print(df)
sns.scatterplot(data=df, x=0,  y=1, palette='deep')

plt.show()

