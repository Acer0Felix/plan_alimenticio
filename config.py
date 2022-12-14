import os
from dotenv import load_dotenv

dotenv_file_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)
    
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Sol1DeoGlor1a@localhost:5432/sportapp_plan_nutricional"
    
class ProductionConfig(Config):
    pass
