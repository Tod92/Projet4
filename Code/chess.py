"""Entry point."""

from models.database import JsonDatabase

from controllers.base import Controller

from views.base import Views
from views.console import ConsoleView
from views.reporting import Reporting

JSON_PLAYERS_PATH = "Data\Players\Players.json"
JSON_TOURNAMENTS_PATH = "Data\Tournaments\Tournaments.json"


def main():
    database = JsonDatabase(JSON_PLAYERS_PATH, JSON_TOURNAMENTS_PATH)

    active_view = ConsoleView()
    passive_views = (active_view, Reporting())
    views = Views(active_view, passive_views)

    app = Controller(database, views)
    app.run()

if __name__ == "__main__":
    main()
