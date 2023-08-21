phrase = 'Winterfell se souvient de Stark'

reversedPhrase = phrase.split()
reversedPhrase.append(reversedPhrase[0])
reversedPhrase[0] = reversedPhrase[-2]
reversedPhrase.pop(-2)
reversedPhrase = ' '.join(reversedPhrase)

print(reversedPhrase)