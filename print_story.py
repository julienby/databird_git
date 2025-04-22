#Crée un script python (.py) permettant d’afficher l’histoire du fichier story.txt

with open('story.txt', 'r') as file:
    print(file.read())

