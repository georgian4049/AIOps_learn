from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import OpenAI
import os

api_key = os.environ.get("GOOGLE_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    
)

app = FastAPI()

@app.get("/api")
def idea():
    try:
        messages = [{"role": "user", "content": "Reply with a new business idea for AI Agents, formatted with headings, sub-headings and bullet points"}]
        stream = client.chat.completions.create(
                        model="gemini-2.5-flash",
                        messages=messages 
                    )
        def event_stream():
            for chunk in stream:
                text = chunk.choices[0].delta.content
                if text:
                    lines = text.split("\n")
                    for line in lines:
                        yield f"data: {line}\n"
                    yield "\n"

        return StreamingResponse(event_stream(), media_type="text/event-stream")
    except Exception as e:
        print("exception", str(e))
        return str(e)