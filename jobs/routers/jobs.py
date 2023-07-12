from fastapi import Depends, APIRouter
from sqlalchemy.orm import session
from schemes import jobs as schemes
from models import jobs as models
from dependencies import get_db


router = APIRouter()


# a POST endpoint for creating a job
@router.post('/jobs/', response_model=schemes.Job)
def create_job(job: schemes.Job, db: session = Depends(get_db)):
    
    job = models.Job(item=job.item, count=job.count)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job
