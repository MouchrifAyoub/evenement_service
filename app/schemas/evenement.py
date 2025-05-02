from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum


class StatutEvenementEnum(str, Enum):
    EN_PREPARATION = "en_preparation"
    PRET = "pret"
    ANNULE = "annule"


class EvenementBase(BaseModel):
    titre: str
    date_evenement: date
    lieu: str
    nb_participants: Optional[int] = None


class EvenementCreate(EvenementBase):
    demande_id: int


class EvenementRead(EvenementBase):
    id: int
    status: StatutEvenementEnum

    model_config = {
        "from_attributes": True
    }


class EvenementUpdateStatut(BaseModel):
    status: StatutEvenementEnum
