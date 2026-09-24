class VisualiseurCatalogue {
  serveurUrl = "http://localhost:5000";

  descriptions = {
    boxplot: "Répartition des prix par catégorie.",
    scatterplot: "Prix en fonction du score des avis.",
    histplot: "Distribution globale des prix.",
    countplot: "Nombre de produits par catégorie.",
    heatmap: "Corrélation entre les variables numériques.",
    violinplot: "Densité des prix par catégorie.",
  };

  constructor() {
    this.descriptionZone = document.getElementById("description");
    this.graphiqueZone = document.getElementById("graphique");
    this.boutonsMenu = document.querySelectorAll(".groupe-boutons button");
  }

  initialiser() {
    this.boutonsMenu.forEach((bouton) => {
      bouton.addEventListener("click", () => {
        if (bouton.classList.contains("active")) {
          return;
        }
        const nomGraphique = bouton.dataset.route;
        this.afficher(nomGraphique, bouton);
      });
    });

    const premierBouton = this.boutonsMenu[0];
    if (premierBouton) {
      this.afficher(premierBouton.dataset.route, premierBouton);
    }
  }

  mettreAJourDescription(nomGraphique) {
    this.descriptionZone.textContent = this.descriptions[nomGraphique] || "";
  }

  chargerGraphique(nomGraphique) {
    const messageChargement = document.createElement("p");
    messageChargement.className = "etat-message";
    messageChargement.textContent = "Chargement du graphique en cours...";
    this.graphiqueZone.replaceChildren(messageChargement);

    const image = document.createElement("img");
    image.alt = `Graphique ${nomGraphique}`;

    image.onload = () => {
      const sourceTexte = document.createElement("p");
      sourceTexte.className = "legende";
      sourceTexte.textContent = "Source : catalogue_produits.csv";

      this.graphiqueZone.replaceChildren();
      this.graphiqueZone.appendChild(image);
      this.graphiqueZone.appendChild(sourceTexte);
    };

    image.onerror = () => {
      const messageErreur = document.createElement("p");
      messageErreur.className = "etat-message";
      messageErreur.textContent =
        "Erreur : impossible de joindre le serveur Flask (http://localhost:5000).";
      this.graphiqueZone.replaceChildren(messageErreur);
    };

    image.src = `${this.serveurUrl}/${nomGraphique}`;
  }

  activerBouton(boutonActif) {
    this.boutonsMenu.forEach((bouton) => bouton.classList.remove("active"));
    if (boutonActif) {
      boutonActif.classList.add("active");
    }
  }

  afficher(nomGraphique, boutonActif) {
    this.activerBouton(boutonActif);
    this.mettreAJourDescription(nomGraphique);
    this.chargerGraphique(nomGraphique);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const visualiseur = new VisualiseurCatalogue();
  visualiseur.initialiser();
});
