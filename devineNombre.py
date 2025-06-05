import random
secret = random.randint(1,100)

print("J'ai choisi un nombre entre 1 et 100, essaie de le deviner")

inputUser = int(input())

while inputUser != secret:
    if inputUser < secret:
        print("C'est plus")
        inputUser = int(input())
    
    if inputUser > secret:
        print("C'est moins")
        inputUser = int(input())

print(f"GG t'as trouvé c'était {secret}")