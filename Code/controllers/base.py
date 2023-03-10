from controllers.playerscontroller import PlayersController
from controllers.tournamentscontroller import TournamentsController
from controllers.gamecontroller import GameController
from controllers.reportscontroller import ReportsController


class Controller:
    """
    Main controller
    Gere le menu principal et premiers sous menus
    """
    def __init__(self, database, menus, views):
        self.database = database
        self.menus = menus
        self.views = views

    def init_main_menu(self):
        choice = self.views.prompt_choices(self.menus.main)
        if choice == 0:
            self.init_play_menu()
        elif choice == 1:
            self.init_players_menu()
        elif choice == 2:
            self.init_tournaments_menu()
        elif choice == 3:
            self.init_report_menu()
        # To quit
        elif choice == 4:
            return False
        return True

    def init_play_menu(self):
        while True:
            tournamentscontroller = TournamentsController(self.database,
                                                          self.menus,
                                                          self.views)
            tournaments = tournamentscontroller.list_tournaments()
            if tournaments is None:
                return None
            self.views.show_user(self.menus.choose_tournament)
            choice = self.views.prompt_choices(tournaments,
                                               back=True)
            # Choix retour
            if choice == -1:
                return None
            else:
                if tournaments[choice].is_playable() is False:
                    print("TOURNOI NON JOUABLE")
                    return None
                tournament_id = tournaments[choice]._id
                self.game(tournament_id)

    def init_players_menu(self):
        while True:
            players = self.database.get_players()
            playerscontroller = PlayersController(players, self.menus, self.views)
            choice = self.views.prompt_choices(self.menus.players_management, back=True)
            # Choix retour
            if choice == -1:
                return None
            # Nouveau joueur
            elif choice == 0:
                newplayers = playerscontroller.create_player()
                self.database.save_players(newplayers)
            # Liste joueurs
            elif choice == 1:
                newplayers = playerscontroller.list_players_choice()
                self.database.save_players(newplayers)

    def init_tournaments_menu(self):
        while True:
            tournamentscontroller = TournamentsController(self.database,
                                                          self.menus,
                                                          self.views)
            choice = self.views.prompt_choices(self.menus.tournaments_management,
                                               back=True)
            # Choix retour
            if choice == -1:
                return None
            # Creation tournoi
            elif choice == 0:
                tournamentscontroller.create_tournament()
            # Liste tournois
            elif choice == 1:
                tournamentscontroller.list_tournaments_choice()

    def init_report_menu(self):
        reportscontroller = ReportsController(self.database,
                                              self.menus,
                                              self.views)
        reportscontroller.run()

    def game(self, tournament_id):
        gamecontroller = GameController(self.database,
                                        self.menus,
                                        self.views,
                                        tournament_id)
        gamecontroller.run()

    def run(self):
        running = True
        while running:
            running = self.init_main_menu()
