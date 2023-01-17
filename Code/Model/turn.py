import Match as M


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
            match_list += [M.Match(player1, player2)]
        return match_list

    def closing(self):
        """
        On demande à l'objet Turn de se cloturer (isfinished = True)
        Doit verifier que tous les matchs de match_list sont réalisés cad ne
        sont plus sous la forme objet Match() mais tuple
        """
        for e in match_list:
            if type(e) != tuple:
                return False
        self.isfinished = True
        return self
