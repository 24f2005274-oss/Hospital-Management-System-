import os
import json
from openai import OpenAI

class MedicalScribeService:
    def __init__(self):
        # Initialize OpenAI Client (expects OPENAI_API_KEY in env)
        api_key = os.environ.get('OPENAI_API_KEY')
        self.client = OpenAI(api_key=api_key) if api_key else None

    def process_audio_to_soap(self, audio_file_path):
        """
        Takes an audio file, transcribes it via Whisper, 
        and structures it into a SOAP note via GPT-4o-mini.
        """
        if not self.client:
            raise ValueError("OpenAI API key not configured.")

        # 1. Transcribe Audio (Whisper)
        with open(audio_file_path, "rb") as audio_file:
            transcript = self.client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
        
        raw_text = transcript.text

        # 2. Structure into SOAP format (GPT)
        return self.generate_soap_note_from_text(raw_text)

    def generate_soap_note_from_text(self, raw_transcript):
        """
        Generates a structured SOAP note from a raw text transcript.
        """
        if not self.client:
            return {"error": "OpenAI API key not configured. Mocking response.", "raw": raw_transcript}

        prompt = f"""
        You are an expert AI Medical Scribe.
        Convert the following doctor-patient conversation transcript into a structured SOAP note.
        Provide the output strictly as a JSON object with the following keys:
        - subjective
        - objective
        - assessment
        - plan
        - suggested_icd10_codes (an array of strings)

        Transcript:
        {raw_transcript}
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful medical scribe."},
                {"role": "user", "content": prompt}
            ]
        )

        return json.loads(response.choices[0].message.content)
