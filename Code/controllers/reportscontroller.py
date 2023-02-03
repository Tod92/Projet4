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

    def all_turns_and_matchs(self):
            tournaments = self.database.get_tournaments()
            tournament = self.pick_tournament(tournaments)
            report = ""
            for turn in tournament.turns:
                 report += str(turn.name) + " (" + self.turn_status(turn)
                 report += ") : \n"
                 for m in turn.matchs:
                     if type(m) == tuple:
                         p1_name = m[0][0]
                         p1_score = m[0][1]
                         p2_name = m[1][0]
                         p2_score = m[1][1]
                         report += str(p1_name) + " : "
                         report += str(p1_score) + " / "
                         report += str(p1_name) + " : "
                         report += str(p1_score) + "\n"
                     else:
                         report += str(m) + "\n"
            self.views.gen_report(report)

    def turn_status(self, turn_obj):
        """
        Renvoi l'état du tour (str) : non démarré, démarré ou terminé.
        Y ajoute la date et heure selon l'état
        """
        result = "!"
        if turn_obj.is_finished == True:
            result = "terminé le "
            result += turn_obj.end_time.strftime("%d/%m/%Y %H:%M:%S")
        elif turn_obj.is_started == True:
            result = "démarré le "
            result += turn_obj.start_time.strftime("%d/%m/%Y %H:%M:%S")
        else:
            result = "non démarré"
        return result

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
                self.all_turns_and_matchs()


if __name__ == '__main__':
    main()
