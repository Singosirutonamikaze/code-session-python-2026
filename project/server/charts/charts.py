"""
Génération des graphiques.
1 : chaque graphique a sa propre fonction
2 : la fonction generer() appelle la bonne fonction selon le nom reçu
3 : make_image() transforme le graphique en image PNG et le renvoie
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import io
from flask import send_file
from data.data import charger


def make_image():
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    plt.close()
    return send_file(buf, mimetype="image/png")


def boxplot(data):
    sns.boxplot(data=data, x="Categorie", y="Prix_Unitaire_ECO")
    plt.xticks(rotation=30)
    plt.title("Distribution des prix par catégorie")


def scatterplot(data):
    sns.scatterplot(data=data, x="Prix_Unitaire_ECO", y="Score_Avis", hue="Statut_Disponibilite")
    plt.title("Prix vs Score des avis")


def histplot(data):
    sns.histplot(data=data, x="Prix_Unitaire_ECO", bins=30, kde=True)
    plt.title("Distribution des prix")


def countplot(data):
    sns.countplot(data=data, x="Categorie", hue="Statut_Disponibilite")
    plt.xticks(rotation=30)
    plt.title("Nombre de produits par catégorie")


def heatmap(data):
    corr = data[["Prix_Unitaire_ECO", "Quantite_Stock", "Score_Avis"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Corrélation entre les variables")


def violinplot(data):
    sns.violinplot(data=data, x="Categorie", y="Prix_Unitaire_ECO")
    plt.xticks(rotation=30)
    plt.title("Distribution des prix par catégorie (violon)")


GRAPHIQUES = {
    "boxplot":     boxplot,
    "scatterplot": scatterplot,
    "histplot":    histplot,
    "countplot":   countplot,
    "heatmap":     heatmap,
    "violinplot":  violinplot,
}


def generer(type_graphique):
    data = charger()
    GRAPHIQUES[type_graphique](data)
    return make_image()
