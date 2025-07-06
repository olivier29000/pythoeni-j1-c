# TP04 - Distributeur de Boissons
print("_____Distributeur de boissons v2_____")
print("Pièces acceptées : 2€ 1€ 0.50€ 0.20€ 0.10€ 0.05€")

# Permet d'afficher la monnaie avec les centimes et la devise :
afficher_monnaie = lambda m, d="€": "%.2f%s" % (m/100, d)

une_piece = 1 # Initialisation de la variable pour rentrer au moins une fois dans la boucle
while une_piece >= 0:
    print("_____________________________________________________Début du cycle")
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

    input("________________________Appuyer sur 'Entrée' pour continuer")

print("_______________________________Fin du programme")