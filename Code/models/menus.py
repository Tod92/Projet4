class Menus:
    main = ["Jouer Tournoi",
            "Gestion Joueurs",
            "Gestion Tournois",
            "Rapports",
            "Quitter"]

    players_management = ["Nouveau joueur",
                          "Liste joueurs"]

    players_modification = ["Prenom",
                            "Nom",
                            "Date de naissance"]

    tournaments_management = ["Nouveau Tournoi",
                              "Liste tournois"]

    tournaments_modification = ["Nom",
                                "Lieu",
                                "Description",
                                "Date de debut",
                                "Date de fin",
                                "Nombre de tours",
                                "Ajouter joueur au tournoi"]
    start_turn = ["Demarrer tour (demarrage des matchs)",
                  "Quitter"]

    gen_turn = ["Generer nouveau tour (verrouillage liste participants)",
                "Quitter"]

    active_turn = ["Saisir le résultat d'un match",
                   "Terminer le tour",
                   "Quitter"]

    reports = ["Liste de tous les joueurs par ordre alphabétique",
               "Liste de tous les tournois",
               "Nom et date d'un tournoi donné",
               "Liste des joueurs du tournoi par ordre alphabétique",
               "Liste de tous les tours du tournoi et de tous les matchs du tour"]

    draw = "Match nul"
    cant_close_turn = "Cloture du tour impossble. Match(s) en cours"
    pick_winner = "Selectionner le vainqueur du match : "
    choose_tournament = "Choisir le tournoi à jouer"
    tournaments_empty = "Liste de tournois vide"
    turn_not_started = "Tour non démarré"
    started_matchs = "Matchs en cours : "
    finished_matchs = "Matchs terminés : "
