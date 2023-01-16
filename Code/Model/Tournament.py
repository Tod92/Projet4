import json, jsonpickle

SAVE_PATH = "Tournaments.json"

class Tournament:
    """
    """
    def __init__(self, id, name, place, start_date, end_date, turn_number,
                players_list, description, nb_turns = 4):
        self._id = id
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.turn_number = turn_number
        self.turn_list = []
        self.players_list = players_list
        self.description = description
        self.nb_turns = nb_turns

    def __str__(self):
        result = "Tournoi (id :" + str(self._id) + ")\n"
        result += "Nom : " + self.name + "\n"
        result += "Lieu : " + self.place + "\n"
        result += "Description : " + self.description + "\n"
        result += "Date de debut : " + self.start_date + "\n"
        result += "Date de fin : " + self.end_date + "\n"
        result += "Nombre de tours : " + str(self.nb_turns) + "\n"
        result += "Tour actuel : " + str(self.turn_number) + "\n"
        result += "Participants : " + str(self.players_list)

        return result


def load_file():
    """
    Fonction qui ouvre le fichier de sauvegarde SAVE_PATH et retourne la liste
    de tournois
    Si l'ouverture du fichier ne fonctionne pas, écrit fichier avec liste vierge
    """
    try:
        with open(SAVE_PATH, 'r') as file:
            json_liste_tournois = json.load(file)
        liste_tournois = jsonpickle.decode(json_liste_tournois)
    except:
        liste_tournois = []
        json_liste_tournois = jsonpickle.encode(liste_tournois)
        with open(SAVE_PATH, 'w') as file:
            json.dump(json_liste_tournois, file)
        print("enregistrement ok")

    return liste_tournois

def save_file(liste_tournois):
    """
    Fonction qui va serialiser la liste de joueurs en JSON puis écrire le
    fichier dans SAVE_PATH
    """
    json_liste_tournois = jsonpickle.encode(liste_tournois)
    with open(SAVE_PATH, 'w') as file:
        json.dump(json_liste_tournois, file)
        print("enregistrement ok")
    return True

def save_tournament(tournament_object):
    liste_tournois = load_file()
    #suppression du tournois à remplacer avec même id
    for i in range(len(liste_tournois)):
        if liste_tournois[i]._id == tournament_object._id:
            liste_tournois.pop(i)
            break
    liste_tournois.append(tournament_object)
    save_file(liste_tournois)
