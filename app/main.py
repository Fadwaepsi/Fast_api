from fastapi import FastAPI
from app.api.v1.user import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"status" : "ok"}

app.include_router(router)