from models.tarifs import TarifsManager
from models.reservation import Reservation



def afficher_menu():
    print("============================================================")
    print("SYSTÈME DE LOCATION DE VÉHICULES")
    print("============================================================")
    print("1. Afficher les clients")
    print("2. Afficher les véhicules")
    print("7. Quitter")
    print("============================================================")



def demander_choix():
    return input("Votre choix : ").strip()



def afficher_clients(clients):
    print("============================================================")
    print("LISTE DES CLIENTS")
    print("============================================================")
    for c in clients:
        print(c)
    print("============================================================")



def afficher_vehicules(vehicules):
    print("============================================================")
    print("LISTE DES VÉHICULES")
    print("============================================================")
    for v in vehicules:
        print(v)
    print("============================================================")



def demander_reservation(clients, vehicules, data_manager):
    print("============================================================")
    print("CRÉER UNE NOUVELLE RÉSERVATION")
    print("============================================================")

    print("Clients disponibles :")
    for c in clients:
        print(c)

    id_client = input("ID du client : ").strip()

    print("Véhicules disponibles :")
    for v in vehicules:
        print(v)

    id_vehicule = input("ID du véhicule : ").strip()

    date_depart = input("Date de départ (AAAA-MM-JJ) : ").strip()
    date_retour = input("Date de retour (AAAA-MM-JJ) : ").strip()

    fk_raw = input("Forfait kilométrique (100, 200, 300, +300) : ").strip()
    forfait_km = fk_raw if fk_raw == "+300" else int(fk_raw)

    vehicule = None
    for v in vehicules:
        if v.id_vehicule == id_vehicule:
            vehicule = v
            break

    if vehicule is None:
        print("Erreur : véhicule introuvable.")
        return None

    tarif = TarifsManager.obtenir_tarif(vehicule.cylindree, forfait_km)
    if tarif is None:
        print("Erreur : tarif introuvable pour cette cylindrée/ce forfait.")
        return None

    cout_journalier, prix_km_supp = tarif

    reservations = data_manager.charger_reservations()
    id_reservation = data_manager.generer_id_reservation(reservations)

    reservation = Reservation(
        id_reservation,
        id_client,
        id_vehicule,
        date_depart,
        date_retour,
        forfait_km,
        cout_journalier,
        prix_km_supp,
    )

    print("============================================================")
    print("RÉCAPITULATIF DE LA RÉSERVATION")
    print("============================================================")
    print(f"Réservation {reservation.id_reservation}")
    print(f"Client : {reservation.id_client}")
    print(f"Véhicule : {reservation.id_vehicule}")
    print(f"Du {reservation.date_depart} au {reservation.date_retour}")
    print(f"Forfait : {reservation.forfait_km} km")
    print(f"Coût journalier : {reservation.cout_journalier}€")
    print(f"Prix km supp. : {reservation.prix_km_supp}€/km")
    print(f"Coût estimé : {reservation.cout_estime:.2f}€")
    print("============================================================")

    return reservation   



def afficher_reservations(reservations):
    print("============================================================")
    print("LISTE DES RÉSERVATIONS")
    print("============================================================")
    for r in reservations:
        print(f"{r.id_reservation} | Client: {r.id_client} | Véhicule: {r.id_vehicule} | {r.date_depart} -> {r.date_retour} | Forfait: {r.forfait_km} | Coût estimé: {r.cout_estime:.2f}€")
    print("============================================================")



def afficher_reservations_client(reservations, id_client):
    print("============================================================")
    print(f"RÉSERVATIONS DU CLIENT {id_client}")
    print("============================================================")
    for r in reservations:
        print(f"{r.id_reservation} | Client: {r.id_client} | Véhicule: {r.id_vehicule} | {r.date_depart} -> {r.date_retour} | Forfait: {r.forfait_km} | Coût estimé: {r.cout_estime:.2f}€")
    print("============================================================")    