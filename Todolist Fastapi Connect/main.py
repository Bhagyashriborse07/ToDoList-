# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import SessionLocal, engine
# import models, schemas, crud
# from models import Base,ToDoItem  

# Base.metadata.create_all(bind=engine)

# app = FastAPI()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/todos/", response_model=list[schemas.ToDo])
# def read_todos(db: Session = Depends(get_db)):
#     return crud.get_todos(db)

# @app.get("/todos/{todo_id}", response_model=schemas.ToDo)
# def read_todo(todo_id: int, db: Session = Depends(get_db)):
#     db_item = crud.get_todo(db, todo_id)
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     return db_item

# @app.post("/todos/", response_model=schemas.ToDo)
# def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
#     return crud.create_todo(db, todo)

# @app.delete("/todos/{todo_id}", response_model=schemas.ToDo)
# def delete_todo(todo_id: int, db: Session = Depends(get_db)):
#     db_item = crud.delete_todo(db, todo_id)
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     return db_item


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud
from models import Base, ToDoItem  # important: import model

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos/", response_model=list[schemas.ToDo])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@app.get("/todos/{todo_id}", response_model=schemas.ToDo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_todo(db, todo_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_item

@app.post("/todos/", response_model=schemas.ToDo)
def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

@app.delete("/todos/{todo_id}", response_model=schemas.ToDo)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_todo(db, todo_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_item
