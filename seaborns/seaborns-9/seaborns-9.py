"""
On utilise ici Seaborn pour tracer un countplot.
1 : on charge les données du catalogue produits
2 : on compte et affiche le nombre de produits par catégorie en distinguant le statut de disponibilité
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

sns.countplot(data=data, x="Categorie", hue="Statut_Disponibilite")
plt.xticks(rotation=30)
plt.show()
