import openai
import os
from pathlib import Path

from pathlib import Path

prompts = Path(__file__).resolve().parent.parent / "prompts"



def read_manager():

    manager_file = prompts / "Manager.txt"
    try:
        return manager_file.read_text(encoding="utf-8")

    except Exception as e:
        print(f"Error reading Manager.txt: {e}")
        return ""
def call_agent(text:str):

    client = openai.OpenAI(
        base_url="http://localhost:8000/v1",
        api_key="sk-no-key-required"
    )
    response = client.chat.completions.create(
        model="local-model",
        messages=[{"role": "user", "content": text}]
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    text = read_manager()
    call_agent(text)