s = input("Entrez une chaine de caractère : ")

# Séparer la chaine en une liste de mots en utilisant l'espace comme séparateur
mots = s.split()

# Échanger le premier et le dernier mot de la liste
mots[0], mots[-1] = mots[-1], mots[0]

# Recréer une chaine en joignant les mots de la liste avec des espaces
s_echangee = " ".join(mots)

print(s_echangee)
