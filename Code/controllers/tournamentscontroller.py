from models.tournament import Tournament


class TournamentsController:
    def __init__(self, tournaments, views):
        self.tournaments = tournaments
        self.views = views

    def create_tournament(self):
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
        return self.tournaments

    def sort_start_date(self):
        """
        renvoi liste de tournois par ordre de date début
        """
        #Tri de la liste par date de demarrage
        self.tournaments.sort(key = lambda x: x.start_date)
        return self.tournaments




    def list_tournaments_choice(self):
        """
        Menu de choix parmis liste des tournois et renvoi vers
        manage_tournaments du joueur choisi
        """
        if self.tournaments == []:
            self.views.show_user("Liste tournois vide")
            return self.tournaments
        self.tournaments = self.sort_start_date()
        choice = self.views.prompt_choices(self.tournaments, back = True)
        if choice == -1:
            return self.tournaments
        else:
            tournament = self.tournaments.pop(choice)
            modified_tournament = self.manage_tournament(tournament)
            self.tournaments.append(modified_tournament)
            return self.tournaments

def tournament_modification(tournament_object):
    """
    Affiche et permet de choisir l'element modifiable par l'utilisateur
    """
    choix = self.views.pick(MENU_MODIFICATION, back = True)
    if choix == -1:
        return None
    elif choix == 0:
        tournament_object.name = self.views.user_input("Nom du tournoi")
    elif choix == 1:
        tournament_object.place = self.views.user_input("Lieu du tournoi")
    elif choix == 2:
        tournament_object.description = self.views.user_input("Description du tournoi")
    elif choix == 3:
        tournament_object.nb_turns = self.views.user_input("Nombre de tours")
    tournament.save_tournament(tournament_object)


def player_management(tournament_object):
    """
    Permet d'ajouter des joueurs au Tournoi
    """
    while True:
        if len(tournament_object.players) == 0:
            self.views.affiche("Pas de joueurs associés au tournoi")
        else:
            for p in tournament_object.players:
                self.views.affiche(p)
        choix = self.views.pick(MENU_JOUEURS, back = True)
        if choix == -1:
            return None
        elif choix == 0:
            add_player_to_tournament(tournament_object)

def add_player_to_tournament(tournament_object):
    """
    """
    self.views.affiche("Selectionner le joueur à ajouter au tournoi")
    player = playercontroller.player_list()
    if player == None:
        return None
    for p in tournament_object.players:
        if p.chess_id == player.chess_id:
            self.views.affiche("Ajout impossible : identifiant deja present")
            return None
    tournament_object.players.append(player)
    tournament.save_tournament(tournament_object)
