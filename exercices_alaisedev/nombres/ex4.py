# Vérifiez si une année est une année bisextile
# attention, regardez bien la définition selon le calendrier grégorien

num = int(input("indiquez un nombre"))

if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print("c'est une année bisextile")
else:
    print("ce n'est pas une année bisextile")
