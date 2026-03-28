from fastapi import FastAPI, Request

app = FastAPI()

# Home route
@app.api_route("/", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"])
async def root(request: Request):
    return {
        "ok": True,
        "status": "success",
        "message": "root handled",
        "method": request.method
    }

# Catch ALL routes and ALL methods
@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"])
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
