# la suite de fibonacci est une séquence de nombre où chaque nombre est la somme des deux précédents
# 0 1 1 2 3 5 8...
# affichez la suite de fibonacci jusqu'à atteindre un nombre supérieur à celui donné

num = int(input("indiquez un nombre"))

a = 0
b = 1
n = 0
while b < num:
    print(a + b, end=" ")
    a, b = b, a + b
    n += 1
print()
print(f"il a fallu {n} pas")