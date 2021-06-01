from sqlalchemy.orm import Session

import models
import schemas.user as schemas
from config.database import session


def find_user(user_id: int):
    return models.User.query.filter(models.User.id == user_id).first()


def find_user_by_username(username: str):
    return models.User.query.filter(models.User.username == username).first()


def get_users(skip: int = 0, limit: int = 100):
    return models.User.query.offset(skip).limit(limit).all()


def create_user(user: schemas.UserCreate):
    db_user = models.User(username=user.username, name=user.name)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user
