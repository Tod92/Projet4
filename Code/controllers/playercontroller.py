from Model import player
from View import userinterface

def player_creation():
    #while True:
        #chess_id = userinterface.user_input("Identifiant National d'Echec")
        #if is_chess_id_format(chess_id) == False:
            #message a demander a View
            #break
        #if is_avaible(chess_id) == False:
            #message a demander a View
            #break
    chess_id = userinterface.user_input("Identifiant National d'Echec")
    #TODO : verification que l'id n'est pas deja en base
    firstname = userinterface.user_input("Prénom")
    lastname = userinterface.user_input("Nom")
    birth = userinterface.user_input("Date de naissance")
    newplayer = player.Player(chess_id,firstname, lastname, birth)
    #is_saved pour indiquer si sauvegarde json ok (True)
    is_saved = player.save_player(newplayer)
    return is_saved

def player_list():
    """
    Liste les joueurs par ordre alphabetique du lastname et renvoi l'instance
    du joueur choisi ou None si retour
    """
    liste_joueurs = player.load_file()
    #Tri de la liste par ordre alphabetique du lastname
    liste_joueurs.sort(key= lambda x: x.lastname)
    choix = userinterface.pick(liste_joueurs, back = True)
    if choix == -1:
        return None
    return liste_joueurs[choix]
