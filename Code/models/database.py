import json, jsonpickle


class JsonDatabase:
    """
    Objet de gestion des sauvegardes via fichiers JSON
    """
    def __init__(self, players_file_path, tournaments_file_path):
        self.players_file_path = players_file_path
        self.tournaments_file_path = tournaments_file_path

    def write_file(self, object, path):
        """
        json encode object and create or overwrite file at path
        """
        json_object = jsonpickle.encode(object)
        with open(path, 'w') as file:
            json.dump(json_object, file)

    def load_file(self, path):
        """
        La methode renvoie la liste extraite du fichier JSON situé "path"
        Le fichier est crée en cas d'échec d'ouverture au chemin indiqué
        """
        try:
            with open(path, 'r') as file:
                json_list = json.load(file)
            return jsonpickle.decode(json_list)
        except:
            empty_list = []
            self.write_file(empty_list, path)
            return empty_list

    def get_players(self):
            return self.load_file(self.players_file_path)
    def get_tournaments(self):
            return self.load_file(self.tournaments_file_path)
    def save_players(self, players):
            self.write_file(players, self.players_file_path)
    def save_tournaments(self, tournaments):
            self.write_file(tournaments, self.tournaments_file_path)

if __name__ == '__main__':
    main()
