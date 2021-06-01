import boto3

from config.settings import settings

UserPoolId = settings.amazon_cognito_user_pool_id
ClientId = settings.amazon_cognito_client_id
# ClientSecret = settings.amazon_cognito_client_secret

session_args = {
    "region_name": settings.amazon_cognito_region
}

session = boto3.session.Session(**session_args)

client = session.client("cognito-idp")


def admin_create_user(username: str):
    """Amazon Cognitoの管理者ユーザーがユーザを作成する
    :param username:
    :return:
    """
    response = client.admin_create_user(
        UserPoolId=UserPoolId,
        Username=username,
        MessageAction="SUPPRESS",
    )

    return response


def admin_initiate_auth(username: str, password: str):
    # クライアントシークレットを発行する場合
    #
    # message = bytes(username + ClientId, 'utf-8')
    # key = bytes(ClientSecret, 'utf-8')
    #
    # secret_hash = base64.b64encode(
    #     hmac.new(key, message, digestmod=hashlib.sha256).digest()
    # ).decode()

    response = client.admin_initiate_auth(
        UserPoolId=UserPoolId,
        ClientId=ClientId,
        AuthFlow="ADMIN_USER_PASSWORD_AUTH",
        AuthParameters={
            "USERNAME": username,
            "PASSWORD": password,
            # 'SECRET_HASH': secret_hash
        },
    )

    return response


def admin_set_user_password(username: str, password: str):
    """Amazon Cognitoの管理者ユーザーがパスワードの変更を行う
    :param username:
    :param password:
    :return:
    """

    response = client.admin_set_user_password(
        UserPoolId=UserPoolId,
        Username=username,
        Password=password,
        Permanent=True,
    )

    return response

