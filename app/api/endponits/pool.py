from fastapi import APIRouter
from app.services.pool_service import PoolService
from app.models.pool import SubmitPoolSchema

router = APIRouter()
poo_service = PoolService()

@router.post("/create-pool")
async def create_pool(pool: SubmitPoolSchema):
    