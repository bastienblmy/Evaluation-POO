from datetime import date

class Reservation:
    def __init__(self, id_reservation, id_client, id_vehicule, date_depart, date_retour, forfait_km, cout_journalier, prix_km_supp, cout_estime):
        self.id_reservation = id_reservation
        self.id_client = id_client
        self.id_vehicule = id_vehicule
        self.date_depart = date_depart
        self.date_retour = date_retour
        self.forfait_km = forfait_km
        self.cout_journalier = cout_journalier
        self.prix_km_supp = prix_km_supp
        self.cout_estime = self._calculer_cout_estime()

    
    def _calculer_cout_estime(self):
        d1 = date.fromisoformat(self.date_depart)
        d2 = date.fromisoformat(self.date_retour)
        nb_jours = (d2 - d1).days
        if nb_jours < 1:
            nb_jours = 1
        return nb_jours * self.cout_journalier