"""
On utilise ici Seaborn pour tracer un jointplot.
1 : on charge les données du catalogue produits
2 : on affiche un scatterplot central entre le prix et le score
3 : on ajoute les histogrammes de chaque variable sur les côtés
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

sns.jointplot(data=data, x="Prix_Unitaire_ECO", y="Score_Avis", hue="Statut_Disponibilite")
plt.show()
