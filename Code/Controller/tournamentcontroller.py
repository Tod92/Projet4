from Model import tournament
from View import userinterface


START_DATE_WAIT_MSG = "En attente du démarrage du premier tour"
END_DATE_WAIT_MSG = "En attente de la fin du tournoi"

MENU_MODIFICATION = ["Nom",
                     "Lieu",
                     "Description"]


def tournament_creation():
    #id détérminé par le nombre de tournois présents dans le fichier json
    id = len(tournament.load_file())
    name = userinterface.user_input("Nom du tournoi")
    place = userinterface.user_input("Lieu du tournoi")
    start_date = START_DATE_WAIT_MSG
    end_date = END_DATE_WAIT_MSG
    turn_number = 0
    players_list = []
    description = userinterface.user_input("Description du tournoi")
    newtournament = tournament.Tournament(id,
                                          name,
                                          place,
                                          start_date,
                                          end_date,
                                          turn_number,
                                          players_list,
                                          description)

    is_saved = tournament.save_tournament(newtournament)
    return is_saved

def tournament_list():
    """
    Liste les tournois par ordre de création,
    renvoi l'objet tournament choisi ou None si retour
    """
    liste_tournois = tournament.load_file()
    ##Tri de la liste par date de demarrage
    #liste_tournois.sort(key = lambda x: x.start_date)
    choix = userinterface.pick(liste_tournois, back = True)
    if choix == -1:
        return None
    return liste_tournois[choix]


def tournament_modification(tournament_object):
    """
    Affiche et permet de choisir l'element modifiable par l'utilisateur
    """
    choix = userinterface.pick(MENU_MODIFICATION, back = True)
    if choix == -1:
        return None
    elif choix == 0:
        tournament_object.name = userinterface.user_input("Nom du tournoi")
    elif choix == 1:
        tournament_object.place = userinterface.user_input("Lieu du tournoi")
    elif choix == 2:
        tournament_object.description = userinterface.user_input("Description du tournoi")
    tournament.save_tournament(tournament_object)
