from finice.configuration import (
    ProductionConfig,
    DevelopmentConfig,
    TestingConfig,
    LocalConfig,
)
from finice.settings import ENVIRONMENT

if ENVIRONMENT == "prod":
    config = ProductionConfig()
elif ENVIRONMENT == "dev":
    config = DevelopmentConfig()
elif ENVIRONMENT == "testing":
    config = TestingConfig()
elif ENVIRONMENT == "local":
    config = LocalConfig()
else:
    raise ValueError("Invalid environment specified")
