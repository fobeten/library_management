from fastapi import APIRouter

router = APIRouter(prefix="/book")

@router.get("/")
def home():
    return "book home"