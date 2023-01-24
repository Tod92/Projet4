


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

    def set_winner(self, match_index):
        """
        l'indice du match dans la liste matchs en entrée
        """
        match = self.tournament.turns[-1].matchs[match_index]
        player1 = match.player1
        player2 = match.player2
        temp_menu = [player1,player2]
        temp_menu.append(self.menus.draw)
        self.views.show_user(self.menus.pick_winner)
        choice = self.views.prompt_choices(temp_menu, back = True)
        #Retour
        if choice == -1:
            return None
        #Vainqueur = joueur 1
        elif choice == 0:
            p1score, p2score = WINNER_POINTS , 0
        #Vainqueur = joueur 2
        elif choice == 1:
            p1score, p2score = 0, WINNER_POINTS
        #match nul
        elif choice == 2:
            p1score, p2score = DRAW_POINTS , DRAW_POINTS
        result = ([match.player1, p1score], [match.player2, p2score])
        self.tournament.turns[-1].matchs.pop(match_index)
        self.tournament.turns[-1].matchs.append(result)
        #mise à jour des Scores
        self.update_turn_scores()

    def init_scores(self):
        return {p: 0 for p in self.tournament.players}

    def update_turn_scores(self, turn_number = "current"):
        """
        la methode parcours les resultats des matchs terminés pour reconstruire
        le dictionnaire scores du tour souhaité
        turn_number pour appliquer sur le tour souhaité
        """
        if turn_number == "current":
            turn_number = self.tournament.turn_number
        turn = self.tournament.turns[turn_number - 1]
        turn.scores = self.init_scores()
        for m in turn.matchs:
            #Condition pour atteindre les matchs terminés uniquement
            if type(m) == tuple:
                for e in m:
                    player = e[0]
                    score = e[1]
                    if score != 0:
                        turn.scores[player] += score
        self.update_tournament_scores()

    def update_tournament_scores(self):
        """la methode reconstruit le dictionnaire scores du tournois # -*- coding: utf-8 -*-
        faisant la somme de ceux de ses tours """
        self.tournament.scores = self.init_scores()
        for t in self.tournament.turns:
            for p in self.tournament.players:
                self.tournament.scores[p] += t.scores[p]

    def menu_start_turn(self):
        """
        """
        choice = self.views.prompt_choices(self.menus.start_turn)
        if choice == 0:
            self.tournament.turns[-1].start()

        elif choice == 1:
            return None

    def menu_active_turn(self):
        """
        """
        turn = self.tournament.turns[self.tournament.turn_number - 1]
        choice = self.views.prompt_choices(self.menus.active_turn)
        #Saisir le resultat d'un match
        if choice == 0:
            while True:
                started_matchs = [e for e in turn.matchs if type(e) != tuple]
                choice = self.views.prompt_choices(started_matchs, back = True)
                if choice == -1:
                    return None
                #Envoi de l'indice à la methode set_winner()
                #Il s'agit de l'indice dans matchs et non started_matchs
                match = started_matchs[choice]
                choice_in_matchs = turn.matchs.index(match)
                self.set_winner(choice_in_matchs)
                return None
        #Terminer le tour
        if choice == 1:
            #demande au tour de se cloturer s'il le peut
            if turn.closing() == False:
                self.views.show_user(self.menus.cant_close_turn)

        #Quitter
        elif choice == 2:
            return None

    def menu_gen_turn(self):
        """
        """
        choice = self.views.prompt_choices(self.menus.gen_turn)
        if choice == 0:
            name = TURN_NAME + str(len(self.tournament.turns) + 1)
            self.tournament.gen_next_turn(name)

        elif choice == 1:
            return None

    def run(self):
        self.load_tournaments()
        self.tournament = self.extract_tournament_from_list()

        while True:
            if self.tournament.is_finished == True:
                #TODO : indiquer tournoi terminé
                return None

            self.show_turn_details()
            turn_number = self.tournament.turn_number
            if turn_number == 0:
                self.menu_start_turn()
            else:
                turn = self.tournament.turns[turn_number - 1]
                if turn.is_started == False and turn.is_finished == False:
                    self.menu_start_turn()
                elif turn.is_started == True and turn.is_finished == False:
                    self.menu_active_turn()
                elif turn.is_started == True and turn.is_finished == True:
                    self.menu_gen_turn()
            self.save_tournament()








if __name__ == '__main__':
    main()
