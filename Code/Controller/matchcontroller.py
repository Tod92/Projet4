

def closing(match, winner):
    """
    winner : joueur ayant remporté le match. 0 : player1, 1 : player2.
    si nul, winner = 2
    Retourne un tuple contenant deux listes, chacune
    contenant deux éléments : un joueur et un score
    """
    if winner == 0:
        p1score, p2score = 1 , 0
    elif winner == 1:
        p1score, p2score = 0, 1
    elif winner == 2:
        p1score, p2score = 0.5 , 0.5
    return ([match.player1, p1score], [match.player2, p2score])



if __name__ == '__main__':
    main()
