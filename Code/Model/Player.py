class Player:
    """

    """
    def __init__(self,firstname,lastname,birth):
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth

    def __str__(self):
        return self.firstname + "" + self.lastname + " né(e) le " + str(self.birth)
