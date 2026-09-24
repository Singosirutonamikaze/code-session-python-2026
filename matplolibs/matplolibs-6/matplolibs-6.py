"""
On utilise ici Matplotlib pour tracer une boîte à moustaches (boxplot).
1 : on importe les bibliothèques
2 : on charge les données du catalogue produits
3 : on regroupe les prix par catégorie dans une liste
4 : on trace le boxplot avec les noms des catégories en x
5 : on affiche le graphique
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")
categories = data["Categorie"].unique()
groupes = [data[data["Categorie"] == cat]["Prix_Unitaire_ECO"].values for cat in categories]

plt.boxplot(groupes, labels=categories)
plt.xticks(rotation=30)
plt.show()
