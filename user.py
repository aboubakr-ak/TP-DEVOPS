from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, get_db
from sqlalchemy import Column, Integer, String, ForeignKey
import schemas, models


route = APIRouter()


# Add new user
@route.post("/users", response_model=schemas.User)
def add_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name,
                           birthday=request.birthday,
                           gender=request.gender,
                           email=request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Retrieve a list of all users:

# Retrieve details for a specific user:

# Update an existing user:

# delete an existing user:
