"""
On utilise ici Seaborn pour tracer un kdeplot.
1 : on charge les données du catalogue produits
2 : on affiche la densité lissée des scores selon le statut de disponibilité
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

sns.kdeplot(data=data, x="Score_Avis", hue="Statut_Disponibilite", fill=True)
plt.show()
