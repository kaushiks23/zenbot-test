import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    api_key = os.environ.get("MY_SECRET_KEY", "NOT_SET")
    
    # Print to Railway logs (visible in dashboard)
    print(f"🔑 MY_SECRET_KEY value: {api_key}")  # Debug line
    
    return {
        "message": "Railway Secrets Test",
        "your_key": api_key,
        "environment": "production" if os.getenv("RAILWAY_ENVIRONMENT") else "development"
    }