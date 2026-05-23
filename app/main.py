from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from app.config import settings
from app.api import router

# Configure logging
logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Netty_Network AI Executive Operator starting...")
    yield
    logger.info("🛑 Netty_Network shutting down...")

app = FastAPI(
    title="Netty_Network AI Executive Operator",
    description="AI-powered automation architect for business scaling and execution",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)

@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - System Status"""
    return {
        "message": "Netty_Network AI Executive Operator Online",
        "status": "operational",
        "mission": "Execution creates reality"
    }

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "netty-network"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
