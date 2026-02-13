class Client:
    def __init__(self, id_client, nom, prenom, mail, telephone, adresse):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.telephone = telephone
        self.adresse = adresse

    def __str__(self):
        return f"{self.id_client} - {self.prenom} {self.nom}"
    
    def to_dict(self):
        return {
            "id_client": self.id_client,
            "nom": self.nom,
            "prenom": self.prenom,
            "mail": self.mail,
            "telephone": self.telephone,
            "adresse": self.adresse,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            d.get("id_client", ""),
            d.get("nom", ""),
            d.get("prenom", ""),
            d.get("mail", ""),
            d.get("telephone", ""),
            d.get("adresse", ""),
        )