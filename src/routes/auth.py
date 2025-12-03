from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.admin import Admin
from src.schemas.auth import AdminResponse, LoginRequest, LoginResponse
from src.utils.security import create_access_token, verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/admin/login", response_model=LoginResponse)
def admin_login(request: LoginRequest, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.username == request.username).first()

    if not admin or not verify_password(request.password, admin.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username atau password salah",
        )

    token = create_access_token({"sub": admin.username, "role": "admin"})

    return LoginResponse(
        access_token=token,
        admin=AdminResponse(
            id=admin.admin_id,
            name=admin.name,
            username=admin.username,
            email=admin.email,
        ),
    )
