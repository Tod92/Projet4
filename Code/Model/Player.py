import json, jsonpickle

SAVE_PATH = "Players.json"


class Player:
    """
    id : Identifiant National d'Echec
    """
    def __init__(self,id,firstname,lastname,birth):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth

    def __str__(self):
        return self.firstname + "" + self.lastname + " né(e) le " + str(self.birth)

def load_file():
    """
    Fonction qui ouvre le fichier de sauvegarde SAVE_PATH et retourne la liste
    de Joueurs
    Si l'ouverture du fichier ne fonctionne pas, écrit fichier avec liste vierge
    """
    try:
        with open(SAVE_PATH, 'r') as file:
            json_liste_joueurs = json.load(file)
        liste_joueurs = jsonpickle.decode(json_liste_joueurs)
    except:
        liste_joueurs = []
        json_liste_joueurs = jsonpickle.encode(liste_joueurs)
        with open(SAVE_PATH, 'w') as file:
            json.dump(json_liste_joueurs, file)
        print("enregistrement ok")

    return liste_joueurs

def save_file(liste_joueurs):
    """
    Fonction qui va serialiser la liste de jouurs en JSON puis écrire le
    fichier dans SAVE_PATH
    """
    json_liste_joueurs = jsonpickle.encode(liste_joueurs)
    with open(SAVE_PATH, 'w') as file:
        json.dump(json_liste_joueurs, file)
        print("enregistrement ok")


def save_player(player_object):
    liste_joueurs = load_file()
    liste_joueurs.append(player_object)
    save_file(liste_joueurs)

def main():
    joueur = Player("42","toto","leduc","01/01/2023")
    save_player(joueur)

if __name__ == '__main__':
    main()
