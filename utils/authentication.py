import json

import httpx
import jwt
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt.algorithms import RSAAlgorithm

from config.settings import settings
from cruds import user as user_crud

cognito_url = f"https://cognito-idp.{settings.amazon_cognito_region}.amazonaws.com/{settings.amazon_cognito_user_pool_id}"
cognito_jwk_url = f"{cognito_url}/.well-known/jwks.json"


def get_current_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    token = cred.credentials
    payload = verify_token(token)
    user = user_crud.find_user_by_username(payload["username"])

    return user


def verify_token(token):
    """JWT Tokenを検証しPayloadを返却する
    :param token: JWT Token
    :return: Payload
    """

    jwt_header = jwt.get_unverified_header(token)
    key_id = jwt_header["kid"]
    jwt_algorithms = jwt_header["alg"]

    # FIXME: 証明書はキャッシュできる
    with httpx.Client() as client:
        res_cognito = client.get(cognito_jwk_url)

    jwk = None
    for key in json.loads(res_cognito.text)["keys"]:
        if key["kid"] == key_id:
            jwk = key
    if not jwk:
        raise Exception("JWK Not Found")

    public_key = RSAAlgorithm.from_jwk(json.dumps(jwk))

    json_payload = jwt.decode(
        token,
        public_key,
        algorithms=[jwt_algorithms],
        verify=True,
        options={"require_exp": True, "verify_aud": False},
        audience=settings.amazon_cognito_client_id,
        issuer=cognito_url,
    )

    return json_payload
