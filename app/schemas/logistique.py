from pydantic import BaseModel
from typing import Optional


class LogistiqueBase(BaseModel):
    materiel_necessaire: Optional[str] = None
    transport_necessaire: Optional[str] = None


class LogistiqueCreate(LogistiqueBase):
    evenement_id: int


class LogistiqueRead(LogistiqueBase):
    id: int

    model_config = {
        "from_attributes": True
    }
