# TP04 - Distributeur de Boissons
# /!\ Niveau très avancé : Certaines syntaxe sont abordées dans le module n°6.
print("_____Distributeur de boissons v4_____")
# Stock des pièces
stock_pieces = {200:5, 100:3, 50:4, 20:3, 10:12, 5:9} # type_piece:nombre
boissons = [("Café", 60),
            ("Capuccino", 80),
            ("Chocolat", 50),
            ("Eau Chaude", 10),
            ]
NOM, PRIX = 0, 1

# Permet d'afficher la monnaie avec les centimes et la devise :
afficher_monnaie = lambda monnaie, devise="€": ("%.2f%s" % (monnaie/100, devise)).replace('.',',')
# Permet de récupérer un nombre décimal, ou une valeur par défaut :
input_decimal = lambda message, defaut=-1: float(input(message).strip().replace(',','.')) or defaut
# Permet de récupérer un nombre entier, ou une valeur par défaut :
input_entier = lambda message, defaut=-1: int(input_decimal(message, defaut))

une_piece = -1
while True:
    print("_____________________________________________________Début du cycle")
    
    pieces_acceptees = "Pièces acceptées :"
    for type_piece in stock_pieces.keys():
        pieces_acceptees += ' ' + afficher_monnaie(type_piece)
    print(pieces_acceptees)

    print("Affichage du stock des pièces pour le rendu monnaie :")
    for type_piece, nb_en_stock in stock_pieces.items():
        print(" • {} : {}".format(afficher_monnaie(type_piece), nb_en_stock))
    print("____________________________________________________")

    while True:
        print("Liste des boissons :")
        for num_choix, boisson_avec_prix in enumerate(boissons):
            print("\t{} - {} ({})".format(num_choix + 1, boisson_avec_prix[NOM], afficher_monnaie(boisson_avec_prix[PRIX])))
        print("\t{} - {}".format(0, "Arrêt de la machine"))
        num_choix = input_entier("Quel est votre choix (N°) ?\n", -1)
        if num_choix in range(len(boissons) + 1): break
        print("N° de choix non valide !")

    num_choix -= 1
    if num_choix < 0: break # Sortie du Programme

    credit = 0
    nom_boisson = boissons[num_choix][NOM]
    prix_boisson = boissons[num_choix][PRIX]
    print("Boisson sélectionnée : {} ({})".format(nom_boisson, afficher_monnaie(prix_boisson)))

    # Gestion du monnayeur :
    while une_piece != 0 and credit < prix_boisson:
        print("Crédit / {} = {}/{}".format(nom_boisson, afficher_monnaie(credit), afficher_monnaie(prix_boisson)))
        une_piece = 100 * input_decimal("Merci d'introduire une pièce (0 pour 'Annuler') : ", 0)
        if une_piece in stock_pieces.keys():
            credit += une_piece
            if credit < prix_boisson: print("Crédit insuffisant, merci de faire l'appoint.")
            stock_pieces[une_piece] += 1 # stockage de la pièce
        elif une_piece == 0:
            print("Vous avez annulé votre commande…")
        else:
            print("Pièce non acceptée ({})".format(afficher_monnaie(une_piece)))

    # Gestion de l'encaissement, et de la préparation :
    rendu = credit 
    if une_piece != 0:
        print("Crédit / {} = {}/{}".format(nom_boisson, afficher_monnaie(credit), afficher_monnaie(prix_boisson)))
        rendu -= prix_boisson # On crédite le prix de la boisson pour calculer le rendu monnaie
        print("Boisson en cours de préparation…")

    # Gestion du rendu de la monnaie
    if rendu > 0:
        print("Rendu de la monnaie :", afficher_monnaie(rendu))
        print("Détail du rendu monnaie :")
        for type_piece, nb_en_stock in stock_pieces.items():
            if rendu >= type_piece:
                nb_pieces = rendu // type_piece # Division entière
                if nb_pieces > nb_en_stock:
                    nb_pieces, stock_pieces[type_piece] = nb_en_stock, 0
                else:
                    stock_pieces[type_piece] -= nb_pieces # Mise à jour du Stock
                if nb_pieces > 0:
                    print(" •", nb_pieces, "x", afficher_monnaie(type_piece), "=", afficher_monnaie(monnaie := nb_pieces * type_piece))
                    rendu -= monnaie
        print("Reste :", afficher_monnaie(rendu))
        if rendu == 0:
            print("N'oubliez pas votre monnaie.")
        else:
            print("Désolé, mais je n'ai plus d'autre monnaie !")   

    if une_piece != 0:
        print("Votre boisson est prête, vous pouvez vous servir.")

    input("________________________Appuyer sur 'Entrée' pour continuer")

print("_______________________________Fin du programme")