from typing import List, Optional
from pydantic import BaseModel

class Author(BaseModel):
    id:int = None
    name:str
    bio: Optional[str] = None
    books:List[str] = []
