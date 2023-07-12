from pydantic import BaseModel


class Job(BaseModel):
    item: str
    count: int

    class Config:
        orm_mode = True
