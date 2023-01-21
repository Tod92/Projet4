from controllers.playerscontroller import PlayersController
from controllers.tournamentscontroller import TournamentsController


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
        #To quit
        elif choice == 4:
            return False
        return True

    def init_play_menu(self):
        while True:
            tournamentscontroller = TournamentsController(self.database,
                                                          self.menus,
                                                          self.views)
            tournaments = tournamentscontroller.list_tournaments()
            if tournaments == None:
                return None
            self.views.show_user(self.menus.choose_tournament)
            choice = self.views.prompt_choices(tournaments,
                                               back = True)
            #choix retour
            if choice == -1:
                return None
            else:
                tournament_id = tournaments[choice]._id
                self.game(tournament_id)


    def init_players_menu(self):
        while True:
            players = self.database.get_players()
            playerscontroller = PlayersController(players, self.menus, self.views)
            choice = self.views.prompt_choices(self.menus.players_management, back = True)
            #choix retour
            if choice == -1:
                return None
            #creation joueur
            elif choice == 0:
                newplayers = playerscontroller.create_player()
                self.database.save_players(newplayers)
            #liste joueurs
            elif choice == 1:
                newplayers = playerscontroller.list_players_choice()
                self.database.save_players(newplayers)

    def init_tournaments_menu(self):
        while True:
            tournamentscontroller = TournamentsController(self.database,
                                                          self.menus,
                                                          self.views)
            choice = self.views.prompt_choices(self.menus.tournaments_management,
                                               back = True)
            #choix retour
            if choice == -1:
                return None
            #creation tournoi
            elif choice == 0:
                tournamentscontroller.create_tournament()
            #liste tournois
            elif choice == 1:
                tournamentscontroller.list_tournaments_choice()


    def init_report_menu(self):
        pass

    def game(self,tournament_id):
        gamecontroller = GameController(self.database,
                                        self.menus,
                                        self.views,
                                        tournament_id)
        gamecontroller.run()

    def run(self):
        running = True
        while running:
            running = self.init_main_menu()
