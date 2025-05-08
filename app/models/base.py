from sqlalchemy.orm import declarative_base
from sqlalchemy.schema import MetaData
from app.config.settings import POSTGRES_SCHEMA

metadata = MetaData(schema=POSTGRES_SCHEMA)
Base = declarative_base(metadata=metadata)
