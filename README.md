# Nostressia Backend (FastAPI)

Implementasi FastAPI untuk Nostressia yang selaras dengan repository asli, tetapi sudah dikonfigurasi agar dapat dideploy di Vercel.

## Fitur
- Endpoint login admin dengan JWT bearer token.
- CRUD sederhana untuk motivation quotes (create, list, delete).
- CORS terbuka untuk memudahkan integrasi front-end.
- Koneksi MySQL menggunakan SQLAlchemy.

## Struktur penting
- `src/app.py` — instance FastAPI dan konfigurasi middleware/router.
- `src/routes/` — definisi endpoint (`auth.py`, `motivation.py`).
- `src/models/` — model SQLAlchemy (`Admin`, `Motivation`).
- `src/core/` — konfigurasi & koneksi database.
- `api/index.py` — handler yang dipanggil Vercel Functions.
- `vercel.json` — konfigurasi runtime `vercel-python` dan routing.

## Menjalankan lokal
1. Buat environment: `python -m venv .venv && source .venv/bin/activate`.
2. Salin `.env.example` menjadi `.env` dan sesuaikan kredensial database serta `SECRET_KEY`.
3. Install dependensi: `pip install -r requirements.txt`.
4. Jalankan server: `uvicorn src.app:app --reload`.

## Deployment ke Vercel
1. Pastikan sudah login ke Vercel CLI (`npm i -g vercel` lalu `vercel login`).
2. Pastikan `vercel.json` ada di root (sudah disertakan). Vercel akan menggunakan `api/index.py` sebagai entrypoint FastAPI.
3. Set environment variables di Project Settings Vercel (`DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`, `SECRET_KEY`, `ACCESS_TOKEN_EXPIRE_MINUTES`).
4. Deploy: `vercel deploy`.

Referensi dokumen: [FastAPI on Vercel](https://vercel.com/docs/frameworks/backend/fastapi).
