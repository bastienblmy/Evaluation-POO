import ui


def main():
    while True:
        ui.afficher_menu()
        choix = ui.demander_choix()

        if choix == "7":
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()