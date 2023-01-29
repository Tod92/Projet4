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
        playerscontroller = PlayersController(players,
                                              self.menus,
                                              self.views)
        players_sorted = playerscontroller.sort_lastname()
        report = ""
        for player in players_sorted:
            report += "(" + str(player.chess_id) + ") "
            report += str(player.lastname) + " "
            report += str(player.firstname) + "\n"
        self.views.gen_report(report)

    def all_tournaments(self):
        tournaments = self.database.get_tournaments()
        report = ""
        for t in tournaments:
            report += str(t.name) + " "
            report += "Lieu du tournoi : " + str(t.place) + " "
            report += "Description : " + str(t.description) + "\n"
        self.views.gen_report(report)

    def pick_tournament(self, tournaments):
        choice = self.views.prompt_choices(tournaments, back = True)
        if choice == -1:
            return None
        else:
            return tournaments[choice]

    def tournament_name_date(self):
        tournaments = self.database.get_tournaments()
        tournament = self.pick_tournament(tournaments)
        report = tournament.name + " "
        report += "debut : " + tournament.start_date + " "
        report += "fin : " + tournament.end_date
        self.views.gen_report(report)

    def tournaments_players_alpha(self):
        tournaments = self.database.get_tournaments()
        tournament = self.pick_tournament(tournaments)
        #Instanciation du playerscontroller uniquement avec les joueurs
        #du tournoi choisi
        players = tournament.players
        playerscontroller = PlayersController(players,
                                              self.menus,
                                              self.views)
        players_sorted = playerscontroller.sort_lastname()
        report = ""
        for player in players_sorted:
            report += "(" + str(player.chess_id) + ") "
            report += str(player.lastname) + " "
            report += str(player.firstname) + "\n"
        self.views.gen_report(report)

    def run(self):
        while True:
            choice = self.views.prompt_choices(self.menus.reports, back = True)
            #Choix retour
            if choice == -1:
                return None
            #Liste de tous les joueurs par ordre alphabétique
            elif choice == 0:
                self.all_players_alpha()
            #Liste de tous les tournois
            elif choice == 1:
                self.all_tournaments()
            #Nom et date d'un tournoi donné
            elif choice == 2:
                self.tournament_name_date()
            #Liste des joueurs du tournoi par ordre alphabétique
            elif choice == 3:
                self.tournaments_players_alpha()
            #Liste de tous les tours du tournoi et de tous les matchs du tour
            elif choice == 4:
                pass


if __name__ == '__main__':
    main()
