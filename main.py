import uvicorn
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from gql.schema import schema
from routers import authentication, users, user

app = FastAPI()

app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(user.router)

app.add_route("/gql", GraphQLApp(schema=schema))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
