"""
On utilise ici Seaborn pour tracer un regplot.
1 : on charge les données du catalogue produits
2 : on affiche le nuage de points entre le prix et le score avec une droite de régression
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

sns.regplot(data=data, x="Prix_Unitaire_ECO", y="Score_Avis")
plt.show()
