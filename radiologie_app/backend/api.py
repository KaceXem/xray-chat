import base64
import gc
import os
from google import genai
from google.oauth2 import service_account

class MedicalApi:
    def __init__(self):
        # Localisation STRICTEMENT codée en dur à Sydney (souveraineté des données australiennes)
        self.location = "australia-southeast1"
        self.credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "service_account.json")
        self.project_id = os.getenv("GCP_PROJECT_ID", "")

    def _get_vertex_client(self):
        # Chargement sécurisé des identifiants du Service Account
        if os.path.exists(self.credentials_path):
            creds = service_account.Credentials.from_service_account_file(self.credentials_path)
            return genai.Client(
                vertexai=True,
                project=self.project_id or creds.project_id,
                location=self.location,
                credentials=creds
            )
        else:
            # Fallback direct si la variable d'environnement système est utilisée
            return genai.Client(
                vertexai=True,
                project=self.project_id,
                location=self.location
            )

    def process_document(self, base64_data: str, mime_type: str, prompt: str) -> str:
        file_bytes = None
        client = None
        try:
            # 1. Décodage exclusif en mémoire vive RAM (ZÉRO écriture disque local)
            file_bytes = base64.b64decode(base64_data)

            # 2. Client Vertex AI pointé sur Sydney
            client = self._get_vertex_client()

            # 3. Payload binaire
            document = {
                "inline_data": {
                    "mime_type": mime_type,
                    "data": file_bytes
                }
            }

            # 4. Génération via Gemini avec le prompt personnalisé du praticien
            response = client.models.generate_content(
                model='gemini-2.5-flash', # ou gemini-1.5-pro selon la licence GCP du client
                contents=[document, prompt]
            )

            return response.text

        except Exception as e:
            return f"[ERREUR VERTEX AI SYDNEY] : {str(e)}"

        finally:
            # Destruction immédiate des données médicales en RAM
            if file_bytes is not None:
                del file_bytes
            if client is not None:
                del client
            gc.collect()