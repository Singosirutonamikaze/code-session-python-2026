"""
On utilise ici Seaborn pour tracer un pairplot.
1 : on charge les données du catalogue produits
2 : on croise automatiquement toutes les variables numériques entre elles en une seule grande grille
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

sns.pairplot(data, hue="Statut_Disponibilite")
plt.show()