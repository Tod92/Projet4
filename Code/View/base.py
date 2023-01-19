
class Views:
    """
    Regroupe toutes les vues
    """
    def __init__(self, active_view, views):
        self.active_view = active_view
        self.views = views

    def prompt_choices(self, choices, back = False):
        return self.active_view.prompt_choices(choices, back = False)

    def show_user(self, text):
        self.active_view.show_user(text)
        return None

    def gen_report(self, text):
        for view in self.views:
            views.gen_report(text)
