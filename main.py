from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI API",
    version="1.0.0",
    description="API de Exemplo com FastAPI"
)

@app.get("/")
async def home():
    return "Hello, FastAPI!"
