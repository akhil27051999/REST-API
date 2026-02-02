import os
from dotenv import load_dotenv

# Base class that does not load .env yet

class Config:

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTGRES_USER = None
    POSTGRES_PASSWORD = None
    POSTGRES_DATABASE = None
    POSTGRES_HOST = "localhost"
    POSTGRES_PORT = "5432"

    SQLALCHEMY_DATABASE_URI = None

# Dev configuration

class DevConfig(Config):

    # Loads env variables from .env file
    load_dotenv(dotenv_path=".env")  

    DEBUG = os.getenv("DEBUG") == "True"
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
    )