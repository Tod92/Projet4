import Match as M
import Player as P
import Tournament as TO
import Turn as TU

import datetime


def main():

    joueur1 = P.Player("toto","1",datetime.date(2001,1,1))
    joueur2 = P.Player("tata","2",datetime.date(2002,2,2))
    joueur3 = P.Player("tete","3",datetime.date(2003,3,3))
    joueur4 = P.Player("tutu","4",datetime.date(2004,4,4))
    joueur5 = P.Player("titi","5",datetime.date(2005,5,5))
    joueur6 = P.Player("tyty","6",datetime.date(2006,6,6))

    player_list = [joueur1, joueur2, joueur3, joueur4, joueur5, joueur6]
    players_points_dict = {joueur1 : 1, joueur2 : 2, joueur3 : 3, joueur4 : 4,
                            joueur5: 5, joueur6 : 6}

    tour = TU.Turn("Round 1", players_points_dict)
    print(tour)

if __name__ == '__main__':
    main()
