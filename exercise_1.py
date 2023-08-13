# Transformer 42569 secondes en  heures, minutes et secondes
# On sait que :
# 1s = 1/60 min
# 1min = 1/60 heures

given_time = 42569
minutes = given_time // 60   # On convertit en minutes
seconds = given_time % 60    # On recupère le reste de la division 
hours = minutes // 60        # On convertit les minutes en heures
minutes %= 60                # Le reste de la division devient les minutes actuelles

# Affichage des résultats
print(
    given_time,
    ' secondes converties en heures, minutes et secondes deviennent : ',
    str(hours)+' heures '+ str(minutes)+' minutes et '+ str(seconds)+ ' secondes.'
)

# Alternative : Fonction de conversion de n'importe quel nombre de secondes
def secondsConverter(given_seconds):
    hours = given_seconds // 3600
    minutes = (given_seconds // 60) % 60
    seconds = given_seconds % 60
    return print(f' {str(given_seconds)} secondes font : {str(hours)}heures, {str(minutes)}minutes et {str(seconds)}secondes')

secondsConverter(42569)