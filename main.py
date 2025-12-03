# main.py
import os

import mysql.connector
from fastapi import FastAPI
from mysql.connector import Error

app = FastAPI()


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
    """Verify that the application can connect to the configured database."""

    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT DATABASE()")
                current_db = cursor.fetchone()[0]
        return {"status": "connected", "database": current_db}
    except Error as exc:
        # Returning the error message helps debugging without exposing stack traces
        return {"status": "error", "detail": str(exc)}


# This is important for Vercel
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
