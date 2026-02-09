from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/admin",
    tags=["Admin endpoints"]
)

@router.post(
    "/access",
)
async def auth():
    return {"ok": True}


