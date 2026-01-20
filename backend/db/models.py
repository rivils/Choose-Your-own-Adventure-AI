from sqlalchemy import Column, Integer, String, DateTime
import datetime
from .database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"
    __table_args__ = {"extend_existing": True}  # fixes reload issues

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, unique=True, index=True)
    session_id = Column(String)
    theme = Column(String)
    status = Column(String, default="pending")
    story_id = Column(Integer, nullable=True)
    error = Column(String, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
