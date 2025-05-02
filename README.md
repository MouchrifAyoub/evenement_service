
# 🎯 Service de Gestion des Événements

Ce projet est un microservice dédié à la gestion des événements au sein de la FMS. Il permet la création, la validation et le suivi des demandes d'événements, ainsi que la gestion des événements validés.

## 🚀 Fonctionnalités principales

- Création de demandes d'événements : Les utilisateurs peuvent soumettre des demandes d'organisation d'événements.
- Validation des demandes : Les administrateurs peuvent valider ou refuser les demandes soumises.
- Création d'événements : Une fois une demande validée, un événement peut être créé.
- Suivi des événements : Les utilisateurs peuvent suivre l'état de leurs événements.

## 📚 Documentation des Endpoints

### 📌 Demandes d'événements

- **POST** `/api/demandes-evenements`
  Créer une nouvelle demande d'événement.
  Payload JSON :
  ```json
  {
    "titre": "Conférence annuelle",
    "description": "Une conférence sur les dernières avancées technologiques.",
    "lieux": "Amphithéâtre A",
    "date_evenement": "2025-10-15",
    "est_etudiant": true
  }
  ```

- **GET** `/api/mes-demandes-evenements`
  Récupérer toutes les demandes soumises par l'utilisateur connecté.

- **PUT** `/api/demandes-evenements/{id}/traiter`
  Valider ou refuser une demande d'événement.
  Payload JSON :
  ```json
  {
    "statut": "valide", // ou "refusee"
    "motif_refus": "Manque de budget" // requis si statut est "refusee"
  }
  ```

### 📌 Événements

- **POST** `/api/evenements`
  Créer un nouvel événement à partir d'une demande validée.
  Payload JSON :
  ```json
  {
    "titre": "Conférence annuelle",
    "date_evenement": "2025-10-15",
    "lieu": "Amphithéâtre A",
    "nb_participants": 150,
    "demande_id": 1
  }
  ```

- **PATCH** `/api/evenements/{id}/statut`
  Mettre à jour le statut d'un événement.
  Payload JSON :
  ```json
  {
    "statut": "en_preparation" // ou "pret", "annule"
  }
  ```

## 🧪 Tests

Des tests unitaires ont été mis en place pour assurer la fiabilité des fonctionnalités principales du service.

## 📌 Notes supplémentaires

- L'application expose automatiquement une documentation interactive via Swagger UI accessible à l'adresse : `http://localhost:8000/docs`.
- Les statuts possibles pour les demandes sont : `en_attente`, `valide`, `refusee`.
- Les statuts possibles pour les événements sont : `en_preparation`, `pret`, `annule`.
