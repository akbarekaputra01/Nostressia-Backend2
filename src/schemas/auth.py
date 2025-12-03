from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class AdminResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str

    class Config:
        orm_mode = True


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    admin: AdminResponse
