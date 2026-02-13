# Évaluation POO – Location de véhicules

Structure initiale du projet.

## Spécification des modèles (classes)

### 1) Client
Représente un client du service de location.

**Attributs :**
- `id_client` (str) : identifiant unique du client
- `nom` (str) : nom de famille
- `prenom` (str) : prénom
- `mail` (str) : adresse e-mail
- `telephone` (str) : numéro de téléphone
- `adresse` (str) : adresse postale

**Rôle :**
- Identifier le locataire et stocker ses informations de contact.

---

### 2) Vehicule
Représente un véhicule disponible à la location.

**Attributs :**
- `id_vehicule` (str) : identifiant unique du véhicule 
- `marque` (str) : marque (ex: "Renault")
- `modele` (str) : modèle (ex: "Clio")
- `cylindree` (int) : cylindrée (ex: 4, 5 ou 6 cylindres)
- `kilometrage_actuel` (float) : kilométrage actuel du véhicule
- `date_mise_en_circulation` (str) : date au format "AAAA-MM-JJ"

**Rôle :**
- Décrire un véhicule et ses caractéristiques nécessaires au calcul des tarifs.

---

### 3) Reservation
Représente une réservation de location pour un client et un véhicule.

**Attributs :**
- `id_reservation` (str) : identifiant unique de réservation 
- `id_client` (str) : identifiant du client concerné
- `id_vehicule` (str) : identifiant du véhicule loué
- `date_depart` (str) : date de départ "AAAA-MM-JJ"
- `date_retour` (str) : date de retour "AAAA-MM-JJ"
- `forfait_km` (int | str) : forfait kilométrique (100, 200, 300 ou "+300")
- `cout_journalier` (float) : coût par jour calculé via la grille tarifaire
- `prix_km_supp` (float) : prix du km supplémentaire (selon grille)
- `cout_estime` (float) : estimation du coût total (au minimum coût_journalier * nb_jours)

**Rôle :**
- Relier un client et un véhicule sur une période donnée, stocker le forfait et les tarifs appliqués, et fournir une estimation du coût.
