class Date:
  noms_mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

  def __init__(self, jour, mois, annee):
    if self.est_date_valide(jour, mois, annee):
      self.jour = jour
      self.mois = mois
      self.annee = annee
    else:
      raise Exception("Date invalide")

  def __repr__(self):
    nom_mois = self.noms_mois[self.mois - 1]
    return f"{self.jour} {nom_mois} {self.annee}"

  def __lt__(self, autre):
    if self.annee < autre.annee:
      return True
    elif self.annee > autre.annee:
      return False
    else:
      if self.mois < autre.mois:
        return True
      elif self.mois > autre.mois:
        return False
      else:
        if self.jour < autre.jour:
          return True
        else:
          return False

  @staticmethod
  def est_date_valide(jour, mois, annee):
    if not isinstance(jour, int) or not isinstance(mois, int) or not isinstance(annee, int):
      return False
    if jour <= 0 or mois <= 0 or annee <= 0:
      return False

    if mois < 1 or mois > 12:
      return False

    nb_jours_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if jour < 1 or jour > nb_jours_mois[mois - 1]:
      return False

    return True


d1 = Date(25, 1, 1989)
print(d1) 

d2 = Date(32, 14, 2020) # Affiche "Date invalide" et arrête le programme

# Créer deux dates valides et comparer leur ordre chronologique
d3 = Date(15, 3, 2020)
d4 = Date(15, 4, 2020)
print(d3 < d4) # Affiche True 
