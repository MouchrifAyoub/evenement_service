import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config, AsyncEngine

from alembic import context
from app.config.settings import DATABASE_URL, POSTGRES_SCHEMA

# 📦 Import direct de tous les modèles
from app.models import demande_evenement, evenement, budget, logistique

# 📊 Config Alembic
config = context.config

# 🧾 Logging config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 🎯 Target metadata : liste explicite des modèles
target_metadata = [
    demande_evenement.DemandeEvenement.metadata,
    evenement.Evenement.metadata,
    budget.Budget.metadata,
    logistique.Logistique.metadata,
]

# 🔗 Injection dynamique de la DB URL (depuis settings.py)
if config.get_main_option("sqlalchemy.url") in ("", None):
    config.set_main_option("sqlalchemy.url", DATABASE_URL)

# 🔍 Ne migrer que le schéma 'evenement'
def include_object(obj, name, type_, reflected, compare_to):
    return getattr(obj, "schema", None) == POSTGRES_SCHEMA

def run_migrations_offline() -> None:
    """Migrations offline"""
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
    """Migrations async online"""
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
