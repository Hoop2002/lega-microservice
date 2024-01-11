from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_MIGRATION_URL = os.getenv("DATABASE_MIGRATION_URL")