from models.player import Player


class PlayersController:
    def __init__(self, players, views):
        self.players = players
        self.views = views



    def create_player(self):

        chess_id = self.views.user_input("Identifiant National d'Echec")
        #TODO : verification que l'id n'est pas deja en base
        firstname = self.views.user_input("Prénom")
        lastname = self.views.user_input("Nom")
        birth = self.views.user_input("Date de naissance")
        newplayer = Player(chess_id,firstname, lastname, birth)
        #is_saved pour indiquer si sauvegarde json ok (True)
        self.players.append(newplayer)
        return self.players

    def list_players(self):
        """
        Liste les joueurs par ordre alphabetique du lastname et renvoi l'instance
        du joueur choisi ou None si retour
        """
        if self.players == []:
            self.views.show_user("Liste joueurs vide")
            return self.players
        #Tri de la liste par ordre alphabetique du lastname
        self.players.sort(key= lambda x: x.lastname)
        choice = self.views.prompt_choices(self.players, back = True)
        if choice == -1:
            return None
        else:
            player = self.players.pop(choice)
            modified_player = self.manage_player(player)
            self.players.append(modified_player)
        return self.players

    def manage_player(self, player):
        return player
