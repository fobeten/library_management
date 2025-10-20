from pydantic import BaseModel
from fastapi import HTTPException

class Book(BaseModel):
    id:int = None
    title: str
    year: int
    author: str
