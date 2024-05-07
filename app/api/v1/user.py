from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
async def read_items():
    return [{"user_name" : "Pierre"}, {"user_name" : "Jaque"}]

@router.get("/user_all")
async def get_all():
    return[{"hello" : "fadwa"}, {"good" : "girl"}]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"hello": item.name, "good": item_id}