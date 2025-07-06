# comptez le nombre de voyelles et de consonnes dans un string

str = input('Enter a string: ')

voyelles = "aeiuo"
nb = 0
for s in str:
    if s in voyelles:
        nb += 1

print(nb, "voyelles")
print(len(str) - nb , "consonnes")