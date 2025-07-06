# Créez un programme qui demande à l'utilisateur un nombre
# puis qui lui indique si celui ci est pair ou impair

num = int(input("indiquez un nombre"))

if(num % 2 == 0):
    print(num, "est pair")
else:
    print(num, "est impair")
