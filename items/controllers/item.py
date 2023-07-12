from fastapi import APIRouter
from type.item import Query
from strawberry.asgi import GraphQL
import strawberry


item = APIRouter()

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

item.add_route("/graphql", graphql_app)