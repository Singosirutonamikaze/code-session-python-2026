# code-session-python-2026

Ce dépôt regroupe des exercices Python réalisés en cours. On y travaille principalement la **visualisation de données** à partir d'un fichier de catalogue produits.

---

## Les données

Tous les scripts utilisent le fichier `data/catalogue_produits.csv`. Ce fichier contient une liste de produits avec leur prix, leur catégorie, leur stock, leur score d'avis et leur statut de disponibilité.

---

## Matplotlib : `matplolibs/`

Matplotlib est la bibliothèque de base pour faire des graphiques en Python. On contrôle tout à la main : les axes, les couleurs, les étiquettes.

---

### `matplolibs-1/` : Graphique en lignes

On relie les valeurs par une ligne. Ici on trace le prix dans le temps : chaque point est une date, et la ligne montre comment le prix monte ou descend au fil des mois. C'est le graphique qu'on utilise chaque fois qu'on veut voir une **évolution**.

---

### `matplolibs-2/` : Graphique en barres

Une barre par catégorie. La hauteur de chaque barre représente le prix moyen des produits dans cette catégorie. C'est le graphique classique pour **comparer des groupes entre eux**.

---

### `matplolibs-3/` : Nuage de points

Chaque produit devient un point dans le graphique. Sa position horizontale correspond à son prix, sa position verticale à son score d'avis. Si les points forment une ligne montante, ça veut dire que les produits chers ont tendance à mieux noter. Si les points sont éparpillés partout, il n'y a pas de relation. C'est le graphique pour **voir si deux choses sont liées**.

---

### `matplolibs-4/` : Histogramme

On découpe les prix en tranches (ex : 0-50€, 50-100€, etc.) et on compte combien de produits tombent dans chaque tranche. Ça donne une image claire de **comment les prix sont répartis** : est-ce qu'il y a beaucoup de produits bon marché ? Quelques produits très chers ? Une répartition uniforme ?

---

### `matplolibs-5/` : Camembert

Un cercle découpé en parts, une par catégorie. La taille de chaque part correspond au nombre de produits dans cette catégorie. C'est le graphique pour voir **qui prend quelle place** dans l'ensemble du catalogue.

---

### `matplolibs-6/` : Boîte à moustaches

Pour chaque catégorie, on dessine une boîte. La boîte montre où se situent la moitié des produits (ni les plus chers ni les moins chers). Les traits qui dépassent montrent les extrêmes. Les points isolés sont les valeurs vraiment anormales. C'est le graphique pour **voir la dispersion** : est-ce que les prix sont tous similaires ou très écartés ?

---

## Seaborn : `seaborns/`

Seaborn est construit par-dessus Matplotlib. Il produit des graphiques plus soignés visuellement avec beaucoup moins de code, et il gère automatiquement les couleurs par groupe, les légendes, etc.

---

### `seaborns-1/` : Boxplot

Même idée que la boîte à moustaches de Matplotlib, mais en plus lisible. Pour chaque catégorie de produit, on voit d'un coup d'œil où se situe la majorité des prix et si certains produits ont des prix vraiment inhabituels.

---

### `seaborns-2/` : Scatterplot

Même idée que le nuage de points, mais Seaborn ajoute automatiquement une couleur différente par statut de disponibilité. On voit donc en même temps la relation prix/score **et** si les produits en rupture de stock se comportent différemment.

---

### `seaborns-3/` : Boxplot + Scatterplot côte à côte

On combine les deux graphiques précédents dans une seule figure. C'est utile pour présenter plusieurs angles d'analyse en même temps sans avoir à ouvrir plusieurs fenêtres.

---

### `seaborns-4/` : Pairplot

On prend toutes les colonnes numériques du fichier (prix, stock, score) et on croise chaque paire entre elles automatiquement. Le résultat est une grande grille de graphiques. En une seule ligne de code, on a une vue d'ensemble complète de toutes les relations possibles entre les variables.

---

### `seaborns-5/` : Lineplot

Comme le graphique en lignes de Matplotlib, mais Seaborn calcule automatiquement une moyenne lissée si plusieurs produits ont la même date. On voit l'évolution du prix dans le temps de façon plus propre.

---

### `seaborns-6/` : Histogramme avec courbe de densité

Un histogramme classique des prix, mais avec en plus une courbe lissée par-dessus (appelée KDE). Cette courbe aide à voir la forme générale de la distribution sans être distrait par les variations barre par barre.

---

### `seaborns-7/` : Kdeplot

Uniquement la courbe de densité lissée, sans les barres. On trace une courbe par statut de disponibilité pour voir si les produits en stock ont des scores différents de ceux en rupture. Plus la courbe est haute à un endroit, plus il y a de produits avec ce score-là.

---

### `seaborns-8/` : Violinplot

Une sorte de boîte à moustaches, mais au lieu d'une simple boîte, on dessine la forme complète de la distribution. Si le violon est large en haut, c'est qu'il y a beaucoup de produits chers dans cette catégorie. Si le violon est large au milieu, les prix sont concentrés autour d'une valeur centrale.

---

### `seaborns-9/` : Countplot

Des barres qui comptent le nombre de produits, pas leur prix. Pour chaque catégorie, on voit combien de produits sont en stock, combien sont en rupture. C'est simple mais très lisible pour comparer les effectifs.

---

### `seaborns-10/` : Regplot

Un nuage de points avec une droite de régression tracée automatiquement dessus. Cette droite représente la tendance générale : si elle monte vers la droite, les produits chers ont tendance à avoir de meilleurs scores. Si elle est plate, il n'y a pas de lien entre les deux.

---

### `seaborns-11/` : Heatmap

Un tableau coloré. Chaque case correspond à la corrélation entre deux variables. Une case rouge foncé signifie que les deux variables évoluent vraiment ensemble. Une case bleu foncé signifie qu'elles évoluent en sens inverse. Une case pâle signifie qu'il n'y a pas de lien. Les chiffres dans les cases donnent la valeur exacte.

---

### `seaborns-12/` : Jointplot

Trois graphiques en un. Au centre, un nuage de points classique entre le prix et le score. En haut, un histogramme du score tout seul. À droite, un histogramme du prix tout seul. En une seule image, on voit à la fois la relation entre les deux variables et comment chacune se comporte de son côté.

---

### `tests/`, `final/`, `infos/`, `web/`
Autres dossiers de travaux réalisés en cours.
