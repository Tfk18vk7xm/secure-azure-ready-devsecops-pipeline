
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="SecureRelease API",
    description="A sample application for our DevSecOps release pipeline",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "application": "SecureRelease API",
        "version": "1.0.0",
        "message": "Welcome to SecureRelease!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "UP",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
