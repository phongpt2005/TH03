from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = {
    "admin": "admin"
}

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: User):
    if user.username in users and users[user.username] == user.password:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid username or password")

@app.get("/students")
def get_students():
    students = [
        {"id": 1, "msv": "D23CQC01", "name": "Nguyễn Văn A", "class_name": "D23CQC01-B", "phone": "0353608535", "dob": "29/03/2005", "birth_place": "Hà Nội", "achievement": "Tốt"}
    ]
    return students

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
