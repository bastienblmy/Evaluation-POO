import ui
import data_manager
from models.tarifs import TarifsManager


def pause():
    input("\nAppuyez sur Entrée pour revenir au menu...")


def main():
    clients = data_manager.charger_clients()
    vehicules = data_manager.charger_vehicules()

    while True:
        ui.afficher_menu()
        choix = ui.demander_choix()

        if choix == "1":
            ui.afficher_clients(clients)
            pause()

        elif choix == "2":
            ui.afficher_vehicules(vehicules)
            pause()

        elif choix == "3":
            reservation = ui.demander_reservation(clients, vehicules, data_manager)
            if reservation is not None:
                rep = input("Sauvegarder cette réservation ? (o/n) : ").strip().lower()
                if rep == "o":
                    data_manager.sauvegarder_reservation(reservation)
                    print("✓ Réservation enregistrée avec succès !")
                    pause()

        elif choix == "4":
            TarifsManager.afficher_grille()
            pause()

        elif choix == "5":
            reservations = data_manager.charger_reservations()
            ui.afficher_reservations(reservations)
            pause()

        elif choix == "6":
            id_client = input("ID du client : ").strip()
            reservations = data_manager.filtrer_reservations_par_client(id_client)
            ui.afficher_reservations_client(reservations, id_client)
            pause()

        elif choix == "7":
            break

        else:
            print("Choix invalide.")
            pause()


if __name__ == "__main__":
    main()