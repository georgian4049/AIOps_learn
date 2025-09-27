from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

import google.generativeai as genai
import os

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

app = FastAPI()

@app.get("/api", response_class = PlainTextResponse)
def idea():
    try:
        messages = [{"role": "user", "content": "Come up with a new business idea for AI agents. keep message short"}]
        response = model.generate_content("Come up with a new business idea for AI agents. keep message short")
        print(response.text)
        return response.text
    except Exception as e:
        print("exception", e)
        return e