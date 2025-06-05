listeNombres = []

inputUser = input("Entre un nombre (ou stop pour terminer) : ")

while str(inputUser) != "stop" or len(listeNombres) == 0:
    
    try:
        listeNombres.append(int(inputUser))
    except ValueError:
        print("Entre un nombre correct") 
    inputUser = input("Entre au moins un nombre (ou stop pour terminer) : ")
    
def Moyenne(listeNombres):
    somme = 0
    for nombre in listeNombres:
        somme += int(nombre)
    return somme / len(listeNombres)

def Min(listeNombres):
    min = listeNombres[0]
    for nombre in listeNombres:
        if(nombre < min):
            min = nombre
    return min

def Max(listeNombres):
    max = listeNombres[0]
    for nombre in listeNombres:
        if(nombre > max):
            max = nombre
    return max

print(f"Min : {Min(listeNombres)}\nMax : {Max(listeNombres)} \nMoyenne : {Moyenne(listeNombres)}")
    