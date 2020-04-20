# Installation Python API:


## Contenu
 - `app`: dossier contenant les méthodes de l'API
    - `routes.py`: ensemble des methodes de l'API
 - `data`: dossier contenant la *base de données* ainsi que les musiques utilisées dans cette base de données (musique qui pourront être utilisées pour réaliser une reconnaissance)
 - `dejavu`: module de reconnaissance de musique ([source](https://github.com/datawookie/dejavu))
 - `venv`: environnement python pour ce projet
 - `temp`: dossier temproraire utilisé par l'API lors de la reconnaissance des chansons 
 - `requirements.txt`: liste des modules nécessaire au fonctionnement d'API
 - `run.py`: fichier pour lancer le server  

## 1. Prérequis
 - Système Linux (nous ne sommes pas parvenus à le faire fonctionner sous Windows)
 - Avoir installé [`ffmpeg`](https://github.com/FFmpeg/FFmpeg)
 - Avoir un gestionnaire de bases de données type MySQL. 



## 2. Installation
 1. Télécharger le projet:
    - Avec *git* : `git clone https://github.com/alexandreb09/SongToLyrics_Python_Flask.git`
    - Avec un navigateur depuis *GitHub*: [alexandreb09/SongToLyrics_Python_Flask](https://github.com/alexandreb09/SongToLyrics_Python_Flask)
 2. Depuis un terminal, se rendre dans la racine du dossier: `cd SongToLyrics_Python_Flask`
 3. Créer un environnement Python: `python3 -m venv venv`
 4. Activer l'environnement Python: `source venv/bin/activate`
 5. Installer les dépendances: `pip install -r requirements.txt`
 6. Créer une base de données MySQL (ici "`song_to_lyrics`"):

        mysql -u root -p
        Enter password: **********
        mysql> CREATE DATABASE IF NOT EXISTS song_to_lyrics;

 7. Importer la base de données `database\song_to_lyrics.sql`. Cette base de données se compose des 5 morceaux utilisés par défaut dans le module `dejavu`.
 
 8. Lancer le server: `python run.py`
 
 
 
 ## Notes:
 
 - Il est important de lancer le server sur l'adresse `0.0.0.0` afin qu'il soit visible sur l'ensemble des appareils connectés à ce réseau. 

 - Sur l'application Android doit être connectée au même réseau que le server.

 - Il est nécessaire de connaître l'adresse IP de son réseau. Sous Débian, cela peut facilement sur l'Icone *Wifi* en haut à droite -> *Paramètres wifi* -> dans la nouvelle fenêtre sélectionné les *paramêtres* du réseau puis l'adresse *IPv4* apparaît.

 - L'appliation ne peut bien sur reconnaître que les chansons présentes dans la BDD. Le présent projet n'a pas pour intérêt de mettre en place une grande quantité de musique bien que cela soit en réalité possible. Pour **ajouter des musiques supplémentaires**, veuillez vous référer au projet originel [dejavu](https://github.com/datawookie/dejavu)

 - L'application Android `SongToLyrics` met à disposition de l'utilisateur une page de connexion au serveur si celle-ci n'est pas fonctionnelle. Elle permet en outre de tester la connexion au server.