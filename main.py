import ui
import data_manager


def main():
    clients = data_manager.charger_clients()
    vehicules = data_manager.charger_vehicules()

    while True:
        ui.afficher_menu()
        choix = ui.demander_choix()

        if choix == "1":
            ui.afficher_clients(clients)

        elif choix == "2":
            ui.afficher_vehicules(vehicules)

        elif choix == "7":
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()