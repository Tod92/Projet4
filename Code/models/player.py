
class Player:
    """
    chess_id : Identifiant National d'Echec
    """
    def __init__(self,chess_id,firstname,lastname,birth):
        self.chess_id = chess_id
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth

    def __str__(self):
        return self.firstname + " " + self.lastname + " né(e) le " + str(self.birth)

    def __repr__(self):
        return "(" + self.chess_id + ")" +self.firstname + " " + self.lastname
