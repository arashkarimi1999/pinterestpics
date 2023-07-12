import strawberry
from typing import List
from databases import collection


@strawberry.type
class Item:
    tag: str
    link: str


@strawberry.type
class Query:

    @strawberry.field
    def item(self, filter: str, first: int) -> List[Item]:
        # Fetch items from MongoDB based on the provided filter and limit
        query = {"tag": filter}
        items = collection.find(query).limit(first)

        # Convert MongoDB documents into Item instances
        return [Item(link=item["link"], tag=item["tag"]) for item in items]
