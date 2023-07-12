from databases import Base
from sqlalchemy import Column, String, Integer


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    item = Column(String)
    count = Column(Integer)
