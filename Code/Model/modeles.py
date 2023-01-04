import datetime
import random

class Tournament:
    """
    """
    def __init__(self, name, place, start_date, end_date, turn_number,
                players_list, description, nb_turns = 4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.turn_number = turn_number
        self.turn_list = []
        self.player_list = players_list
        self.description = description

    def gen_new_turn():
        pass


class Turn:
    """

    """
    def __init__(self, name, players_points_dict):
        #players_points_dict doit etre un dict tuples contenant joueur et score
        self.name = name
        self.isfinished = False
        self.start_time = "TODO"
        self.match_list = self.gen_match_list(players_points_dict)

    def __str__(self):
        return self.name + " : " + str(self.match_list)


    def gen_match_list(self, players_points_dict):
        #Tri de la liste de tuples du plus gros score au plus petit
        liste_triee = sorted(players_points_dict.items(),
                            key=lambda x: x[1],reverse = True)
        #On ne garde que les joueurs dans la liste désormais triée
        liste_triee = [e[0] for e in liste_triee]

        match_list = []
        for i in range(len(liste_triee)//2):
            player1 = liste_triee.pop(0)
            player2 = liste_triee.pop(0)
            match_list += [Match(player1, player2)]
        return match_list
    def closing(self)

class Match:
    """
    Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune
    contenant deux éléments : un joueur et un score. Les matchs doivent être stockés sous
    forme de liste dans l'instance du tour auquel ils appartiennent.
    """
    def __init__(self, player1, player2):
        self.isfinished = False
        self.player1 = player1
        self.player2 = player2

    def closing(self, winner):
        """
        winner : joueur ayant remporté le match
        si nul, winner = None
        Retourne un tuple contenant deux listes, chacune
        contenant deux éléments : un joueur et un score
        """
        if winner == self.player1:
            p1score, p2score = 1 , 0
        elif winner == self.player2:
            p1score, p2score = 0, 1
        elif winner == None:
            p1score, p2score = 0.5 , 0.5
        self.isfinished = True
        return ([self.player1, p1score], [self.player2, p2score])



class Player:
    """

    """
    def __init__(self,firstname,lastname,birth):
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth

    def __str__(self):
        return self.firstname + "" + self.lastname + " né(e) le " + birth



def main():

    joueur1 = Player("toto","1",datetime.date(2001,1,1))
    joueur2 = Player("tata","2",datetime.date(2002,2,2))
    joueur3 = Player("tete","3",datetime.date(2003,3,3))
    joueur4 = Player("tutu","4",datetime.date(2004,4,4))
    joueur5 = Player("titi","5",datetime.date(2005,5,5))
    joueur6 = Player("tyty","6",datetime.date(2006,6,6))

    player_list = [joueur1, joueur2, joueur3, joueur4, joueur5, joueur6]
    players_points_dict = {joueur1 : 1, joueur2 : 2, joueur3 : 3, joueur4 : 4,
                            joueur5: 5, joueur6 : 6}

    tour = Turn("Round 1", players_points_dict)
    print(tour)
if __name__ == '__main__':
    main()
