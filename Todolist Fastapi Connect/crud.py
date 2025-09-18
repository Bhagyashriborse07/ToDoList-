
from sqlalchemy.orm import Session
from models import ToDoItem
from schemas import ToDoCreate

def get_todos(db: Session):
    return db.query(ToDoItem).all()

def get_todo(db: Session, todo_id: int):
    return db.query(ToDoItem).filter(ToDoItem.id == todo_id).first()

def create_todo(db: Session, todo: ToDoCreate):
    db_item = ToDoItem(**todo.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_todo(db: Session, todo_id: int):
    db_item = db.query(ToDoItem).filter(ToDoItem.id == todo_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
