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

    def __str__(self):
        return "Match : " + str(self.player1) + " contre " + str(self.player2)

    def __repr__(self):
        return "Match : " + str(self.player1) + " contre " + str(self.player2)

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
