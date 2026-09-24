"""
Définition des routes de l'application.
1 : chaque route correspond à un graphique
2 : on appelle le service charts pour générer l'image
3 : on renvoie l'image au client
"""
from charts.charts import generer

def register_routes(app):

    @app.route("/boxplot")
    def boxplot():
        return generer("boxplot")

    @app.route("/scatterplot")
    def scatterplot():
        return generer("scatterplot")

    @app.route("/histplot")
    def histplot():
        return generer("histplot")

    @app.route("/countplot")
    def countplot():
        return generer("countplot")

    @app.route("/heatmap")
    def heatmap():
        return generer("heatmap")

    @app.route("/violinplot")
    def violinplot():
        return generer("violinplot")
