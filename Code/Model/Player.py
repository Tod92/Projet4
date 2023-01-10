class Player:
    """
    id : Identifiant National d'Echec
    """
    def __init__(self,id,firstname,lastname,birth):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth

    def __str__(self):
        return self.firstname + "" + self.lastname + " né(e) le " + str(self.birth)
