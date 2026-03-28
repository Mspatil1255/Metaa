from fastapi import FastAPI, Request

app = FastAPI()

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
async def catch_all(full_path: str, request: Request):
    try:
        data = await request.json()
    except Exception:
        data = None

    return {
        "ok": True,
        "status": "success",
        "message": "request handled",
        "path": "/" + full_path,
        "method": request.method,
        "received": data
    }
