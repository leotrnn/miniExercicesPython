error = False
counter = 0

print("Counting du pauvre")

while error == False:
    inputUser = int(input())
    if inputUser != (counter + 1):
        print(f"Blud sait pas compter bah la honte, t'as fais {counter}")
        error = True
        break
    counter = counter + 1
    