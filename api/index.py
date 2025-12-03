import sys
from pathlib import Path

# Ensure project root is on path for Vercel handler resolution
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.app import app  # noqa: E402

__all__ = ["app"]
