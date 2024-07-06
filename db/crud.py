from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session,user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all() 

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()