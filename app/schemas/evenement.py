from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from enum import Enum


class EventStatutEnum(str, Enum):
    EN_ATTENTE = "en_attente"
    VALIDE = "valide"
    REFUSE = "refuse"
    EN_PREPARATION = "en_preparation"
    PRET = "pret"
    ANNULE = "annule"


class EvenementBase(BaseModel):
    nom: str
    description: Optional[str] = None
    date_evenement: date
    lieu: str
    budget_estime: Optional[int] = None
    besoins_logistiques: Optional[str] = None


class EvenementCreate(EvenementBase):
    est_etudiant: bool = False


class EvenementRead(EvenementBase):
    id: int
    statut: EventStatutEnum
    commentaire_refus: Optional[str] = None
    cree_par: int
    created_at: datetime

    model_config = {
        "from_attributes": True  # remplace orm_mode pour Pydantic v2
    }


class EvenementUpdateStatut(BaseModel):
    statut: EventStatutEnum


class EvenementTraiter(BaseModel):
    statut: EventStatutEnum
    commentaire_refus: Optional[str] = None
