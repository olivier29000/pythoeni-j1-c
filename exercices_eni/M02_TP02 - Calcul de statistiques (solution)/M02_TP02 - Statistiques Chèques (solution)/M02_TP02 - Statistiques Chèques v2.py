# TP 03 - Statistiques Chèques
print("_____Statistiques Chèques v2_____")

# Niveau Essentiel :
numero_cheque = +1 #  Initialisation de la variable (> 0) pour rentrer au moins une fois dans la boucle
nombre_cheques, total_montant = 0, 0.0

# Niveau Attendu :
LIMITE = 200
nb_inferieur_limite, total_inferieur_limite = 0, 0.0
nb_superieur_limite, total_superieur_limite = 0, 0.0

while numero_cheque > 0:
    print('_________________________________________________________________')
    numero_cheque = int(input("Quel est le numéro du prochain chèque (0 pour sortir) ? "))
    if numero_cheque > 0:
        montant_cheque = float(input("Quel est son montant (. comme séparateur décimal) : "))
        # Niveau Essentiel : Comptabilisation du nombre et des montants par accumulation
        nombre_cheques += 1
        total_montant += montant_cheque

        # Niveau Attendu : Comptabilisation du nombre et des montants en fonction de la limite
        if montant_cheque < LIMITE:
            nb_inferieur_limite += 1
            total_inferieur_limite += montant_cheque
        else:
            nb_superieur_limite += 1
            total_superieur_limite += montant_cheque
        
        print("C'est bien enregistré, passons au suivant…")

# Affichage du calcul de la saisie
print("Affichage des résultats :____________________________________________")
if nombre_cheques > 0:
    # Niveau Essentiel :
    print(" • Nombre de chèques :", nombre_cheques)
    print(" • Somme des chèques :", total_montant, "€")
    print(" • Moyenne des montants :", (total_montant / nombre_cheques), "€")
    
    # Niveau Attendu :
    print(" - - - - - - - - - - - - - - - - - - - - - - - ")
    print(" • Somme des chèques <", LIMITE,"€ :", total_inferieur_limite, "€ ( nb. =", nb_inferieur_limite, ")")
    print(" • Somme des chèques ≥", LIMITE,"€ :", total_superieur_limite, "€ ( nb. =", nb_superieur_limite, ")")
else:
    print(" # Aucun chèque saisi !")

print("_________________________________Fin du programme")