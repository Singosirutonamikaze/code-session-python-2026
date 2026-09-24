"""
On utilise ici Seaborn pour tracer un histogramme avec courbe de densité.
1 : on charge les données du catalogue produits
2 : on affiche comment les prix sont distribués sur l'ensemble des produits
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

sns.histplot(data=data, x="Prix_Unitaire_ECO", bins=30, kde=True)
plt.show()
