from fastapi import FastAPI, Request
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "running"}

# Support both possible reset paths
@app.post("/reset")
@app.post("/openenv/reset")
async def reset(request: Request):
    return {"status": "success", "message": "reset ok"}

# Support both possible validate paths
@app.post("/validate")
@app.post("/openenv/validate")
async def validate(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = {}
    return {"status": "success", "message": "validate ok", "received": data}
