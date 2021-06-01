from typing import List

from pydantic import BaseModel

from schemas.post import Post


class UserBase(BaseModel):
    """ベース
    """

    username: str
    name: str


class UserCreate(UserBase):
    """リクエストパラメータ
    """

    password: str


class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        orm_mode = True
