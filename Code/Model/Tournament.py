class Tournament:
    """
    """
    def __init__(self, name, place, start_date, end_date, turn_number,
                players_list, description, nb_turns = 4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.turn_number = turn_number
        self.turn_list = []
        self.player_list = players_list
        self.description = description

    def gen_new_turn():
        pass
