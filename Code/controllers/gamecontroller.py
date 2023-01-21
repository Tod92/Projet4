

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

    def run(self):
        self.load_tournaments()
        tournament = self.extract_tournament_from_list()
        print("J'ai reussi à extraire le tournoi : ", tournament)
        print("mon self.tournaments : ", self.tournaments)
        print("mon tournament : ", tournament)
        
