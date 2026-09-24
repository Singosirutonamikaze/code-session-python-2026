from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def analyze_catalogue_produits():
    df = pd.read_csv(DATA_DIR / "catalogue_produits.csv", sep=";")
    df["Date_Ajout"] = pd.to_datetime(df["Date_Ajout"])

    fig, axes = plt.subplots(2, 2, figsize=(16, 11))

    sns.boxplot(data=df, x="Categorie", y="Prix_Unitaire_ECO", ax=axes[0, 0])
    axes[0, 0].tick_params(axis="x", rotation=25)

    sns.scatterplot(
        data=df,
        x="Prix_Unitaire_ECO",
        y="Score_Avis",
        hue="Statut_Disponibilite",
        size="Quantite_Stock",
        ax=axes[0, 1],
    )

    sns.countplot(data=df, x="Categorie", hue="Statut_Disponibilite", ax=axes[1, 0])
    axes[1, 0].tick_params(axis="x", rotation=25)

    df_monthly = df.set_index("Date_Ajout").resample("ME")["ID_Produit"].count().reset_index()
    axes[1, 1].plot(df_monthly["Date_Ajout"], df_monthly["ID_Produit"], marker="o")
    axes[1, 1].tick_params(axis="x", rotation=45)

    plt.show()


def analyze_logs_attaques():
    df = pd.read_csv(DATA_DIR / "logs_simulation_attaques.csv", sep=";")
    df["Horodatage"] = pd.to_datetime(df["Horodatage"])

    fig, axes = plt.subplots(2, 2, figsize=(16, 11))

    event_counts = df["Type_Evenement"].value_counts().reset_index()
    event_counts.columns = ["Type_Evenement", "Count"]
    sns.barplot(data=event_counts, y="Type_Evenement", x="Count", ax=axes[0, 0])

    contingency = pd.crosstab(df["Severite"], df["Statut"])
    sns.heatmap(contingency, annot=True, fmt="d", cmap="YlOrRd", ax=axes[0, 1])

    top_ips = df["IP_Source"].value_counts().head(5)
    axes[1, 0].pie(top_ips.values, labels=top_ips.index, autopct="%1.1f%%")

    sns.countplot(
        data=df,
        x="Utilisateur",
        hue="Severite",
        ax=axes[1, 1],
        order=df["Utilisateur"].value_counts().index,
    )
    axes[1, 1].tick_params(axis="x", rotation=30)

    plt.show()


if __name__ == "__main__":
    analyze_catalogue_produits()
    analyze_logs_attaques()