"""
Analyse exploratoire et visualisation de données avec Matplotlib et Seaborn.
Couvre deux jeux de données du dossier 'data' :
1. Catalogue Produits (catalogue_produits.csv)
2. Logs de Sécurité (logs_simulation_attaques.csv)
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configuration globale du style
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams["figure.autolayout"] = True
plt.rcParams["font.sans-serif"] = "DejaVu Sans"

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


# =====================================================================
# 1. ANALYSE DU CATALOGUE PRODUITS
# =====================================================================
def analyze_catalogue_produits():
    file_path = DATA_DIR / "catalogue_produits.csv"
    if not file_path.exists():
        print(f"Fichier non trouvé : {file_path}")
        return

    df = pd.read_csv(file_path, sep=";")
    df["Date_Ajout"] = pd.to_datetime(df["Date_Ajout"])
    df["Valeur_Stock"] = df["Prix_Unitaire_ECO"] * df["Quantite_Stock"]

    print("=== Aperçu Catalogue Produits ===")
    print(df.info())
    print(df.describe())

    fig, axes = plt.subplots(2, 2, figsize=(16, 11))
    fig.suptitle("Analyse Exploratoire - Catalogue Produits", fontsize=18, fontweight="bold")

    # 1. Distribution des prix par catégorie (Boxplot Seaborn)
    sns.boxplot(
        data=df,
        x="Categorie",
        y="Prix_Unitaire_ECO",
        ax=axes[0, 0],
        palette="Set2"
    )
    axes[0, 0].set_title("Distribution des Prix par Catégorie", fontsize=13, fontweight="semibold")
    axes[0, 0].set_xlabel("")
    axes[0, 0].set_ylabel("Prix Unitaire (ECO)")
    axes[0, 0].tick_params(axis="x", rotation=25)

    # 2. Relation Score Avis vs Prix Unitaire avec Statut de Stock (Scatterplot)
    sns.scatterplot(
        data=df,
        x="Prix_Unitaire_ECO",
        y="Score_Avis",
        hue="Statut_Disponibilite",
        size="Quantite_Stock",
        sizes=(30, 250),
        alpha=0.75,
        ax=axes[0, 1]
    )
    axes[0, 1].set_title("Score d'Avis vs Prix & Quantité en Stock", fontsize=13, fontweight="semibold")
    axes[0, 1].set_xlabel("Prix Unitaire (ECO)")
    axes[0, 1].set_ylabel("Score d'Avis (1-5)")
    axes[0, 1].legend(bbox_to_anchor=(1.02, 1), loc="upper left", borderaxespad=0)

    # 3. Répartition des produits par catégorie et disponibilité (Countplot)
    sns.countplot(
        data=df,
        x="Categorie",
        hue="Statut_Disponibilite",
        ax=axes[1, 0],
        palette="viridis"
    )
    axes[1, 0].set_title("Nombre de Produits par Disponibilité", fontsize=13, fontweight="semibold")
    axes[1, 0].set_xlabel("Catégorie")
    axes[1, 0].set_ylabel("Nombre de Références")
    axes[1, 0].tick_params(axis="x", rotation=25)

    # 4. Évolution des ajouts de produits par mois (Matplotlib Lineplot)
    df_monthly = (
        df.set_index("Date_Ajout")
        .resample("ME")["ID_Produit"]
        .count()
        .reset_index()
    )
    axes[1, 1].plot(
        df_monthly["Date_Ajout"].dt.strftime("%Y-%m"),
        df_monthly["ID_Produit"],
        marker="o",
        linewidth=2.5,
        color="#2b5c8f"
    )
    axes[1, 1].set_title("Évolution Temporelle des Ajouts au Catalogue", fontsize=13, fontweight="semibold")
    axes[1, 1].set_xlabel("Mois d'Ajout")
    axes[1, 1].set_ylabel("Nouveaux Produits")
    axes[1, 1].tick_params(axis="x", rotation=45)
    axes[1, 1].grid(True, linestyle="--", alpha=0.6)

    plt.show()


# =====================================================================
# 2. ANALYSE DES LOGS D'ATTAQUES ET SÉCURITÉ
# =====================================================================
def analyze_logs_attaques():
    file_path = DATA_DIR / "logs_simulation_attaques.csv"
    if not file_path.exists():
        print(f"Fichier non trouvé : {file_path}")
        return

    df = pd.read_csv(file_path, sep=";")
    df["Horodatage"] = pd.to_datetime(df["Horodatage"])

    print("\n=== Aperçu Logs d'Attaques ===")
    print(df.info())

    fig, axes = plt.subplots(2, 2, figsize=(16, 11))
    fig.suptitle("Monitoring & Analyse - Logs de Cyberattaques", fontsize=18, fontweight="bold")

    # 1. Répartition des types d'événements (Barplot horizontal)
    event_counts = df["Type_Evenement"].value_counts().reset_index()
    event_counts.columns = ["Type_Evenement", "Count"]
    sns.barplot(
        data=event_counts,
        y="Type_Evenement",
        x="Count",
        ax=axes[0, 0],
        palette="mako"
    )
    axes[0, 0].set_title("Fréquence des Types d'Attaques / Événements", fontsize=13, fontweight="semibold")
    axes[0, 0].set_xlabel("Nombre d'Occurrences")
    axes[0, 0].set_ylabel("")

    # 2. Matrice croisée Sévérité vs Statut de Résolution (Heatmap Seaborn)
    contingency = pd.crosstab(df["Severite"], df["Statut"])
    sns.heatmap(
        contingency,
        annot=True,
        fmt="d",
        cmap="YlOrRd",
        cbar=True,
        ax=axes[0, 1]
    )
    axes[0, 1].set_title("Distribution Sévérité vs Statut d'Action", fontsize=13, fontweight="semibold")
    axes[0, 1].set_xlabel("Statut")
    axes[0, 1].set_ylabel("Sévérité")

    # 3. Top 5 des IPs Sources suspectes les plus actives
    top_ips = df["IP_Source"].value_counts().head(5)
    axes[1, 0].pie(
        top_ips.values,
        labels=top_ips.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=sns.color_palette("flare", len(top_ips))
    )
    axes[1, 0].set_title("Top 5 des Adresses IP Sources", fontsize=13, fontweight="semibold")

    # 4. Événements par utilisateur ciblé
    sns.countplot(
        data=df,
        x="Utilisateur",
        hue="Severite",
        ax=axes[1, 1],
        palette="coolwarm",
        order=df["Utilisateur"].value_counts().index
    )
    axes[1, 1].set_title("Comptes Utilisateurs Ciblés par Sévérité", fontsize=13, fontweight="semibold")
    axes[1, 1].set_xlabel("Nom d'Utilisateur / Identifiant")
    axes[1, 1].set_ylabel("Nombre d'Événements")
    axes[1, 1].tick_params(axis="x", rotation=30)
    axes[1, 1].legend(title="Sévérité", loc="upper right")

    plt.show()


if __name__ == "__main__":
    analyze_catalogue_produits()
    analyze_logs_attaques()
