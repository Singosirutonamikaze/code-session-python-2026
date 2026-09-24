"""
On utilise ici Matplotlib pour tracer un camembert (pie).
1 : on importe les bibliothèques
2 : on charge les données du catalogue produits
3 : on compte le nombre de produits par catégorie
4 : on trace le camembert avec les noms des catégories
5 : on affiche le graphique
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")
compte = data["Categorie"].value_counts()

plt.pie(compte.values, labels=compte.index)
plt.show()
