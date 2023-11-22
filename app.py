from flask import Flask, render_template

app = Flask(__name__)

# Définir une route pour la page d'accueil
@app.route('/')
def home():
    return 'Bienvenue sur mon site web en Python !'

# Définir une route pour une page avec un modèle HTML
@app.route('/page')
def page():
    # Vous pouvez créer un dossier "templates" dans le même répertoire que votre script
    # et y placer un fichier HTML nommé "page.html" avec le contenu que vous souhaitez afficher.
    return render_template('page.html')

if __name__ == '__main__':
    # Démarrer l'application Flask
    app.run(debug=True)
