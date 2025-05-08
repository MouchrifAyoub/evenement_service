from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from app.config.settings import POSTGRES_SCHEMA
from app.models.base import Base

class Budget(Base):
    __tablename__ = "budget"

    id = Column(Integer, primary_key=True, index=True)
    montant_estime = Column(Integer, nullable=False)
    montant_valide = Column(Integer, nullable=True)
    valide_par_service_financier = Column(Boolean, default=False)

    evenement_id = Column(Integer, ForeignKey("evenement.id"), nullable=False)
