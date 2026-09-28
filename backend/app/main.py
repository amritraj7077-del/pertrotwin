import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logging import logger
from app.api.v1.router import api_router
from app.db.seed import seed_database
from app.db.connection import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting {settings.PROJECT_NAME} v{settings.VERSION} in {settings.ENVIRONMENT} mode...")
    # Initialize database tables
    try:
        await init_db()
        logger.info("Database tables initialized successfully.")
    except Exception as e:
        logger.error(f"Error during database initialization: {e}")
        # In production, don't fail startup if init fails
        if settings.ENVIRONMENT == "production":
            logger.warning("Database initialization failed in production, continuing anyway...")
        else:
            raise
    
    # Seed database only in development or if explicitly requested
    if settings.ENVIRONMENT == "development" or os.getenv("SEED_DATABASE") == "true":
        try:
            await seed_database()
        except Exception as e:
            logger.error(f"Error during database startup seed: {e}")
            if settings.ENVIRONMENT == "production":
                logger.warning("Database seeding failed in production, continuing anyway...")
            else:
                raise
    
    yield
    logger.info(f"Shutting down {settings.PROJECT_NAME}...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    lifespan=lifespan,
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS if settings.CORS_ORIGINS else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount central v1 router
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "docs": f"{settings.API_V1_STR}/docs",
        "api_v1": settings.API_V1_STR,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
