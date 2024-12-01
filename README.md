# ue19-lab-05


# Jokes Fetcher Application

Description :
Cette application interroge une API publique (JokesAPI) pour récupérer et afficher une blague aléatoire.

Prérequis :
- Python 3.8 ou supérieur
- `pip` pour installer les dépendances
- Docker (optionnel, pour exécuter l'application dans un conteneur)

Installation :
1. Clonez ce repository :
   ```bash
   git clone https://github.com/Supianbek/ue19-lab-05.git
   cd ue19-lab-05

Installez les dépendances :
pip install -r requirements.txt

Pour exécuter le script :
python app.py

Avec docker :
-Construire l'image Docker : 
docker build -t jokes-fetcher .
-Executer le programme :
docker run --rm jokes-fetcher

