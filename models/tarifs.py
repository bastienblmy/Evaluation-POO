class TarifsManager:
    TARIFS = {
        4: {100: (35.0, 0.25), 200: (50.0, 0.20)},
        5: {100: (45.0, 0.30)},
        6: {100: (60.0, 0.40)}}

    @classmethod
    def obtenir_tarif(cls, cylindree, forfait_km):
        return None

    @classmethod
    def afficher_grille(cls):
        pass