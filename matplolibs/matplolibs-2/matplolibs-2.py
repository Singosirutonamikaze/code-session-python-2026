"""
On utilise ici Matplotlib pour tracer un graphique en barres (bar).
1 : on importe les bibliothèques
2 : on charge les données du catalogue produits
3 : on calcule le prix moyen par catégorie
4 : on trace les barres
5 : on affiche le graphique
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")
prix_par_categorie = data.groupby("Categorie")["Prix_Unitaire_ECO"].mean()

plt.bar(prix_par_categorie.index, prix_par_categorie.values)
plt.xticks(rotation=30)
plt.show()
