# Créez un programme qui demande à l'utilisateur un nombre
# puis qui lui indique si c'est un nombre parfait
# NB : un nombre parfait est un nombre dont la somme des diviseurs propres inférieur à lui même est égal à lui même
# NB : un diviseur propre est un diviseur sans reste (exemple : 3 est un diviseur propre de 6, car 6 / 3 = 2)
# exemple : 6 est un nombre parfait car ces diviseurs propres sont 1, 2, 3 et 1 + 2 + 3 = 6
# 28 est aussi un nombre parfait

num = int(input("indiquez un nombre"))
somme = 0

for i in range(1, num):
    if(num % i == 0):
        somme = i + somme

if(somme == num):
    print("c'est un nombre parfait")
else:
    print("ce n'est pas un nombre parfait")