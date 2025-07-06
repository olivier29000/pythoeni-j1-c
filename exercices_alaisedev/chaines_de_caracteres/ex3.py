# enlevez les mots interdits de cette histoire

story = """
Ce matin-là, Jules était déjà en retard. 
Il saute dans sa vieille voiture, tourne la clé... rien. 
Putain, pas aujourd’hui.
Il sort, claque la portière un peu trop fort. 
Il tente de bricoler sous le capot, comme s’il savait ce qu’il faisait. 
Bien sûr, aucune idée. Il se coupe un doigt. Merde, évidemment.
Il finit par appeler son pote Karim, qui lui répond encore à moitié endormi :
— Putain, t’as encore oublié de faire la vidange ou quoi ?
Jules rigole nerveusement. 
Le genre de rire qui veut dire "je vais exploser". 
Finalement, Karim arrive, le dépanne tant bien que mal. 
Jules monte enfin dans la voiture de secours, en route pour une journée qui s’annonce… longue."""

mots_interdits = "merde putain crotte"

for word in mots_interdits.split(" "):
    story = (story.replace(word , "*****"))

print(story)