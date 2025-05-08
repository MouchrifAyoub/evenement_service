from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from app.config.settings import POSTGRES_SCHEMA
from app.models.base import Base

class Logistique(Base):
    __tablename__ = "logistique"

    id = Column(Integer, primary_key=True, index=True)
    materiel_necessaire = Column(String, nullable=True)
    transport_necessaire = Column(String, nullable=True)

    evenement_id = Column(Integer, ForeignKey("evenement.id"), nullable=False)
