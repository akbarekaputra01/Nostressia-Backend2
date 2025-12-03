from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum


class Message(BaseModel):
    message: str


class HealthStatus(BaseModel):
    status: str


app = FastAPI(
    title="FastAPI on Vercel",
    description="Minimal FastAPI app adapted for Vercel Serverless Functions.",
    version="0.1.0",
)


@app.get("/", response_model=Message, summary="Root greeting")
async def read_root() -> Message:
    """Return a welcome message and confirm the app is running."""

    return Message(message="Hello from FastAPI on Vercel")


@app.get("/health", response_model=HealthStatus, summary="Health check")
async def health() -> HealthStatus:
    """Lightweight readiness check for monitoring and load balancers."""

    return HealthStatus(status="ok")


handler = Mangum(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api.index:app", host="0.0.0.0", port=3000, reload=True)
