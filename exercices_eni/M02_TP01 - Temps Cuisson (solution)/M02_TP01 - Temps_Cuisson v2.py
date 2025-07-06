# TP 01 - Calcul et Affichage du Temps de Cuisson
print("_____Calcul du Temps de Cuisson v2_____")
print("") # Afficher une ligne vide
print("Type de viande :")
BOEUF = 1
PORC = 2
print(BOEUF, "= BOEUF")
print(PORC, "= PORC")
type_viande = int(input("Votre choix de viande : "))

print("")
print("Mode de Cuisson :")
BLEUE = 1
A_POINT = 2
BIEN_CUIT = 3
print(BLEUE, "= BLEUE")
print(A_POINT, "= A POINT")
print(BIEN_CUIT, "= BIEN CUIT")
mode_cuisson = int(input("Votre choix de cuisson : "))

print("")
poids_viande = int(input("Quel est le poids de votre viande (en grammes) ? "))

# Variable de stockage du calcul à afficher
temps_cuisson = 0

MODE_CUISSON_INCONNU = "Mode de cuisson inconnu"
if type_viande == BOEUF:
    poids_ref = 500
    if mode_cuisson == BLEUE:
        temps_cuisson = poids_viande * 10 / poids_ref
    elif mode_cuisson == A_POINT:
        temps_cuisson = poids_viande * 17 / poids_ref
    elif mode_cuisson == BIEN_CUIT:
        temps_cuisson = poids_viande * 25 / poids_ref
    else:
        print(MODE_CUISSON_INCONNU)
elif type_viande == PORC:
    poids_ref = 400
    if mode_cuisson == BLEUE:
        temps_cuisson = poids_viande * 15 / poids_ref
    elif mode_cuisson == A_POINT:
        temps_cuisson = poids_viande * 25 / poids_ref
    elif mode_cuisson == BIEN_CUIT:
        temps_cuisson = poids_viande * 40 / poids_ref
    else:
        print(MODE_CUISSON_INCONNU)
else:
    print("Type de viande inconnue")

if temps_cuisson > 0:
    print("Il vous faut", temps_cuisson, "minute(s) pour cuire votre viande")

print("")
print("_________________________Fin du programme")
