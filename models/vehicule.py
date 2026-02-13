class Vehicule:
    def __init__(self, id_vehicule, marque, modele, cylindree, kilometrage_actuel, date_mise_en_circulation):
        self.id_vehicule = id_vehicule
        self.marque = marque
        self.modele = modele
        self.cylindree = cylindree
        self.kilometrage_actuel = kilometrage_actuel
        self.date_mise_en_circulation = date_mise_en_circulation

    def __str__(self):
        return f"{self.id_vehicule} - {self.marque} {self.modele} ({self.cylindree})"
    
    def to_dict(self):
        return {
            "id_vehicule": self.id_vehicule,
            "marque": self.marque,
            "modele": self.modele,
            "cylindree": self.cylindree,
            "kilometrage_actuel": self.kilometrage_actuel,
            "date_mise_en_circulation": self.date_mise_en_circulation,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            d.get("id_vehicule", ""),
            d.get("marque", ""),
            d.get("modele", ""),
            d.get("cylindree", 0),
            d.get("kilometrage_actuel", 0),
            d.get("date_mise_en_circulation", ""),
        )