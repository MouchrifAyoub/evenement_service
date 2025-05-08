from sqlalchemy import Column, Integer, String, Date, Enum, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from enum import Enum as PyEnum
from app.config.settings import POSTGRES_SCHEMA
from app.models.base import Base

class StatutDemandeEnum(str, PyEnum):
    EN_ATTENTE = "en_attente"
    VALIDE = "valide"
    REFUSEE = "refusee"

class DemandeEvenement(Base):
    __tablename__ = "demande_evenement"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    lieux = Column(String, nullable=False)
    date_evenement = Column(Date, nullable=False)
    statut = Column(Enum(StatutDemandeEnum), default=StatutDemandeEnum.EN_ATTENTE)
    motif_refus = Column(Text, nullable=True)
    cree_par = Column(Integer, nullable=False)  # id utilisateur (ex: récupéré de l'authent)
