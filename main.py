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



def get_db_connection():
    """Create a MySQL connection using environment variables.

    Falls back to provided default credentials when environment variables
    are not set so the API can connect in local development or Vercel.
    """

    return mysql.connector.connect(
        user=os.getenv("DB_USER", "Nostressia_nationalas"),
        password=os.getenv(
            "DB_PASSWORD", "2f5d922599f787ad53a4a1c7a243e24be84a5be7"
        ),
        host=os.getenv("DB_HOST", "mfv81z.h.filess.io"),
        port=os.getenv("DB_PORT", "3306"),
        database=os.getenv("DB_NAME", "Nostressia_nationalas"),
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
