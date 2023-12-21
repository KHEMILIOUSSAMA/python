import os
import shutil
from datetime import datetime
import sys

def init():
    suivi_directory = 'suivi'

    #verifier si lee répertoire existe déja
    if not os.path.exists(suivi_directory):
        os.makedirs(suivi_directory)
        print("Suivi initialisé dans le répertoire de travail.")
    else:
         print("Le suivi existe déjà.")  

def add(file_name):
    suivi_directory = 'suivi'

    #Vérifie si le suivi a été initialisé
    if not os.path.exists(suivi_directory):
       print("Le suivi n'est pas initialisé. Utilisez 'init' d'abord.")
       return
    
    # Copie le fichier dans le répertoire de suivi
    shutil.copy(file_name, os.path.join(suivi_directory, file_name))
    print(f"Fichier {file_name} ajouté au suivi.")

def commit(message):
    suivi_directory = 'suivi'    

    # Vérifie si le suivi a été initialisé

    if not os.path.exists(suivi_directory):
        print("Le suivi n'est pas initialisé. Utilisez 'init' d'abord.")
        return
    
    # Crée un sous-répertoire pour la version
    version_dir = os.path.join(suivi_directory, f"version_{datetime.now().strftime('%Y%m%d%H%M%S')}")
    os.makedirs(version_dir)
    
    # Copie tous les fichiers du suivi dans le sous-répertoire de version
    for file_name in os.listdir(suivi_directory):
        file_path = os.path.join(suivi_directory, file_name)
        if os.path.isfile(file_path):
            shutil.copy(file_path, version_dir)

    # Crée un fichier de description de version
    with open(os.path.join(version_dir, 'description.txt'), 'w') as description_file:
        description_file.write(message)

    print(f"Version créée avec succès.") 



def log():
    suivi_directory = 'suivi'

    # Vérifie si le suivi a été initialisé
    if not os.path.exists(suivi_directory):
        print("Le suivi n'est pas initialisé. Utilisez 'init' d'abord.")
        return

    print("Historique des versions :")
    for version_dir in sorted(os.listdir(suivi_directory)):
        version_path = os.path.join(suivi_directory, version_dir)
        if os.path.isdir(version_path):
            version_number = version_dir.split('_')[1]

            # Récupère la date à partir du nom du répertoire
            version_date = datetime.strptime(version_number, '%Y%m%d%H%M%S').strftime('%Y-%m-%d')

            # Récupère la description de version à partir du fichier de description
            with open(os.path.join(version_path, 'description.txt')) as description_file:
                version_description = description_file.read()

            print(f"Version {version_number} - \"{version_description}\" ({version_date})")

def checkout(version_number):
    suivi_directory = 'suivi'

    # Vérifie si le suivi a été initialisé
    if not os.path.exists(suivi_directory):
        print("Le suivi n'est pas initialisé. Utilisez 'init' d'abord.")
        return

    # Vérifie si le numéro de version est valide
    version_dir = os.path.join(suivi_directory, f"version_{version_number}")
    if not os.path.exists(version_dir):
        print(f"La version {version_number} n'existe pas.")
        return

    # Restaure la version en copiant les fichiers du sous-répertoire de version vers le suivi
    for file_name in os.listdir(version_dir):
        file_path = os.path.join(version_dir, file_name)
        if os.path.isfile(file_path):
            shutil.copy(file_path, os.path.join(suivi_directory, file_name))

    print(f"Restauration de Version {version_number} réussie.")