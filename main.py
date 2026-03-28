from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

# Initialize FastAPI app
app = FastAPI()

# Set your Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Request body format
class RequestModel(BaseModel):
    query: str

# Root route
@app.get("/")
def home():
    return {"message": "AI Agent is running 🚀"}

# AI Agent endpoint
@app.post("/ask")
def ask_ai(request: RequestModel):
    response = model.generate_content(request.query)
    return {"response": response.text}
