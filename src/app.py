from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.database import Base, engine
from src.routes.auth import router as auth_router
from src.routes.motivation import router as motivation_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nostressia API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
def read_root():
    return {"status": "ok"}


app.include_router(auth_router, prefix="/api")
app.include_router(motivation_router, prefix="/api")
