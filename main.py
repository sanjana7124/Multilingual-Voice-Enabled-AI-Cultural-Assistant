import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI(title="LinguaVoice AI Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins for local testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str          # user text (any language)
    input_language: str   # e.g. "auto", "hi", "kn"
    target_language: str  # e.g. "hi", "en", "ta"

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        system_prompt = (
            "You are LinguaVoice AI, an accessibility-focused assistant for India. "
            "User may speak/type in any language (possibly mixed).\n"
            f"- Detect the language of the user message (hint: user_input_language={req.input_language}).\n"
            f"- Answer ONLY in the target language: {req.target_language}.\n"
            "- If needed, first translate the user's question into the target language in your mind, "
            "then respond clearly and politely.\n"
            "- Keep answers concise, suitable to be read aloud."
        )

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": req.message},
            ],
            temperature=0.7,
        )
        reply = completion.choices[0].message.content
        return {
            "response": reply,
            "target_language": req.target_language
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
