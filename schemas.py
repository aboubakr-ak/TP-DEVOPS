from typing import List, Optional
from pydantic import BaseModel


class book (BaseModel):
    id: int
    title : str
    author : str
    description : str
    published_year : int
    publisher : str

    class Config():
        orm_mode = True 


class User(BaseModel):
    id: int
    name : str
    birthday : str
    gender : str
    email : str

    class Config():
        orm_mode = True 