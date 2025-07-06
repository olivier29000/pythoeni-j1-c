# calculez la somme des nombres naturels d'un nombre donné
# avec une boucle
# et avec une formule

num = int(input("indiquez un nombre"))

somme = 0

for i in range(1,num+1):
    somme = somme + i

print(somme)

print(num * (num + 1) / 2)