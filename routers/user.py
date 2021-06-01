from fastapi import APIRouter, Depends

import cruds.post as post_crud
import schemas
from utils.authentication import get_current_user

router = APIRouter(
    prefix="/user",
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=schemas.User)
def read_user(current_user: schemas.User = Depends(get_current_user)):
    """認証済みのユーザーを取得する
    :param current_user: 認証済みのユーザー
    :return: User
    """

    return current_user


@router.post("/posts", response_model=schemas.Post)
def create_post(
    item: schemas.PostCreate, current_user: schemas.User = Depends(get_current_user)
):
    """認証済みのユーザーがPostを投稿する
    要認証
    :param item: Post
    :param current_user: 認証済みのユーザー
    :return: Post
    """

    post = post_crud.create_post(current_user.id, item)
    return post
