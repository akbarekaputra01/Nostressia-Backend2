# FastAPI on Vercel

This repo contains a FastAPI setup tailored for the Vercel Python runtime, following the official [Vercel guide for FastAPI](https://vercel.com/docs/frameworks/backend/fastapi) and the [FastAPI documentation](https://fastapi.tiangolo.com/).

## Local development

1. Use Python 3.12 to match the Vercel runtime.
2. Create and activate a virtual environment (recommended by the FastAPI docs):
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the FastAPI server locally (default port 3000 mirrors the Vercel runtime):
   ```bash
   uvicorn api.index:app --reload --host 0.0.0.0 --port 3000
   ```
5. Open the interactive docs served by FastAPI:
   - Swagger UI: http://localhost:3000/docs
   - ReDoc: http://localhost:3000/redoc

## Deployment on Vercel

- `vercel.json` configures the Python runtime (`python3.12`) for functions inside `api/` and rewrites all incoming requests to the FastAPI app.
- Vercel automatically installs dependencies from `requirements.txt` during deployment.
- `handler = Mangum(app)` adapts FastAPI to Vercel's serverless environment, as in the Vercel guide.

## Routes

- `GET /` returns a welcome message (`Message` schema).
- `GET /health` returns a simple health check payload (`HealthStatus` schema).
