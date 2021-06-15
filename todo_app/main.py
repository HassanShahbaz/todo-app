from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI(
    title="ToDo App",
    description="CRUD API for ToDo app.",
    version="1.0.0",
)

# Create tables in database defined in models.py
models.Base.metadata.create_all(engine)

# Create session/connection for local db and return it to use
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 


@app.post('/create-todo', status_code=status.HTTP_201_CREATED)
def create_todo(request: schemas.ToDo, db: Session = Depends(get_db)):
    new_todo = models.ToDo(title=request.title, description=request.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.put('/update-todo/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_todo(id, request: schemas.ToDo, db: Session = Depends(get_db)):
    todo = db.query(models.ToDo).filter(models.ToDo.id == id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Todo with id {id} does not exist')
    todo.update(request.dict())
    db.commit()
    return {'detail': 'Updated successfully'}

@app.delete('/delete-todo/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id, db: Session = Depends(get_db)):
    todo = db.query(models.ToDo).filter(models.ToDo.id == id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Todo with id {id} does not exist')
    todo.delete()
    db.commit()
    return {'detail': 'Todo has been deleted'}


@app.get('/todos')
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(models.ToDo).all()
    if not todos:
        return {'detail': 'No todos found'}
    return todos
    