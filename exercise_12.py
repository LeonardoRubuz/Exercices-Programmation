class Date:
    nomsMois = [
        "Janvier",
        "Février",
        "Mars",
        "Avril",
        "Mai",
        "Juin",
        "Juillet",
        "Août",
        "Septembre",
        "Octobre",
        "Novembre",
        "Décembre"
    ]
    def __init__(self, jour, mois, année):
        if jour < 1 or jour > 31:
            raise ValueError("Le jour doit être compris entre 1 et 31.")
        if mois < 1 or mois > 12:
            raise ValueError("Le mois doit être compris entre 1 et 12.")
        if année < 1 or année > 9999:
            raise ValueError("L'année doit être comprise entre 1 et 9999.")
        self.jour = jour
        self.mois = mois
        self.année = année

    def __str__(self):
        return f"{self.jour}/{self.mois}/{self.année}"

    def __repr__(self):
        return f"Date({self.jour}, {self.nomsMois[self.mois - 1]}, {self.année})"