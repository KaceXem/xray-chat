import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

VERTEX_PROJECT = os.getenv("GCP_PROJECT_ID", "")
VERTEX_LOCATION = "australia-southeast1"

# Modèle mis à jour suite au test réussi
MODEL_NAME = "gemini-3.6-flash"