"""Entry point."""

from models.database import Database

from controllers.base import Controller

from views.base import Views
from views.console import ConsoleView
from views.reporting import Reporting

def main():
    database = Database()

    active_view = ConsoleView()
    passive_views = (active_view, Reporting())
    views = Views(active_view, passive_views)

    app = Controller(database, views)
    app.run()

if __name__ == "__main__":
    main()
