from fastapi import FastAPI
from controllers.item import item


app = FastAPI()
app.include_router(item, tags=['item'])