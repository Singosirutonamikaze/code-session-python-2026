"""
On utilise ici Matplotlib pour tracer un histogramme (hist).
1 : on importe les bibliothèques
2 : on charge les données du catalogue produits
3 : on trace la distribution des prix en 30 tranches
4 : on affiche le graphique
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

plt.hist(data["Prix_Unitaire_ECO"], bins=30)
plt.show()
