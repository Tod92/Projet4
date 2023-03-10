from models.player import Player


class PlayersController:
    def __init__(self, players, menus, views):
        self.players = players
        self.menus = menus
        self.views = views

    def is_chess_id_format(self, chess_id):
        if len(chess_id) != 7:
            return False
        start = chess_id[:2]
        try:
            str(start)
        except ValueError:
            return False
        if start.isupper() is False:
            return False
        end = chess_id[2:]
        try:
            int(end)
        except ValueError:
            return False
        return True

    def chess_id_in_players(self, chess_id):
        """
        returns True if player chess id found in self.players
        """
        for p in self.players:
            if p.chess_id == chess_id:
                return True
        return False

    def create_player(self):
        while True:
            chess_id = self.views.user_input("Identifiant National d'Echec")
            # Verification du format "AB12345"
            if self.is_chess_id_format(chess_id):
                # Verification de doublon de chess_id
                if self.chess_id_in_players(chess_id) is False:
                    break
                else:
                    self.views.show_user("Identifiant déja présent")
            else:
                self.views.show_user("Erreur de format de l'identiant. ")
        firstname = self.views.user_input("Prénom", type="str")
        lastname = self.views.user_input("Nom", type="str")
        birth = self.views.user_input("Date de naissance", type="int")
        newplayer = Player(chess_id, firstname, lastname, birth)
        self.players.append(newplayer)
        return self.players

    def sort_lastname(self):
        """
        renvoi liste de joueurs par ordre alphabetique du lastname
        """
        # Tri de la liste par ordre alphabetique du lastname
        self.players.sort(key=lambda x: x.lastname)
        return self.players

    def list_players_choice(self):
        """
        Menu de choix parmis liste des joueurs par ordre alphabetique du
        lastname et renvoi vers manage_player du joueur choisi
        """
        if self.players == []:
            self.views.show_user("Liste joueurs vide")
            return self.players
        self.players = self.sort_lastname()
        choice = self.views.prompt_choices(self.players, back=True)
        if choice == -1:
            return self.players
        else:
            player = self.players.pop(choice)
            modified_player = self.manage_player(player)
            self.players.append(modified_player)
        return self.players

    def manage_player(self, player):
        self.views.show_user(repr(player))
        menu = self.menus.players_modification
        choice = self.views.prompt_choices(menu, back=True)
        # Retour
        if choice == -1:
            return player
        # Prenom
        elif choice == 0:
            player.firstname = self.views.user_input("Prenom", type="str")
        # Nom
        elif choice == 1:
            player.lastname = self.views.user_input("Nom", type="str")
        # Date de naissance
        elif choice == 2:
            player.birth = self.views.user_input("Date de naissance", type="int")
        return player
