from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
KEY_TO_TEST = os.getenv("GEMINI_API_KEY")
print(KEY_TO_TEST)
try:
    client = genai.Client(api_key=KEY_TO_TEST)
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Réponds juste 'Connexion OK'."
    )
    print("Succès :", response.text)
except Exception as e:
    print("Échec du test :", e)