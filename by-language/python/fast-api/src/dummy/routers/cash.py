from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/cash")


@router.get("/")
async def get_cash():
    """Retrieve cash amount."""
    return JSONResponse(content={"amount": "$100"})


@router.post("/", status_code=204)
async def post_cash():
    """Endpoint to handle posting cash."""
    return Response(status_code=204)
