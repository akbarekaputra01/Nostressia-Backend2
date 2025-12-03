from typing import Optional

from pydantic import BaseModel


class MotivationBase(BaseModel):
    quote: str
    uploader_id: Optional[int] = None
    author_name: Optional[str] = None


class MotivationCreate(MotivationBase):
    pass


class MotivationResponse(MotivationBase):
    motivation_id: int

    class Config:
        orm_mode = True
