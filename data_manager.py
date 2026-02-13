import json
from models.client import Client
from models.vehicule import Vehicule
from models.reservation import Reservation



def charger_clients():
    with open("clients.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Client.from_dict(d) for d in data]



def charger_vehicules():
    with open("vehicules.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Vehicule.from_dict(d) for d in data]



def charger_reservations():
    with open("reservations.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    reservations = []
    for d in data:
        r = Reservation(
            d.get("id_reservation", ""),
            d.get("id_client", ""),
            d.get("id_vehicule", ""),
            d.get("date_depart", ""),
            d.get("date_retour", ""),
            d.get("forfait_km", 100),
            d.get("cout_journalier", 0),
            d.get("prix_km_supp", 0),
        )
        if "cout_estime" in d:
            r.cout_estime = d["cout_estime"]
        reservations.append(r)

    return reservations



def sauvegarder_reservation(reservation):
    with open("reservations.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    data.append({
        "id_reservation": reservation.id_reservation,
        "id_client": reservation.id_client,
        "id_vehicule": reservation.id_vehicule,
        "date_depart": reservation.date_depart,
        "date_retour": reservation.date_retour,
        "forfait_km": reservation.forfait_km,
        "cout_journalier": reservation.cout_journalier,
        "prix_km_supp": reservation.prix_km_supp,
        "cout_estime": reservation.cout_estime,
    })

    with open("reservations.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)



def generer_id_reservation(reservations):
    max_num = 0
    for r in reservations:
        s = str(r.id_reservation).replace("R", "")
        if s.isdigit():
            n = int(s)
            if n > max_num:
                max_num = n
    return f"R{max_num + 1:04d}"



def filtrer_reservations_par_client(id_client):
    reservations = charger_reservations()
    return [r for r in reservations if r.id_client == id_client]