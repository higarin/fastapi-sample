FastAPI Sample
----

FastAPI, SQLAlchemy, Alembic, Graphene, Amazon Cognito

## Install Dependencies

Install the poetry package manager

* https://github.com/python-poetry/poetry

Install the project dependencies:

```shell
$ poetry install
```

## Local Development

Configure environment variable

```sh
$ cp .env.template .env
$ vi .env
```

Enter a poetry shell

```shell
$ poetry shell
```

Migration

```shell
$ alembic upgrade head
```

Run the live server

```shell
$ uvicorn main:app --reload
```

## Build app's container image

```sh
$ docker build -t <tag> .
```

## Docs
* FastAPI
    * https://fastapi.tiangolo.com/ja/tutorial/
* pydantic
    * https://fastapi.tiangolo.com/ja/tutorial/schema-extra-example/
    * https://fastapi.tiangolo.com/ja/tutorial/sql-databases/#create-the-pydantic-models
    * https://pydantic-docs.helpmanual.io/
* SQLAlchemy
    * https://fastapi.tiangolo.com/ja/tutorial/sql-databases/
* Alembic
    * https://alembic.sqlalchemy.org/en/latest/
* GraphQL (Graphene)
    * https://github.com/graphql-python/graphene-sqlalchemy
* Amazon Cognito
    * https://docs.aws.amazon.com/ja_jp/cognito/latest/developerguide/cognito-user-identity-pools.html
    * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html
