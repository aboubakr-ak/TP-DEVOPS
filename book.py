from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, get_db
from sqlalchemy import Column, Integer, String, ForeignKey
import schemas, models


route = APIRouter()




# Add new book
@route.post("/books")
def add_book(request: schemas.book, db: Session = Depends(get_db)):
    
    new_book = models.book (
                           id = request.id,
                           title = request.title,
                           author =  request.author,
                           description = request.description,
                           published_year = request.published_year,
                           publisher = request.publisher
                        )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

# Retrieve a list of all books
@route.get("/books", response_model=list[schemas.book])
def get_books(db: Session = Depends(get_db)):
    return db.query(models.book).all()

# Retrieve details for a specific book
@route.get("/books/{book_id}", response_model=schemas.book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.book).filter(models.book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book



# Update an existing book:

# delete an existing book: