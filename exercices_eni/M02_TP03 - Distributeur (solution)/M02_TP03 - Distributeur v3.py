# TP04 - Distributeur de Boissons
print("_____Distributeur de boissons v3_____")
print("Pièces acceptées : 2€ 1€ 0.50€ 0.20€ 0.10€ 0.05€")

# Stock des pièces
nb_pieces_200, nb_pieces_100 = 5, 3  # Euro
nb_pieces_050, nb_pieces_020, nb_pieces_010, nb_pieces_005 = 4, 3, 12, 9  # Centime d'Euro

# Permet d'afficher la monnaie avec les centimes et la devise :
afficher_monnaie = lambda m, d="€": "%.2f%s" % (m/100, d)

une_piece = 1
while une_piece >= 0:
    print("_____________________________________________________Début du cycle")
    print("Affichage du stock des pièces pour le rendu monnaie :")
    print(" •", afficher_monnaie(200), ":", nb_pieces_200)
    print(" •", afficher_monnaie(100), ":", nb_pieces_100)
    print(" •", afficher_monnaie(50), ":", nb_pieces_050)
    print(" •", afficher_monnaie(20), ":", nb_pieces_020)
    print(" •", afficher_monnaie(10), ":", nb_pieces_010)
    print(" •", afficher_monnaie(5), ":", nb_pieces_005)
    print("____________________________________________________")
    print("Vous avez sélectionné un Café")
    credit = 0
    PRIX_CAFE = 60

    # Gestion du monnayeur :
    while une_piece > 0 and credit < PRIX_CAFE:
        print("Crédit / Café =", afficher_monnaie(credit), "/", afficher_monnaie(PRIX_CAFE))
        une_piece = int(100 * float(input("Merci d'introduire une pièce (0 pour 'Annuler', < 0 pour 'Quitter') : ")))

        if une_piece in (200, 100, 50, 20, 10, 5):
            credit += une_piece
            if credit < PRIX_CAFE: print("Crédit insuffisant, merci de faire l'appoint.")
            # stockage de la pièce
            if une_piece == 200: nb_pieces_200 += 1
            elif une_piece == 100: nb_pieces_100 += 1
            elif une_piece == 50: nb_pieces_050 += 1
            elif une_piece == 20: nb_pieces_020 += 1
            elif une_piece == 10: nb_pieces_010 += 1
            elif une_piece == 5: nb_pieces_005 += 1
        elif une_piece == 0:
            print("Vous avez annulé votre commande…")
        else:
            print("Pièce non acceptée :", afficher_monnaie(une_piece))

    # Gestion de l'encaissement, et de la préparation :
    rendu = credit 
    if une_piece > 0:
        print("Crédit / Café =", afficher_monnaie(credit), "/", afficher_monnaie(PRIX_CAFE))
        rendu -= PRIX_CAFE # On crédite le prix de la boisson pour calculer le rendu monnaie
        print("Boisson en cours de préparation…")
        print("Votre boisson est prête, vous pouvez vous servir.")
    elif une_piece < 0:
        print("Procédure d'arrêt du distributeur")
    else:
        une_piece = 1 # Ré-Initialisation de la variable pour rentrer à nouveau dans les prochaines boucles
    
    # Gestion du rendu de la monnaie
    if rendu > 0:
        print("Rendu de la monnaie :", afficher_monnaie(rendu))
        print("Détail du rendu monnaie :")
        if rendu >= (type_piece := 200): # Pièce de 2€
            nb_pieces = rendu // type_piece # Division entière
            if nb_pieces > nb_pieces_200:
                nb_pieces, nb_pieces_200 = nb_pieces_200, 0
            else:
                nb_pieces_200 -= nb_pieces # Mise à jour du Stock
            if nb_pieces > 0:
                print(" •", nb_pieces, "x", afficher_monnaie(type_piece), "=", afficher_monnaie(monnaie := nb_pieces * type_piece))
                rendu -= monnaie
        if rendu >= (type_piece := 100): # Pièce de 1€
            nb_pieces = rendu // type_piece # Division entière
            if nb_pieces > nb_pieces_100:
                nb_pieces, nb_pieces_100 = nb_pieces_100, 0
            else:
                nb_pieces_100 -= nb_pieces # Mise à jour du Stock
            if nb_pieces > 0:
                print(" •", nb_pieces, "x", afficher_monnaie(type_piece), "=", afficher_monnaie(monnaie := nb_pieces * type_piece))
                rendu -= monnaie
        if rendu >= (type_piece := 50): # Pièce de 0.50€
            nb_pieces = rendu // type_piece # Division entière
            if nb_pieces > nb_pieces_050:
                nb_pieces, nb_pieces_050 = nb_pieces_050, 0
            else:
                nb_pieces_050 -= nb_pieces # Mise à jour du Stock
            if nb_pieces > 0:
                print(" •", nb_pieces, "x", afficher_monnaie(type_piece), "=", afficher_monnaie(monnaie := nb_pieces * type_piece))
                rendu -= monnaie
        if rendu >= (type_piece := 20): # Pièce de 0.20€
            nb_pieces = rendu // type_piece # Division entière
            if nb_pieces > nb_pieces_020:
                nb_pieces, nb_pieces_020 = nb_pieces_020, 0
            else:
                nb_pieces_020 -= nb_pieces # Mise à jour du Stock
            if nb_pieces > 0:
                print(" •", nb_pieces, "x", afficher_monnaie(type_piece), "=", afficher_monnaie(monnaie := nb_pieces * type_piece))
                rendu -= monnaie
        if rendu >= (type_piece := 10): # Pièce de 0.10€
            nb_pieces = rendu // type_piece # Division entière
            if nb_pieces > nb_pieces_010:
                nb_pieces, nb_pieces_010 = nb_pieces_010, 0
            else:
                nb_pieces_010 -= nb_pieces # Mise à jour du Stock
            if nb_pieces > 0:
                print(" •", nb_pieces, "x", afficher_monnaie(type_piece), "=", afficher_monnaie(monnaie := nb_pieces * type_piece))
                rendu -= monnaie
        if rendu >= (type_piece := 5): # Pièce de 0.05€
            nb_pieces = rendu // type_piece # Division entière
            if nb_pieces > nb_pieces_005:
                nb_pieces, nb_pieces_005 = nb_pieces_005, 0
            else:
                nb_pieces_005 -= nb_pieces # Mise à jour du Stock
            if nb_pieces > 0:
                print(" •", nb_pieces, "x", afficher_monnaie(type_piece), "=", afficher_monnaie(monnaie := nb_pieces * type_piece))
                rendu -= monnaie
        
        print("Reste :", afficher_monnaie(rendu))
        if rendu == 0:
            print("Prenez votre monnaie.")
        else:
            print("Désolé, mais je n'ai plus d'autre monnaie !")   
    input("________________________Appuyer sur 'Entrée' pour continuer")

print("_______________________________Fin du programme")