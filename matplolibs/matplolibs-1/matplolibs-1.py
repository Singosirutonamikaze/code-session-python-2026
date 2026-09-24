"""
On utilise ici Matplotlib pour tracer un graphique en lignes (plot).
1 : on importe les bibliothèques
2 : on charge les données du catalogue produits
3 : on trie par date d'ajout
4 : on trace l'évolution du prix au fil du temps
5 : on affiche le graphique
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")
data["Date_Ajout"] = pd.to_datetime(data["Date_Ajout"])
data_sorted = data.sort_values("Date_Ajout")

plt.plot(data_sorted["Date_Ajout"], data_sorted["Prix_Unitaire_ECO"])
plt.xticks(rotation=30)
plt.show()
