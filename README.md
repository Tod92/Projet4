# Projet 4 - Développez un programme logiciel en Python


Ce script Python a pout but d'assister les organisateurs d'un club d'échec dans la mise en place de tournois. Il va notamment générer les tours et matchs d'un tournoi. Il ne néçessite pas de connection internet, les données sont sauvegardées automatiquement à chaque action en local sur la machine.



## Installation

* Installer Python 3.10.3 :
 https://www.python.org/downloads/release/python-3103/  
  _Compatibilité avec d'autres versions probable mais non testée_

* Télécharger et extraire le repository suivant depuis github :\
https://github.com/Tod92/Projet4

* Se positionner dans le répértoire où le repository a été extrait :\
  `..\Projet4-main\`

* Créer l'environnement virtuel :\
  `python -m venv env`

* Activer l'environnement virtuel :\
  `..\Projet4-main\env\Scripts\activate.bat`

* Installer les packages Python néçessaire à l'execution du script :\
  `(env)..\Projet4-main\pip install -r requirements.txt`

* Installation terminée. Désactivation de l'environnement virtuel :\
  `deactivate`

## Execution du Script

* L'environnement virtuel doit etre activé :\
  `..\Projet4-main\env\Scripts\activate.bat`

* Executer le script python :\
  `..\Projet4-main\python chess.py`


* Penser à désactiver l'environnement virtuel :\
  `deactivate`

## Générer les rapports flake8-html

* Se positionner dans le répertoire "Code" :\
  `flake8 --format=html --htmldir=flake8_rapport --max-line-length=119`

* Les rapports HTML sont a récupérer dans le répértoire ..\Code\flake8_rapport

## Précisions

L'identifiant national d'échec de chaque joueur devra etre utilisé lors de la saisie dans le système de ces derniers.

L'état actuel du script ne permet le démarrage de tournois que si le nombre de joueurs inscrits à ces derniers est pair.

Script testé uniquement en environnement windows pour le moment.

## Format des données

Les données sont stockées au format JSON via l'utilisation de la librairie Python jsonpickle. Ce format permet le stockage (non crypté) des differents objets Python dans les fichiers "Players.json" et "Tournaments.json"




## Historique

* 01/02/2023 : Finalisation projet et documentation
* 27/01/2023 : Rapports fonnctionnels
* 24/01/2023 : Lancement tournoi fonctionnel
* 20/01/2023 : Fin refonte
* 18/01/2023 : Démarrage renfonte Model/View/Controller
* 17/01/2023 : Creations joueurs et tournois
* 14/01/2023 : Démarrage du projet

## Credits
Projet réalisé par Thomas DERUERE\
Assisté par Idriss BEN GELOUNE (Mentor Openclassrooms)
