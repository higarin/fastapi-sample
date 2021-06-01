import schemas
from cruds import user as user_crud
from utils import cognito


def create_user(user: schemas.UserCreate):
    """ユーザーの作成
    Amazon Cognitoのユーザーを作成し、DBに格納する
    FIXME: 失敗時の事は考慮していない
    :param user:
    :return:
    """
    username = user.username
    password = user.password

    # ユーザーを作成
    cognito.admin_create_user(username)
    # パスワードの設定
    cognito.admin_set_user_password(username, password)

    # Userの作成
    db_user = user_crud.create_user(user)

    return db_user
