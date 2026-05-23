from fastapi import APIRouter
from app.api.v1 import workflows, automation, ai_integration, sales

router = APIRouter()

# Include all API route modules
router.include_router(workflows.router, prefix="/api/v1/workflows", tags=["Workflows"])
router.include_router(automation.router, prefix="/api/v1/automation", tags=["Automation"])
router.include_router(ai_integration.router, prefix="/api/v1/ai", tags=["AI Integration"])
router.include_router(sales.router, prefix="/api/v1/sales", tags=["Sales"])
