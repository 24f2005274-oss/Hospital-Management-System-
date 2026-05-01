import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-secret-key')
    
    # Database Setup
    # Use SQLite for local development by default
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"sqlite:///{os.path.join(BASE_DIR, 'hospital_os.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Optional Redis / Celery Setup (Production)
    REDIS_URL = os.environ.get('REDIS_URL', None)
    if REDIS_URL:
        CELERY_BROKER_URL = REDIS_URL
        CELERY_RESULT_BACKEND = REDIS_URL
    
    # AI
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
