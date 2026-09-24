"""
On utilise ici Seaborn pour tracer un violinplot.
1 : on charge les données du catalogue produits
2 : on affiche la distribution des prix par catégorie sous forme de violon
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

sns.violinplot(data=data, x="Categorie", y="Prix_Unitaire_ECO")
plt.xticks(rotation=30)
plt.show()
