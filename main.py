from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import Base, engine
from app.routes.auth_route import router as auth_router
from app.routes.motivation_route import router as motivation_router

app = FastAPI(title="Nostressia API")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello World from FastAPI on Vercel!"}


@app.get("/api/health")
def health_check():
    return {"status": "healthy"}


@app.get("/api/db-health")
def db_health_check():
    try:
        with engine.connect() as connection:
            current_db = connection.execute(text("SELECT DATABASE()")).scalar()
        return {"status": "connected", "database": current_db}
    except SQLAlchemyError as exc:
        return {"status": "error", "detail": str(exc)}


app.include_router(auth_router, prefix="/api")
app.include_router(motivation_router, prefix="/api")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
