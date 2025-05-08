import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config, AsyncEngine

from alembic import context
from app.config.settings import DATABASE_URL, POSTGRES_SCHEMA
from app.models.base import Base
# Importer ici tes modèles SQLAlchemy
from app.models import demande_evenement, evenement, budget, logistique

# Alembic Config object
config = context.config

# Interpréter le fichier de config pour Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata pour 'autogenerate' Alembic
target_metadata = Base.metadata

# Injecter dynamiquement DATABASE_URL depuis settings
if config.get_main_option("sqlalchemy.url") == "":
    config.set_main_option("sqlalchemy.url", DATABASE_URL)

# ✅ Ajout ici pour filtrer uniquement le schéma `evenement`
def include_object(obj, name, type_, reflected, compare_to):
    return getattr(obj, "schema", POSTGRES_SCHEMA) == POSTGRES_SCHEMA


def run_migrations_offline() -> None:
    """Run migrations en mode offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        version_table_schema=POSTGRES_SCHEMA,
        include_schemas=True,
        include_object=include_object,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        version_table_schema=POSTGRES_SCHEMA,
        include_schemas=True,
        include_object=include_object,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations en mode online."""
    connectable: AsyncEngine = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
