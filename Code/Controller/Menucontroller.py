from View import userinterface
from Controller import playercontroller, tournamentcontroller,  matchcontroller


MENU_PRINCIPAL = ["Gestion Joueurs",
                  "Gestion Tournois",
                  "Rapports",
                  "Quitter"]

GESTION_JOUEURS = ["Nouveau joueur",
                   "Liste joueurs"]

GESTION_TOURNOIS = ["Nouveau Tournoi",
                    "Liste tournois"]

MENU_JOUEUR = ["Modifier",
               "Supprimer"]

MENU_TOURNOI = ["Modifier informations tournoi",
                "Participants",
                "Tours"]

DRAW = "Match nul"
WINNER_QUESTION = "Indiquer le vainqueur du match"


def match_menu(match_obj):
    menu_match = [match_obj.player1, match_obj.player2, DRAW]
    while True:
        userinterface.affiche(WINNER_QUESTION)
        choix = userinterface.pick(menu_match, back = True)
        if choix == -1:
            break
        match_tuple = matchcontroller.closing(match_obj, choix)
        return match_tuple


def player_menu(player_object):
    while True:
        choix = userinterface.pick(MENU_JOUEUR, back = True)
        if choix == -1:
            break
        elif choix == 0:
            #Todo : modif joueur
            pass
        elif choix == 1:
            #Todo : confirmation et suppression
            pass


def tournament_menu(tournament_object):
    while True:
        userinterface.affiche(tournament_object)
        choix = userinterface.pick(MENU_TOURNOI, back = True)
        if choix == -1:
            break
        elif choix == 0:
            tournamentcontroller.tournament_modification(tournament_object)
        elif choix == 1:
            tournamentcontroller.player_management(tournament_object)
        elif choix == 2:
            tournamentcontroller.turn_management(tournament_object)


def player_management():
    while True:
        choix = userinterface.pick(GESTION_JOUEURS, back = True)
        if choix == -1:
            break
        elif choix == 0:
            playercontroller.player_creation()
        elif choix == 1:
            joueur = playercontroller.player_list()
            if joueur == None:
                break
            else:
                player_menu(joueur)




def tournament_management():
    while True:
        choix = userinterface.pick(GESTION_TOURNOIS, back = True)
        if choix == -1:
            break
        elif choix == 0:
            tournamentcontroller.tournament_creation()
        elif choix == 1:
            tournoi = tournamentcontroller.tournament_list()
            if tournoi == None:
                break
            else:
                tournament_menu(tournoi)

def main():
    while True:
        choix = userinterface.pick(MENU_PRINCIPAL)
        if choix == 0:
            player_management()
        elif choix == 1:
            tournament_management()
        else:
            print(M.TODO)
