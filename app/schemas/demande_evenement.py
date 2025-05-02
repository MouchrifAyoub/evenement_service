from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from enum import Enum


class StatutDemandeEnum(str, Enum):
    EN_ATTENTE = "en_attente"
    VALIDE = "valide"
    REFUSEE = "refusee"


class DemandeEvenementBase(BaseModel):
    titre: str
    description: Optional[str] = None
    lieux: str
    date_evenement: date


class DemandeEvenementCreate(DemandeEvenementBase):
    est_etudiant: bool = False


class DemandeEvenementRead(DemandeEvenementBase):
    id: int
    statut: StatutDemandeEnum
    motif_refus: Optional[str] = None
    cree_par: int

    model_config = {
        "from_attributes": True
    }
