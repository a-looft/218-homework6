from app.calculator_app import run
from dotenv import load_dotenv
import os
import logging
import logging.config

if __name__ == "__main__":
    run()

load_dotenv()
env = os.getenv("ENVIRONMENT", "production")
print(f"Running in {env} mode")

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger.info("Starting calculator")
