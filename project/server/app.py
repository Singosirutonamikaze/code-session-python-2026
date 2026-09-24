"""
Point d'entrée du serveur.
1 : on crée l'application Flask
2 : on active la protection CSRF
3 : on enregistre les routes
4 : on lance le serveur
"""
import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from routes.routes import register_routes

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "cle-secrete-par-defaut-developpement")

CSRFProtect(app)

register_routes(app)

if __name__ == "__main__":
    mode_debug = os.getenv("FLASK_DEBUG", "false").lower() in ("true", "1")
    app.run(debug=mode_debug, port=5000)
