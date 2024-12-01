# ue19-lab-05


### Jokes Fetcher
Une application Python qui interroge une API publique pour récupérer une blague aléatoire et l'afficher dans le terminal.

### Aperçu
Le but de cette application est de rendre votre journée un peu plus joyeuse en vous racontant une blague issue de l'API JokesAPI. Qu'il s'agisse de blagues courtes ou de dialogues humoristiques, notre application vous garantit une touche de légèreté en quelques secondes.

### Fonctionnalités
- Obtenez une blague aléatoire à chaque exécution.
- Prend en charge différents types de blagues (simples ou en deux parties).
- Facile à configurer et à exécuter.
-Compatible avec Docker pour une exécution simplifiée.

### Prérequis
Avant de commencer, assurez-vous d'avoir installé :

- Python : Version 3.8 ou supérieure.
- pip : Gestionnaire de paquets Python.
- Docker (optionnel) : Si vous souhaitez exécuter l'application dans un conteneur.
  
### Installation
Étape 1 : Clonez ce repository :
git clone https://github.com/<votre-utilisateur>/ue19-lab-05.git
cd ue19-lab-05

Étape 2 : Installez les dépendances :

pip install -r requirements.txt

### Utilisation
Pour exécuter l'application localement :
python app.py

### Exemple de sortie :
Voici une blague pour vous :
Pourquoi les mathématiques sont-elles tristes ? ... Parce qu'elles ont beaucoup de problèmes.

### Développement avec Docker
Étape 1 : Construisez l'image Docker :
docker build -t jokes-fetcher .

Étape 2 : Exécutez le conteneur :
docker run --rm jokes-fetcher


Effectuez vos modifications et commitez-les :
git commit -m "Ajout d'une nouvelle fonctionnalité"

Poussez vos changements :
git push origin feature/nom-de-la-fonctionnalité
Ouvrez une Pull Request.

### Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.
