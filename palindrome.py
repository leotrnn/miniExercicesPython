inputUser = input("Entrez une chaîne : ")


if str(inputUser) == str(inputUser[::-1]):
    print(f"{inputUser} est un palindrome")
else:
    print(f"{inputUser} n'est pas un palindrome")