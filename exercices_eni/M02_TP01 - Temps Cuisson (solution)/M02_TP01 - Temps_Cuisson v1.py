# TP 01 - Calcul et Affichage du Temps de Cuisson
print("_____Calcul du Temps de Cuisson v1_____")
print("")

print("")
print("""Mode de Cuisson (BOEUF) :
    1 = BLEUE
    2 = A POINT
    3 = BIEN CUIT""")
mode_cuisson = int(input("Votre choix de cuisson : "))

print("")
poids_viande = int(input("Quel est le poids de votre viande (en grammes) ? "))

# Variable de stockage du calcul à afficher
temps_cuisson = 0

# On attribut un numéro à chaque mode de cuisson
BLEUE = 1
A_POINT = 2
BIEN_CUIT = 3

# Calcul du temps de cuisson
if mode_cuisson == BLEUE:
    temps_cuisson = poids_viande * 10 / 500
elif mode_cuisson == A_POINT:
    temps_cuisson = poids_viande * 17 / 500
elif mode_cuisson == BIEN_CUIT:
    temps_cuisson = poids_viande * 25 / 500
else:
    print("Mode de cuisson inconnu")

if temps_cuisson > 0:
    print("Il vous faut", temps_cuisson, "minute(s) pour cuire votre viande")

print("")
print("_________________________Fin du programme")

