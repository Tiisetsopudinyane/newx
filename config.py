import os

from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

MEDIA_ROOT = os.path.join(BASE_DIR, "accounts", "static")

UPLOAD_FOLDER = os.path.join(MEDIA_ROOT, "profile")

load_dotenv(os.path.join(BASE_DIR, ".env"))


class BaseConfig:
    # Application configuration
    DEBUG = False
    TESTING = False

    SITE_URL = os.getenv("SITE_DOMAIN", "http://localhost:5000")

    # Site secret key or bootstrap UI theme.
    SECRET_KEY = os.getenv("SECRET_KEY", "my-sekret-key")
    BOOTSTRAP_BOOTSWATCH_THEME = "sketchy"

    # WTF Form and recaptcha configuration
    WTF_CSRF_SECRET_KEY = os.getenv("CSRF_SECRET_KEY", None)
    WTF_CSRF_ENABLED = True


    # SQLAlchemy (ORM) configuration
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Mail configuration
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_PORT = 587
    MAIL_USE_TLS = True  # Enable TLS
    MAIL_USE_SSL = False  # SSL should remain False



class Development(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", None)


class Production(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", None)


class Testing(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", None)


development = Development()

production = Production()

testing = Testing()