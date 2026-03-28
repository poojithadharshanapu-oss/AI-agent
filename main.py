from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Agent is running 🚀"}

@app.get("/ask")
def ask_ai(q: str):
    return {"response": f"You asked: {q}"}
