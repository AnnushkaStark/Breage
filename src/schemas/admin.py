from pydantic import BaseModel


class AdminBase(BaseModel):
    email: str
    password: str
