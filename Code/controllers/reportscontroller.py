from controllers.playerscontroller import PlayersController

class ReportsController:
    """
    Controller pour le menu rapports
    """
    def __init__(self, database, menus, views):
        self.database = database
        self.menus = menus
        self.views = views

    def all_players_alpha(self):
        players = self.database.get_players()
        playerscontroller = PlayersController(players, self.menus, self.views)

        
    def run(self):
        while True:
            choice = self.views.prompt_choices(self.menus.reports, back = True)
            #Choix retour
            if choice == -1:
                return None
            #Liste de tous les joueurs par ordre alphabétique
            elif choice == 0:
                pass
            #Liste de tous les tournois
            elif choice == 0:
                pass
            #Nom et date d'un tournoi donné
            elif choice == 0:
                pass
            #Liste des joueurs du tournoi par ordre alphabétique
            elif choice == 0:
                pass
            #Liste de tous les tours du tournoi et de tous les matchs du tour
            elif choice == 0:
                pass


if __name__ == '__main__':
    main()
