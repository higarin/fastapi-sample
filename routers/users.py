from typing import List

from fastapi import APIRouter, HTTPException

import cruds.post as post_crud
import cruds.user as user_crud
import schemas

router = APIRouter(
    prefix="/users",
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 100,
):
    """ユーザー一覧を取得する
    :param skip:
    :param limit:
    :return:
    """

    users = user_crud.get_users(skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int):
    user = user_crud.find_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.get("/{user_id}/posts", response_model=List[schemas.Post])
def read_users_post(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
):
    """ユーザーの投稿一覧を取得する
    :param user_id:
    :param skip:
    :param limit:
    :return:
    """

    user = user_crud.find_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user.posts


@router.post("/{user_id}/posts", response_model=schemas.Post)
def create_users_post(user_id: int, item: schemas.PostCreate):
    """ユーザーの投稿を (勝手に) ポストする
    :param user_id:
    :param item:
    :return:
    """

    user = user_crud.find_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    post = post_crud.create_post(user.id, item)
    return post
