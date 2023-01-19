BACK = "Retour"

class ConsoleView:
    """
    Vue terminal de commandes
    """
    def star_decorator(fonction):
        def modified(*args,**kwargs):
            print(20*"*")
            result = fonction(*args,**kwargs)
            print(20*"*")
            return result
        return modified

    @star_decorator
    def show_user(self, text):
        print(text)
        return None

    @star_decorator
    def prompt_choices(self, liste, back = False):
        """Fonction d'affichage du menu de choix en fonction de la liste en entrée.
        Renvoie l'index de l'element choisi.
        Si back : True, ajoute le choix retour qui renvoi -1
        """
        l = list(liste)
        if back == True:
            print(0,". ", BACK)
        num = 1
        for e in l:
            print(num,". ",e)
            num += 1
        return int(input("Ton choix : ")) - 1

    def user_input(self, question, type = "free"):
        #Todo : verif types
        return input("Saisir " + question + ":\n")

    def gen_report(self, text):
        print("GENERATION RAPPORT :")
        print(text)
