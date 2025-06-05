text = "Gère ta liste de courses\n"
text += "1 - Ajouter un article\n"
text += "2 - Retirer un article\n"
text += "3 - Afficher la liste\n"
text += "4 - Quitter"

inputUser = False
listeCourse = []

def AjouterArticle(article):
    listeCourse.append(article)
    
def SupprimerArticle(article):
    if article in listeCourse:
        listeCourse.remove(article)

def AfficherListe():
    for article in listeCourse:
        print(article)

while int(inputUser) != 4:
    print(text)
    inputUser = int(input())
    match inputUser:
        case 1:
            article = input("Entrez l'article à ajouter dans la liste : ")
            AjouterArticle(article)
        case 2:
            article = input("Entrez l'article à supprimer de la liste : ")
            SupprimerArticle(article)
        case 3:
            AfficherListe()
            