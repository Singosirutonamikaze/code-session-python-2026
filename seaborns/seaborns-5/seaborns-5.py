"""
On utilise ici Seaborn pour tracer un lineplot.
1 : on charge les données et on convertit la date en format datetime
2 : on affiche l'évolution du prix au fil du temps
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data/catalogue_produits.csv", sep=";")

data["Date_Ajout"] = pd.to_datetime(data["Date_Ajout"])
data_sorted = data.sort_values("Date_Ajout")

sns.lineplot(data=data_sorted, x="Date_Ajout", y="Prix_Unitaire_ECO")
plt.xticks(rotation=30)
plt.show()
