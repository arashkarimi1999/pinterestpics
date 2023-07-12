from datetime import datetime
from fastapi import FastAPI
from routers import jobs
from time import time


app = FastAPI()
app.include_router(jobs.router, tags=['jobs'])