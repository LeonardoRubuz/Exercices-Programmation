voyelles = ['a','e','i','o','u','y']
voyellesCount = 0
valeur = input('Veuillez renseigner un texte : ')

for element in valeur:
    if (element in voyelles):
        voyellesCount += 1

print(f"La chaine {valeur} possède {voyellesCount} voyelles")