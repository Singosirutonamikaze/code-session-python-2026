"""
On utilise ici Seaborn pour tracer un scatterplot.
1 : on charge les données du catalogue produits
2 : on affiche la relation entre le prix et le score des avis, en distinguant le statut de disponibilité
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

sns.scatterplot(data=data, x="Prix_Unitaire_ECO", y="Score_Avis", hue="Statut_Disponibilite", size="Quantite_Stock")
plt.show()