"""Top Menaces et Événements Sécurité"""
import os
import matplotlib.pyplot as plt
import pandas as pda
import numpy as np

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "data", "logs_simulation_attaques.csv")
data = pda.read_csv(csv_path, sep=";")

#print(data)

groupement = data['Type_Evenement'].value_counts()

plt.bar(groupement.index, groupement.values)
plt.xticks(rotation = 45, ha = 'right')
plt.show()






