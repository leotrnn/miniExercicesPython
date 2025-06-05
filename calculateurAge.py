from datetime import datetime
current_year = datetime.now().year

name = input("Comment tu t'appelles\n")

while (True) :
    yearInput = input("T'es né en quelle année\n")
    
    try:
        year = int(yearInput)
        if 1900 <= year <= current_year:
            break    
    except ValueError:
        print(f"Entre une année valide entre 1900 et {current_year}")


age = current_year - year

print(f"{name}, tu as environ {age} ans.")
