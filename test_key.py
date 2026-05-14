import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key (erste 20 Zeichen): {api_key[:20]}")
print(f"Länge: {len(api_key)}")

try:
    client = OpenAI(api_key=api_key)
    models = client.models.list()
    print("✓ Key ist gültig!")
except Exception as e:
    print(f"✗ Fehler: {e}")
