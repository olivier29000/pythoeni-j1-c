# TP 01 - Calcul et Affichage du Temps de Cuisson
print("_____Calcul du Temps de Cuisson v3_____")

type_viande = 0
while type_viande == 0: # Tant que le type de viande est égal à zéro
    print()
    print("Type de viande :")
    print((BOEUF := 1), "= BOEUF")
    print((PORC := 2), "= PORC")
    print((CANARD := 3), "= CANARD")
    type_viande = int(input("Votre choix de viande : "))
    if (type_viande not in (BOEUF, PORC, CANARD)):
        type_viande = 0
        print("==> Type de viande inconnue !")

mode_cuisson = 0
while (mode_cuisson := 0) == 0: # Tant que le mode de cuisson est égal à zéro
    print()
    print("Mode de Cuisson :")
    print((BLEUE_ROSE := 1), "= BLEUE, ROSÉ")
    print((A_POINT := 2), "= A POINT")
    print((BIEN_CUIT := 3), "= BIEN CUIT")
    mode_cuisson = int(input("Votre choix de cuisson : "))
    if (mode_cuisson not in (BLEUE_ROSE, A_POINT, BIEN_CUIT)):
        mode_cuisson = 0
        print("==> Mode de cuisson inconnu !")

poids_viande = 0
while poids_viande == 0: # Tant que le poids de la viande est égal à zéro
    print()
    poids_viande = int(input("Quel est le poids de votre viande (en grammes) ? "))
    if poids_viande <= 0:
        poids_viande = 0
        print("==> Poids non valide !")

# Variable de stockage du calcul à afficher
temps_cuisson = poids_viande

if type_viande == BOEUF:
    temps_cuisson /= 500 # Coefficient
    if mode_cuisson == BLEUE_ROSE : temps_cuisson *= 10
    elif mode_cuisson == A_POINT: temps_cuisson *= 17
    elif mode_cuisson == BIEN_CUIT: temps_cuisson *= 25
elif type_viande == PORC:
    temps_cuisson /= 400 # Coefficient
    if mode_cuisson == BLEUE_ROSE: temps_cuisson *= 15
    elif mode_cuisson == A_POINT: temps_cuisson *= 25
    elif mode_cuisson == BIEN_CUIT: temps_cuisson *= 40
elif type_viande == CANARD:
    temps_cuisson /= 450 # Coefficient
    if mode_cuisson == BLEUE_ROSE: temps_cuisson *= 20
    elif mode_cuisson == A_POINT: temps_cuisson *= 25
    elif mode_cuisson == BIEN_CUIT: temps_cuisson *= 30

if temps_cuisson > 0:
    minutes = int(temps_cuisson)  # Récupération des minutes seules (sans arrondir)
    secondes = int((temps_cuisson - minutes) * 60)  # Conversion du reste des minutes en secondes
    print("Il vous faut", minutes, "minute(s)", secondes ,"seconde(s) pour cuire votre viande.")

print()
print("_________________________Fin du programme")
