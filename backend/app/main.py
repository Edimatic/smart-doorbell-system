from fastapi import FastAPI
from .api.api import api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Doorbell System API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

