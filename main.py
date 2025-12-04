from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.routes.auth_route import router as auth_router
from app.routes.motivation_route import router as motivation_router
from app.routes.tips_route import router as tips_router

app = FastAPI(title="Nostressia API")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api")
app.include_router(motivation_router, prefix="/api")
app.include_router(tips_router, prefix="/api")
