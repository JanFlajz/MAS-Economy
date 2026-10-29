import openai
import os
from pathlib import Path

from pathlib import Path

prompts = Path(__file__).resolve().parent.parent / "prompts"



class CAgent:
    """
    This class serves as defining a single Agent who can:
        1. Call API
        2. Use Tools
    """
    def __init__(self,file_name:str = "Manager.txt"):
        def read_prompt():
            manager_file = prompts / file_name
            try:
                return manager_file.read_text(encoding="utf-8")

            except Exception as e:
                print(f"Error reading Manager.txt: {e}")
                return ""
        self.prompt = read_prompt()


    def call_api(self):
        try:
            text = self.prompt if self.prompt else ""
            client = openai.OpenAI(
                base_url="http://localhost:8000/v1",
                api_key="sk-no-key-required"
            )
            response = client.chat.completions.create(
                model="local-model",
                messages=[{"role": "user", "content": text}]
            )
            print(response.choices[0].message.content)
        except Exception as e:
            print(str(e))