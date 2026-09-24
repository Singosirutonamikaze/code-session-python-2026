"""
On utilise ici Seaborn pour combiner un boxplot et un scatterplot dans une même figure.
1 : on charge les données du catalogue produits
2 : on crée une figure avec deux graphiques côte à côte
3 : à gauche, un boxplot des prix par catégorie ; à droite, un scatterplot prix vs score
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.boxplot(data=data, x="Categorie", y="Prix_Unitaire_ECO", ax=axes[0])
sns.scatterplot(data=data, x="Prix_Unitaire_ECO", y="Score_Avis", hue="Statut_Disponibilite", size="Quantite_Stock", ax=axes[1])

plt.show()