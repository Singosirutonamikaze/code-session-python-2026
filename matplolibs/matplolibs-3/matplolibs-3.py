"""
On utilise ici Matplotlib pour tracer un nuage de points (scatter).
1 : on importe les bibliothèques
2 : on charge les données du catalogue produits
3 : on trace chaque produit comme un point : prix en x, score en y
4 : on affiche le graphique
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

plt.scatter(data["Prix_Unitaire_ECO"], data["Score_Avis"])
plt.show()
