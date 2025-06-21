# app/main.py
import uvicorn
from fastapi import FastAPI
from sqlmodel import SQLModel
from fastapi.middleware.cors import CORSMiddleware

from app.api import user
from app.db.session import engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("⏳ Create tablas...")
    SQLModel.metadata.create_all(bind=engine)
    yield
    print("🛑 Close application...")

app = FastAPI(title="Mi API Backend", version="1.0.0", lifespan=lifespan )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api", tags=["Users"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

