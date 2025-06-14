from fastapi import FastAPI, HTTPException
from services.user_service import UserService
from infrastructure.db.uow import UnitOfWork

app = FastAPI()
user_service = UserService(UnitOfWork)


@app.post("/register")
def register(social_id: int, username: str):
    user = user_service.register_user(social_id, username)
    if user:
        return {"id": user.id, "username": user.username}
    raise HTTPException(status_code=400, detail="Registration failed")


@app.get("/top")
def top(limit: int = 10):
    users = user_service.get_top_users(limit)
    return [{"id": u.id, "username": u.username, "taps": u.taps} for u in users]
