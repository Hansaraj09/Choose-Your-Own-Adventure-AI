from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from routers import story, job
from db.database import create_tables

create_tables()

app = FastAPI(
    title = "Choose Your Own Adventure Game API",
    description="api to generate cool stories",
    versions="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
# so that both frontend and backend at different ports can talk with each other
app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.ALLOWED_ORIGINS,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story.router,prefix=settings.API_PREFIX)
app.include_router(job.router,prefix=settings.API_PREFIX)

# run the backend at port 8000 and make api available from everywhere
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)
