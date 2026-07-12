#Loads the environment variables from the .env file and sets them as attributes of the Config class., app-wide settings

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Car Price Prediction API"
    API_KEY = os.getenv("API_KEY",'demo-key')
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY",'secret')
    JWT_ALGORITHM = 'HS256'
    REDIS_URL = os.getenv("REDIS_URL",'redis://localhost:6379')
    MODEL_PATH = 'app/models/model.pkl'


settings = Settings()