# vérifiez si une string est un palindrome
# un palindrome est un nombre qui s'écrit pareil à l'envers
# exemples : kayak, radar

str = input('Enter a string: ')

if(str == str[::-1]):
    print("c'est un palindrome")
else:
    print("ce n'est pas un palindrome")