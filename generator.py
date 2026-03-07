import json
import os
from pathlib import Path

from dotenv import load_dotenv
from jinja2 import Template
from openai import OpenAI


# Projekt-Root
ROOT = Path(__file__).parent


# Profil laden
def load_profile():
    profile_path = ROOT / "data" / "profile.json"
    return json.loads(profile_path.read_text(encoding="utf-8"))


# Prompt-Datei laden
def load_prompt():
    prompt_path = ROOT / "prompts" / "de_motivation.txt"
    return prompt_path.read_text(encoding="utf-8")


# AI Motivationsschreiben generieren
def generate_letter(job_title, job_description, file_content=None):

    # .env laden
    load_dotenv()

    # OpenAI API Key aus .env holen
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY wurde nicht gefunden. Bitte .env prüfen.")

    # OpenAI Client starten
    client = OpenAI(api_key=api_key)

    # Profil laden
    profile = load_profile()

    # Prompt Template laden
    prompt_template = Template(load_prompt())

    # Prompt mit Daten füllen
    prompt = prompt_template.render(
        job_title=job_title,
        job_description=job_description,
        profile_json=json.dumps(profile, indent=2, ensure_ascii=False),
    )

    # OpenAI Anfrage
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text