from Model import Player
from View import Userinterface

#joueur = Player.Player("toto","1",datetime.date(2001,1,1))




def main():
    id = Userinterface.user_input("Identifiant National d'Echec")
    #TODO : verification que l'id n'est pas deja en base
    firstname = Userinterface.user_input("Nom")
    lastname = Userinterface.user_input("Prénom")
    birth = Userinterface.user_input("Date de naissance")
    newplayer = Player.Player(id,firstname, lastname, birth)
    #is_saved pour indiquer si sauvegarde json ok (True)
    is_saved = Player.save_player(newplayer)
