
# 🎉 evenement_service

Microservice FastAPI pour la gestion des demandes d’événements au sein de la FMS – UM6P.  
Ce service permet aux utilisateurs authentifiés de soumettre des événements, de suivre leur statut, et aux responsables de les traiter et les finaliser.

---

## 🧱 Stack technique

- **Langage** : Python 3.11+
- **Framework** : FastAPI (async)
- **Base de données** : PostgreSQL (schéma `evenement`)
- **Connexion DB** : `databases + asyncpg`
- **Migrations** : Alembic
- **Gestion dépendances** : Poetry

---

## 📦 Installation locale

```bash
git clone https://github.com/MouchrifAyoub/evenement_service.git
cd evenement_service
poetry install
```

Ajoutez un fichier `.env` à la racine :

```
DATABASE_URL=postgresql+asyncpg://<user>:<pass>@localhost:5432/evenement_db
POSTGRES_SCHEMA=evenement
APP_ENV=dev
```

---

## 🗄️ Migration de base de données

```bash
alembic revision --autogenerate -m "initial"
alembic upgrade head
```

---

## 🚀 Lancer le serveur

```bash
poetry run uvicorn app.main:app --reload
```

Swagger UI dispo via : [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📘 Endpoints disponibles

| Méthode | Endpoint                         | Description                                 |
|---------|----------------------------------|---------------------------------------------|
| `POST`  | `/evenements`                   | Soumettre une demande d’événement           |
| `GET`   | `/mes-evenements`               | Lister mes demandes                         |
| `GET`   | `/evenements-valides`           | Voir les événements validés (BDE)           |
| `PUT`   | `/evenements/{id}/traiter`      | Valider ou refuser une demande              |
| `PATCH` | `/evenements/{id}/statut`       | Mettre à jour le statut après validation    |

---

## 🧠 Règles métier clés

- Un événement doit être soumis ≥ 6 semaines avant la date prévue
- Routage automatique selon le profil (étudiant → Student Life, sinon → Communication)
- Un refus nécessite un motif obligatoire
- Les transitions de statut sont strictement contrôlées (`en_attente` → `valide/refusé` → `prêt/annulé`)
- Accès protégé via `get_current_user` (prévu pour intégration Keycloak)

---

## 📂 Structure

```
evenement_service/
├── app/
│   ├── api/                # Routes FastAPI
│   ├── config/             # Chargement env & settings
│   ├── db/                 # Connexion DB
│   ├── models/             # Modèles SQLAlchemy
│   ├── repositories/       # Accès base de données
│   ├── schemas/            # Schémas Pydantic
│   ├── services/           # Logique métier
│   └── main.py             # Point d'entrée
├── alembic/                # Migrations
├── README.md
└── pyproject.toml
```

---

## 🧪 Tests manuels réalisés

- ✅ Création avec données valides
- ✅ Refus si date < 6 semaines
- ✅ Statut modifiable uniquement après validation
- ✅ Motif obligatoire en cas de refus
- ✅ Protection contre traitement ou update non autorisé

---

## ✍️ Auteur

Mouchrif Ayoub – PFE 2025 – FMS / UM6P

---

## 📄 Licence

Ce projet est privé. Toute reproduction ou diffusion non autorisée est interdite.
