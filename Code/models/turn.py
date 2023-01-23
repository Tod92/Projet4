from models.match import Match
#from match import Match
class Turn:
    """

    """
    def __init__(self, name, players_points_dict):
        #players_points_dict doit etre un dict tuples contenant joueur et score
        self.name = name
        self.is_finished = False
        self.start_time = "TODO"
        self.matchs = self.gen_matchs(players_points_dict)

    def __str__(self):
        return self.name + " : " + str(self.matchs)


    def gen_matchs(self, players_points_dict):
        #Tri de la liste de tuples du plus gros score au plus petit
        liste_triee = sorted(players_points_dict.items(),
                            key=lambda x: x[1],reverse = True)
        #On ne garde que les joueurs dans la liste désormais triée
        liste_triee = [e[0] for e in liste_triee]

        matchs = []
        for i in range(len(liste_triee)//2):
            player1 = liste_triee.pop(0)
            player2 = liste_triee.pop(0)
            matchs += [Match(player1, player2)]

        return matchs

    def closing(self):
        """
        On demande à l'objet Turn de se cloturer (isfinished = True)
        Doit verifier que tous les matchs de matchs sont réalisés cad ne
        sont plus sous la forme objet Match() mais tuple
        """
        for e in matchs:
            if type(e) != tuple:
                return False
        self.is_finished = True
        return self


if __name__ == '__main__':
    scores = {"Tod" : 5, "benj" : 2, "hugo" : 1, "jess" : 0}
    turn = Turn("Round", scores)
    print(turn)
    scores = {"Tod" : 0, "benj" : 0, "hugo" : 10, "jess" : 10}
    turn = Turn("Round", scores)
    print(turn)
