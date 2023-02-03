
class Player:
    """
    chess_id : Identifiant National d'Echec
    """
    def __init__(self, chess_id, firstname, lastname, birth):
        self.chess_id = chess_id
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth

    def __str__(self):
        result = "(" + self.chess_id + ")"
        result += self.firstname + " " + self.lastname
        return result

    def __repr__(self):
        result = "(" + self.chess_id + ")"
        result += self.firstname + " " + self.lastname + " "
        result += "né(e) le : " + self.birth
        return result
