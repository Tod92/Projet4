
class Tournament:
    """
    """
    def __init__(self, id, name, place, start_date, end_date, turn_number,
                players, description, nb_turns = 4):
        self._id = id
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.turn_number = turn_number
        self.turn_list = []
        self.players = players
        self.description = description
        self.nb_turns = nb_turns
        self.is_started = False
        self.is_finished = False


    def __str__(self):
        result = "Tournoi (id :" + str(self._id) + ")\n"
        result += "Nom : " + self.name + "\n"
        result += "Lieu : " + self.place + "\n"
        result += "Description : " + self.description + "\n"
        result += "Date de debut : " + self.start_date + "\n"
        result += "Date de fin : " + self.end_date + "\n"
        result += "Nombre de tours : " + str(self.nb_turns) + "\n"
        result += "Tour actuel : " + str(self.turn_number) + "\n"
        result += "Participants : " + str(self.players)

        return result

    def is_playable(self):
        """
        renvoie True si les conditions sont remplies pour pouvoir jouer
        le tournoi : non terminé, liste joueurs non vide et pair
        """
        #TODO : gestion exceptions pour remonter la raison du unplayable
        if self.is_finished == True:
            return False
        elif self.players == []:
            return False
        elif (len(self.players)%2) != 0:
            return False
        else:
            return True
