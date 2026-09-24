"""
On utilise ici Seaborn pour tracer une heatmap.
1 : on charge les données du catalogue produits
2 : on calcule la corrélation entre les variables numériques
3 : on affiche cette corrélation sous forme de grille colorée
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

corr = data[["Prix_Unitaire_ECO", "Quantite_Stock", "Score_Avis"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()
