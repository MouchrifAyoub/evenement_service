from pydantic import BaseModel
from typing import Optional


class BudgetBase(BaseModel):
    montant_estime: int
    montant_valide: Optional[int] = None
    valide_par_service_financier: bool = False


class BudgetCreate(BudgetBase):
    evenement_id: int


class BudgetRead(BudgetBase):
    id: int

    model_config = {
        "from_attributes": True
    }
