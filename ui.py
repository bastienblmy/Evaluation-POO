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