from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import Base, engine
from routers.story import router as stories_router

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Choose-Your-Own-Adventure AI", version="0.1.0")

# CORS (allow all origins for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(stories_router, prefix="/api/stories", tags=["stories"])

@app.get("/")
def root():
    return {"message": "API is running!"}
