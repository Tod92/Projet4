from View import Userinterface
from Controller import Playercontroller


MENU_PRINCIPAL = ["Gestion Joueurs",
"Gestion Tournois",
"Rapports",
"Quitter"]

GESTION_JOUEURS = ["Nouveau joueur",
"Liste joueurs"]

MENU_JOUEUR = ["Modifier",
"Supprimer"]

def player_menu(player_object):
    while True:
        choix = Userinterface.pick(MENU_JOUEUR, back = True)
        if choix == -1:
            break
        elif choix == 0:
            #Todo : modif joueur
            pass
        elif choix == 1:
            #Todo : confirmation et suppression
            pass

def player_management():
    while True:
        choix = Userinterface.pick(GESTION_JOUEURS, back = True)
        if choix == 0:
            Playercontroller.player_creation()
        elif choix == 1:
            joueur = Playercontroller.player_list()
            if joueur == None:
                break
            else:
                player_menu(joueur)

        elif choix == -1:
            break

def main():
    while True:
        choix = Userinterface.pick(MENU_PRINCIPAL)
        if choix == 0:
            player_management()
        elif choix == 1:
            tournament_menu()
        else:
            print(M.TODO)
