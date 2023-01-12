from Model import Player
from View import Userinterface

#joueur = Player.Player("toto","1",datetime.date(2001,1,1))




def player_creation():
    id = Userinterface.user_input("Identifiant National d'Echec")
    #TODO : verification que l'id n'est pas deja en base
    firstname = Userinterface.user_input("Prénom")
    lastname = Userinterface.user_input("Nom")
    birth = Userinterface.user_input("Date de naissance")
    newplayer = Player.Player(id,firstname, lastname, birth)
    #is_saved pour indiquer si sauvegarde json ok (True)
    is_saved = Player.save_player(newplayer)
    return is_saved

def player_list():
    """
    Liste les joueurs par ordre alphabetique du lastname et renvoi l'instance
    du joueur choisi ou None si retour
    """
    liste_joueurs = Player.load_file()
    #Tri de la liste par ordre alphabetique du lastname
    liste_joueurs.sort(key= lambda x: x.lastname)
    choix = Userinterface.pick(liste_joueurs, back = True)
    if choix == -1:
        return None
    return liste_joueurs[choix]
