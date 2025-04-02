import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    api_key = os.environ.get("MY_SECRET_KEY")
    return {"message": "Secret is working!", "your_key": api_key or "No key found"}