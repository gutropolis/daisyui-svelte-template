import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Query:
    hello: str = "world"

schema = strawberry.Schema(query=Query)

app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")