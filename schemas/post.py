from pydantic import BaseModel


class PostBase(BaseModel):
    """ベース
    """

    content: str


class PostCreate(PostBase):
    """リクエストパラメータ
    """

    pass


class Post(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
