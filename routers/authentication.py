from fastapi import APIRouter

import schemas
import services
from utils import cognito

router = APIRouter(
    prefix="/authentication",
    responses={404: {"description": "Not found"}},
)


@router.post("/sign_up")
async def sign_up(user: schemas.UserCreate):
    """サインアップ
    :param user:
    :return:
    """

    response = services.create_user(user)
    return response


@router.post("/sign_in")
async def sign_in(username: str, password: str):
    """サインイン
    :param username:
    :param password:
    :return:
    """

    response = cognito.admin_initiate_auth(username, password)
    return response
