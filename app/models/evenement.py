from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from enum import Enum as PyEnum
from app.config.settings import POSTGRES_SCHEMA
from app.models.base import Base

class StatutEvenementEnum(str, PyEnum):
    EN_PREPARATION = "en_preparation"
    PRET = "pret"
    ANNULE = "annule"

class Evenement(Base):
    __tablename__ = "evenement"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, nullable=False)
    date_evenement = Column(Date, nullable=False)
    lieu = Column(String, nullable=False)
    nb_participants = Column(Integer, nullable=True)
    status = Column(Enum(StatutEvenementEnum), default=StatutEvenementEnum.EN_PREPARATION)

    demande_id = Column(Integer, ForeignKey("demande_evenement.id"), nullable=False)
