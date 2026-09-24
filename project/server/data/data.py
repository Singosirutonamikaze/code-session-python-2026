"""
Chargement des données.
1 : on localise le fichier CSV de manière fiable via pathlib
2 : on lit le catalogue produits
3 : on renvoie le dataframe prêt à l'emploi
"""
from pathlib import Path
import pandas as pd

CHEMIN_CATALOGUE = Path(__file__).resolve().parents[3] / "data" / "catalogue_produits.csv"

def charger():
    return pd.read_csv(CHEMIN_CATALOGUE, sep=";")
