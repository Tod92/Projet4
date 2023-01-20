from models.player import Player


class PlayersController:
    def __init__(self, players, menus, views):
        self.players = players
        self.menus = menus
        self.views = views



    def create_player(self):

        chess_id = self.views.user_input("Identifiant National d'Echec")
        #TODO : verification que l'id n'est pas deja en base
        firstname = self.views.user_input("Prénom")
        lastname = self.views.user_input("Nom")
        birth = self.views.user_input("Date de naissance")
        newplayer = Player(chess_id,firstname, lastname, birth)
        self.players.append(newplayer)
        return self.players

    def sort_lastname(self):
        """
        renvoi liste de joueurs par ordre alphabetique du lastname
        """
        #Tri de la liste par ordre alphabetique du lastname
        self.players.sort(key= lambda x: x.lastname)
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
        choice = self.views.prompt_choices(self.players, back = True)
        if choice == -1:
            return self.players
        else:
            player = self.players.pop(choice)
            modified_player = self.manage_player(player)
            self.players.append(modified_player)
        return self.players

    def manage_player(self, player):
        self.views.show_user(player)
        #TODO : menu pour modifier les infos du joueur SAUF ID
        return player
