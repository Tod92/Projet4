from View import Userinterface
from Controller import Playercreation


MENU_PRINCIPAL = ["Gestion Joueurs",
"Gestion Tournois",
"Rapports",
"Quitter"]

GESTION_JOUEURS = ["Nouveau joueur",
"Liste joueurs"]


def player_menu():
    while True:
        choix = Userinterface.pick(GESTION_JOUEURS,  back = True)
        if choix == 0:
            Playercreation.main()
        if choix == 1:
            return None


def main():
    while True:
        choix = Userinterface.pick(MENU_PRINCIPAL)
        if choix == 0:
            player_menu()
        if choix == 1:
            tournament_menu()
        else:
            print(M.TODO)
