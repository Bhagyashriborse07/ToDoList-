
# from pydantic import BaseModel

# class ToDoBase(BaseModel):
#     title: str
#     description: str
#     completed: bool = False

# class ToDoCreate(ToDoBase):
#     pass

# class ToDo(ToDoBase):
#     id: int

#     class Config:
#         orm_mode = True 
from pydantic import BaseModel

class ToDoCreate(BaseModel):
    title: str
    description: str

class ToDo(ToDoCreate):
    id: int
    completed: bool

    class Config:
        orm_mode = True
