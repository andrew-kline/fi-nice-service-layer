import argparse
import logging

from finice.db import downgrade_db, migrate_db, upgrade_db


logger = logging.getLogger("finice.cli")

def upgrade_database():
    upgrade_db()

def downgrade_database():
    downgrade_db()

def create_revision():
    parser = argparse.ArgumentParser(description="Create a revision using Alembic's auto migration")
    parser.add_argument("--msg", type=str, action="store", required=True)
    args = parser.parse_args()
    migrate_db(args.msg)