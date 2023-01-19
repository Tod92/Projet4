from controllers.playerscontroller import PlayersController
from controllers.tournamentscontroller import TournamentsController


class Controller:
    """
    Main controller
    database management
    """
    def __init__(self, database, menus, views):
        self.database = database
        self.menus = menus
        self.views = views

    def init_main_menu(self):
        print(self.menus.main)
        choice = self.views.prompt_choices(self.menus.main)
        if choice == 0:
            self.init_players_menu()
        elif choice == 1:
            self.init_tournaments_menu()
        elif choice == 2:
            self.init_report_menu()
        #To quit
        elif choice == 3:
            return False
        return True


    def init_players_menu(self):
        while True:
            players = self.database.get_players()
            playerscontroller = PlayersController(players, self.views)
            choice = self.views.prompt_choices(self.menus.players_management,back = True)
            if choice == -1:
                return None
            elif choice == 0:
                newplayers = playerscontroller.create_player()
                self.database.save_players(newplayers)
            elif choice == 1:
                newplayers = playerscontroller.list_players()
                self.database.save_players(newplayers)
    def init_tournaments_menu(self):
        pass

    def init_report_menu(self):
        pass

    def run(self):
        running = True
        while running:
            running = self.init_main_menu()


# from Model import tournament
# from View import userinterface
# from Controller import playercontroller


# START_DATE_WAIT_MSG = "En attente du démarrage du premier tour"
# END_DATE_WAIT_MSG = "En attente de la fin du tournoi"
#
# MENU_MODIFICATION = ["Nom",
#                      "Lieu",
#                      "Description",
#                      "Nombre de tours"]
#
# MENU_JOUEURS = ["Ajouter joueur au tournoi"]
