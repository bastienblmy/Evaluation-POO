class TarifsManager:
    TARIFS = {
        4: {100: (35.0, 0.25), 200: (50.0, 0.20), 300: (65.00, 0.15), "+300": (80.00, 0.10)},
        5: {100: (45.0, 0.30), 200: (60.00, 0.25), 300: (75.00, 0.20), "+300": (95.00, 0.15)},
        6: {100: (60.0, 0.40), 200: (80.00, 0.35), 300: (100.00, 0.30), "+300": (120.00, 0.25)}}

    @classmethod
    def obtenir_tarif(cls, cylindree, forfait_km):
        if cylindree not in cls.TARIFS:
            return None
        return cls.TARIFS[cylindree].get(forfait_km)

    @classmethod
    def afficher_grille(cls):
        print("======================================================================")
        print("GRILLE TARIFAIRE")
        print("======================================================================")
        print("Cylindrée Forfait Coût/jour Prix km supp.")
        print("----------------------------------------------------------------------")

        for cylindree in (4, 5, 6):
            for forfait in (100, 200, 300, "+300"):
                cout_jour, prix_km = cls.TARIFS[cylindree][forfait]
                print(f"{cylindree} cylindres {forfait} {cout_jour:.2f}€ {prix_km:.2f}€/km")
            print("----------------------------------------------------------------------")