from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class StoryJobBase(BaseModel):
    theme: str


class StoryJobResponse(BaseModel):
<<<<<<< HEAD
    job_id: int
=======
    job_id: str
>>>>>>> c2249ef (Initial commit)
    status: str
    created_at: datetime
    story_id: Optional[int] = None
    completed_at: Optional[datetime] = None
    error: Optional[str] = None

    class Config:
        from_attributes = True


class StoryJobCreate(StoryJobBase):
    pass