BACK = "Retour"


class ConsoleView:
    """
    Vue terminal de commandes
    """
    def star_decorator(fonction):
        def modified(*args, **kwargs):
            print(20*"*")
            result = fonction(*args, **kwargs)
            print(20*"*")
            return result
        return modified

    @star_decorator
    def show_user(self, text):
        print(text)
        return None

    @star_decorator
    def prompt_choices(self, menu, back=False):
        """Fonction d'affichage du menu de choix en fonction de la liste
        en entrée.
        Renvoie l'index de l'element choisi.
        Si back : True, ajoute le choix retour qui renvoi -1
        """
        min_choice = 1
        if back:
            print(0, ". ", BACK)
            min_choice = 0
        num = 1
        for e in menu:
            print(num, ". ", e)
            num += 1
        while True:
            result = input("Ton choix : ")
            try:
                result = int(result)
                if result < min_choice or result > len(menu):
                    print("Erreur : choix indisponible")
                else:
                    return result - 1
            except ValueError:
                print("Erreur : un nombre est attendu")

    def user_input(self, question, type="free"):
        while True:
            result = input("Saisir " + question + ":\n")
            if type == "free":
                return result
            elif type == "int":
                try:
                    if result.isnumeric() is False:
                        raise ValueError
                    return int(result)
                except ValueError:
                    print("Erreur : un nombre est attendu")
            elif type == "str":
                try:
                    result = str(result)
                    return result
                except ValueError:
                    print("Erreur : du texte est attendu")

    def gen_report(self, text):
        print("GENERATION RAPPORT :")
        print(text)
