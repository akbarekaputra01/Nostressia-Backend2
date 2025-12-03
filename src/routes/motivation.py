from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.motivation import Motivation
from src.schemas.motivation import MotivationCreate, MotivationResponse

router = APIRouter(prefix="/motivations", tags=["Motivations"])


@router.get("", response_model=List[MotivationResponse])
def list_motivations(db: Session = Depends(get_db)):
    return db.query(Motivation).all()


@router.post("", response_model=MotivationResponse, status_code=status.HTTP_201_CREATED)
def create_motivation(payload: MotivationCreate, db: Session = Depends(get_db)):
    motivation = Motivation(
        quote=payload.quote,
        uploader_id=payload.uploader_id,
        author_name=payload.author_name,
    )
    db.add(motivation)
    db.commit()
    db.refresh(motivation)
    return motivation


@router.delete("/{motivation_id}")
def delete_motivation(motivation_id: int, db: Session = Depends(get_db)):
    motivation = db.query(Motivation).filter(Motivation.motivation_id == motivation_id).first()

    if motivation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Motivation not found")

    db.delete(motivation)
    db.commit()

    return {"message": "Motivation deleted successfully"}
