from fastapi import FastAPI, Depends
from fastapi.responses import StreamingResponse
from openai import OpenAI
import os
from fastapi_clerk_auth import ClerkConfig, ClerkHTTPBearer, HTTPAuthorizationCredentials 

clerk_config = ClerkConfig(jwks_url=os.getenv("CLERK_JWKS_URL"))
clerk_guard = ClerkHTTPBearer(clerk_config)

api_key = os.environ.get("GOOGLE_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    
)

app = FastAPI()

@app.get("/api")
def idea(creds: HTTPAuthorizationCredentials = Depends(clerk_guard)):
    try:
        user_id = creds.decoded["sub"]
        messages = [{"role": "user", "content": "Reply with a new business idea for AI Agents, formatted with headings, sub-headings and bullet points"}]
        stream = client.chat.completions.create(
                        model="gemini-2.5-flash",
                        messages=messages ,
                        stream=True
                    )
        def event_stream():
            for chunk in stream:
                text = chunk.choices[0].delta.content
                if text:
                    lines = text.split("\n")
                    for line in lines:
                        yield f"data: {line}\n"
                        yield "data:  \n"
                    yield f"data: {lines[-1]}\n\n"

        return StreamingResponse(event_stream(), media_type="text/event-stream")
    except Exception as e:
        print("exception", str(e))
        return str(e)