# TP04 - Distributeur de Boissons
print("_____Distributeur de boissons v1_____")
print("Pièces acceptées : 2€ 1€ 0.50€ 0.20€ 0.10€ 0.05€")

# Permet d'afficher la monnaie avec les centimes et la devise :
afficher_monnaie = lambda m, d="€": "%.2f%s" % (m/100, d)

une_piece = 1
print("_____________________________________________________Début du cycle")
print("Vous avez sélectionné un Café")
credit = 0
PRIX_CAFE = 60

# Gestion du monnayeur :
while une_piece > 0 and credit < PRIX_CAFE:
    print("Crédit / Café =", afficher_monnaie(credit), "/", afficher_monnaie(PRIX_CAFE))
    une_piece = int(100 * float(input("Merci d'introduire une pièce (0 pour 'Annuler') : ")))

    if une_piece in (200, 100, 50, 20, 10, 5):
        credit += une_piece
        if credit < PRIX_CAFE: print("Crédit insuffisant, merci de faire l'appoint.")
    elif une_piece == 0:
        print("Vous avez annulé votre commande…")
    else:
        print("Pièce non acceptée :", afficher_monnaie(une_piece))

# Gestion de l'encaissement, et de la préparation :
if une_piece != 0:
    print("Crédit / Café =", afficher_monnaie(credit), "/", afficher_monnaie(PRIX_CAFE))
    print("Boisson en cours de préparation…")
    print("Votre boisson est prête, vous pouvez vous servir.")

print("_______________________________Fin du programme")