from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid
from db.database import get_db
from db.models import StoryJob

router = APIRouter()

@router.post("/create")
def create_story(theme: str, db: Session = Depends(get_db)):
    job_id = str(uuid.uuid4())
    session_id = str(uuid.uuid4())

    job = StoryJob(
        job_id=job_id,
        session_id=session_id,
        theme=theme,
        status="pending"
    )

    db.add(job)
    db.commit()
    db.refresh(job)
    return {"job_id": job.job_id, "theme": job.theme, "status": job.status}
