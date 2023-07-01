import os

PG_USER = os.getenv("PG_USER", "postgres")
PG_PASS = os.getenv("PG_PASS", "postgres")
ENVIRONMENT = os.getenv("ENV", "dev")
