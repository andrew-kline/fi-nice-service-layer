import contextlib
import os
from typing import Optional, TYPE_CHECKING

from alembic.config import Config
from alembic import command
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from finice import config

if TYPE_CHECKING:
    from sqlalchemy.engine import Engine

Base = declarative_base()

ALEMBIC_INI_PATH = os.path.join(os.path.dirname(__file__), "alembic/alembic.ini")
ALEMBIC_SCRIPTS_PATH = os.path.join(os.path.dirname(__file__), "alembic")

DEFAULT_DB_ENGINE: "Engine" = create_engine(
    config.DATABASE_URI, echo=False, pool_pre_ping=True
)


@contextlib.contextmanager
def get_session(engine: Optional["Engine"] = DEFAULT_DB_ENGINE) -> scoped_session:
    """
    Create a thread-safe sqlalchemy Session 

    Example use:
        with get_session() as session:
            user = User(name="test")
            session.add(user)

    Args:
        engine (Optional[Engine]): SQLAlchemy engine, default will utilize the database URL set via the environment

    Returns:
        scoped_session    
    """
    sess_obj = scoped_session(sessionmaker(bind=engine))
    session = sess_obj()
    try:
        yield session
        session.commit()
        session.flush()
    except Exception:
        session.rollback()
        raise
    finally:
        sess_obj.remove()


def init_alembic(db_uri: Optional[str] = config.DATABASE_URI) -> Config:
    """Common alembic command initialization steps"""
    alembic_cfg = Config(ALEMBIC_INI_PATH)
    alembic_cfg.set_main_option("sqlalchemy.url", db_uri)
    alembic_cfg.set_main_option("script_location", ALEMBIC_SCRIPTS_PATH)

    return alembic_cfg


def upgrade_db(db_uri: Optional[str] = None):
    command.upgrade(init_alembic(), "head")


def downgrade_db(db_uri: Optional[str] = None):
    command.downgrade(init_alembic(), "-1")


def migrate_db(message: Optional[str] = "", db_uri: Optional[str] = None):
    alembic_cfg = init_alembic()
    alembic_cfg.set_main_option("compare_type", "true")
    command.revision(alembic_cfg, message, autogenerate=True)
