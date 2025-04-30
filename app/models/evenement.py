from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    DateTime,
    Enum,
    Boolean,
    func,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from app.config.settings import POSTGRES_SCHEMA
import enum


# Métadonnées avec schéma personnalisé
metadata = MetaData(schema=POSTGRES_SCHEMA)
Base = declarative_base(metadata=metadata)

class EventStatutEnum(str, enum.Enum):
    EN_ATTENTE = "en_attente"
    VALIDE = "valide"
    REFUSE = "refuse"
    EN_PREPARATION = "en_preparation"
    PRET = "pret"
    ANNULE = "annule"


class Evenement(Base):
    __tablename__ = "evenements"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    date_evenement = Column(Date, nullable=False)
    lieu = Column(String(255), nullable=False)
    budget_estime = Column(Integer, nullable=True)
    besoins_logistiques = Column(Text, nullable=True)

    statut = Column(
        Enum(EventStatutEnum, name="event_statut_enum"),
        default=EventStatutEnum.EN_ATTENTE,
        nullable=False,
    )
    commentaire_refus = Column(Text, nullable=True)  # visible après traitement

    cree_par = Column(Integer, nullable=False)  # ID utilisateur (auth)
    est_etudiant = Column(Boolean, default=False, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
