from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
async def read_items():
    return [{"user_name" : "Pierre"}, {"user_name" : "Jaque"}]

@router.get("/user_all")
async def get_all():
    return[{"hello" : "fadwa"}, {"good" : "girl"}]

