


WINNER_POINTS = 1
DRAW_POINTS = 0.5
TURN_NAME = "Round"


class GameController:
    """
    Controller pour lancer un tournoi
    """
    def __init__(self, database, menus, views, tournament_id):
        self.database = database
        self.menus = menus
        self.views = views
        self._tournament_id = tournament_id
        self.tournaments = []


    def load_tournaments(self):
        self.tournaments = self.database.get_tournaments()

    def save_tournaments(self):
        self.database.save_tournaments(self.tournaments)

    def extract_tournament_from_list(self):
        """
        Ouvre la liste locale tournaments et en extrait le tournoi voulu via
        son id. None si non trouvé.
        !le tournoi devra etre append à la liste avant sauvegarde!
        """
        #recuperation de l'index
        for n in range(len(self.tournaments)):
            if self.tournaments[n]._id == self._tournament_id:
                index = n
        return self.tournaments.pop(index)

    def save_tournament(self):
        """
        réinjecte le tournoi dans la liste tournaments et sauvegarde cette
        derniere
        """
        self.tournaments.append(self.tournament)
        print("Jenvoie ca a save_tournaments : ", self.tournaments)
        self.save_tournaments()
        #suppression du tournoi de la liste après avoir sauvegardé la liste
        self.tournaments.pop()

    def show_turn_details(self):
        """
        Informations du tournoi et tour pour le menu de jeu
        """
        turn_number = self.tournament.turn_number
        if turn_number > 0:
            turn = self.tournament.turns[turn_number - 1]
            turn_details = turn.name + "\n"
            #les matchs terminés sont stockés sous forme de tuples
            started_matchs = [e for e in turn.matchs if type(e) != tuple]
            finished_matchs = [e for e in turn.matchs if type(e) == tuple]
            turn_details += self.menus.started_matchs + str(started_matchs)
            turn_details += self.menus.finished_matchs + str(finished_matchs)
        else:
            turn_details = self.menus.turn_not_started

        result = "Tournoi : " + str(self.tournament.name + "\n")
        result += "Scores : " + str(self.tournament.scores) + "\n"
        result += str(turn_details)
        self.views.show_user(result)



    def menu_first_start(self):
        """
        """
        choice = self.views.prompt_choices(self.menus.first_start)
        if choice == 0:
            name = TURN_NAME + str(len(self.tournament.turns) + 1)
            self.tournament.gen_next_turn(name)

        elif choice == 1:
            print("quand meme !")
            return None

    def menu_gen_turn(self):
        """
        """
        print(self.tournament)
        print(self.tournaments)
        print(self.tournament.turns)
        print(self.tournament.turns[0].name)
        print(self.tournament.turns[0].matchs)
        exit()


    def run(self):
        self.load_tournaments()
        self.tournament = self.extract_tournament_from_list()
        # print("J'ai reussi à extraire le tournoi : ", self.tournament)
        # print("mon self.tournaments : ", self.tournaments)
        # print("mon tournament : ", self.tournament)
        while True:
            if self.tournament.is_finished == True:
                return None
            self.show_turn_details()
            if self.tournament.turn_number == 0:
                self.menu_first_start()
            else:
                self.menu_gen_turn()

            self.save_tournament()







# def closing(match, winner):
#     """
#     winner : joueur ayant remporté le match. 0 : player1, 1 : player2.
#     si nul, winner = 2
#     Retourne un tuple contenant deux listes, chacune
#     contenant deux éléments : un joueur et un score
#     """
#     if winner == 0:
#         p1score, p2score = 1 , 0
#     elif winner == 1:
#         p1score, p2score = 0, 1
#     elif winner == 2:
#         p1score, p2score = 0.5 , 0.5
#     return ([match.player1, p1score], [match.player2, p2score])
#
#
#
# if __name__ == '__main__':
#     main()
