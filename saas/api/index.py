from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from openai import OpenAI
import os

api_key = os.environ.get("GOOGLE_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    
)

app = FastAPI()

@app.get("/api", response_class = PlainTextResponse)
def idea():
    try:
        messages = [
                {
                    "role": "system", "content": "You are a helpful assistant",
                    "role": "user", "content": "Come up with a new business idea for AI agents. keep message short"
                }
            ]
        response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Explain to me how AI works"
            }
        ]
    )
        return response.choices[0].message.content
    except Exception as e:
        print("exception", str(e))
        return str(e)