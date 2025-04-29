from fastapi import FastAPI
from app.config.database import database

app = FastAPI(title="Evenement Service")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def read_root():
    return {"message": "Evenement Service API is running"}
