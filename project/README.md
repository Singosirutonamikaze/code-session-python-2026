# Visualisation des données : catalogue produits

Ce projet permet d'explorer visuellement les données du catalogue produits à travers une interface web simple.

---

## Comment ça marche

Le projet est divisé en deux parties :

**`server/`** : un serveur Python (Flask) qui lit le fichier de données et génère les graphiques à la demande. Quand le client demande un graphique, le serveur le dessine avec Seaborn et le renvoie comme une image.

**`client/`** : l'interface web découpée selon les dossiers existants :
- `index.html` : la structure HTML de la page
- `styles/style.css` : les styles et la mise en page
- `scripts/script.js` : le script JavaScript pour l'affichage interactif des graphiques

---

## Prérequis et versions

- **Python** : 3.14 (testé sous Python 3.14.7)
- **Flask** : 3.1.3
- **flask-wtf** : 1.3.0
- **matplotlib** : 3.10.9
- **seaborn** : 0.13.2
- **pandas** : 2.3.3

---

## Lancer le projet

**1 : installer les dépendances**

```bash
pip install -r server/requirements.txt
```

**2 : démarrer le serveur**

```bash
python server/app.py
```

**3 : ouvrir le client**

Ouvrir le fichier `client/index.html` dans un navigateur.

---

## Graphiques disponibles

| Graphique | Ce qu'on y voit |
|-----------|-----------------|
| Boxplot | La répartition des prix par catégorie |
| Scatterplot | La relation entre le prix et le score des avis |
| Histogramme | La distribution des prix sur l'ensemble des produits |
| Countplot | Le nombre de produits par catégorie et par statut |
| Heatmap | La corrélation entre les variables numériques |
| Violinplot | La forme de la distribution des prix par catégorie |
