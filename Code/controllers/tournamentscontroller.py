

from models.tournament import Tournament


class TournamentsController:
    def __init__(self, database, menus, views):
        self.database = database
        self.menus = menus
        self.views = views
        self.tournaments = []
        self.players = []

    def load_tournaments(self):
        self.tournaments = self.database.get_tournaments()

    def save_tournaments(self):
        self.database.save_tournaments(self.tournaments)

    def load_players(self):
        self.players = self.database.get_players()

    def create_tournament(self):
        self.load_tournaments()
        #id détérminé par le nombre de tournois présents dans la liste
        id = len(self.tournaments)
        name = self.views.user_input("Nom du tournoi")
        place = self.views.user_input("Lieu du tournoi")
        start_date = self.views.user_input("Date de début")
        end_date = self.views.user_input("Date de fin")
        turn_number = 0
        players = []
        description = self.views.user_input("Description du tournoi")
        newtournament = Tournament(id,
                                  name,
                                  place,
                                  start_date,
                                  end_date,
                                  turn_number,
                                  players,
                                  description)

        self.tournaments.append(newtournament)
        self.save_tournaments()

    def sort_start_date(self):
        """
        renvoi liste de tournois par ordre de date début
        """
        #Tri de la liste par date de demarrage
        self.tournaments.sort(key = lambda x: x.start_date)

    def list_tournaments_choice(self):
        """
        Menu de choix parmis liste des tournois et renvoi vers
        manage_tournaments du joueur choisi
        """
        self.load_tournaments()
        if self.tournaments == []:
            self.views.show_user("Liste tournois vide")
            return None
        self.sort_start_date()
        choice = self.views.prompt_choices(self.tournaments, back = True)
        if choice == -1:
            return None
        else:
            tournament = self.tournaments.pop(choice)
            modified_tournament = self.manage_tournament(tournament)
            self.tournaments.append(modified_tournament)
            self.save_tournaments()


    def manage_tournament(self, tournament_object):
        """
        Affiche et permet de choisir l'element modifiable par l'utilisateur
        """
        choice = self.views.prompt_choices(self.menus.tournaments_modification,
                                           back = True)
        #choix retour
        if choice == -1:
            return tournament_object
        #choix nom
        elif choice == 0:
            tournament_object.name = self.views.user_input("Nom du tournoi")
        #choix Lieu
        elif choice == 1:
            tournament_object.place = self.views.user_input("Lieu du tournoi")
        #choix description
        elif choice == 2:
            tournament_object.description = self.views.user_input("Description du tournoi")
        #choix nombre de tour
        elif choice == 3:
            #nombre de tours non modifiable si tournoi démarré
            if tournament_object.turn_number != 0:
                self.views.show_user("Nombre de tours non modifiable. Tournoi démarré")
                return tournament_object
            tournament_object.nb_turns = self.views.user_input("Nombre de tours")
        elif choice == 4:
            tournament_object = self.add_player_to_tournament(tournament_object)

        return tournament_object

    def check_player_chess_id(self, player, players_list):
        """
        returns True if player chess id found in player list
        """
        for p in players_list:
            if p.chess_id == player.chess_id:
                return True
        return False

    def add_player_to_tournament(self, tournament_object):
        """
        """
        self.load_players()
        if self.players == []:
            self.views.show_user("Liste joueurs vide")
            return tournament_object

        self.views.show_user("Selectionner le joueur à ajouter au tournoi")
        choice = self.views.prompt_choices(self.players, back = True)
        if choice == -1:
            return tournament_object
        player = self.players.pop(choice)
        if self.check_player_chess_id(player, tournament_object.players):
            self.views.show_user("Ajout impossible : chess_id deja present")
            return tournament_object
        tournament_object.players.append(player)
        return tournament_object
