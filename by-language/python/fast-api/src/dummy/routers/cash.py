from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/cash")


@router.get("/")
async def get_cash():
    return JSONResponse(content={"amount": "$100"})


@router.post("/", status_code=204)
async def post_cash():
    return Response(status_code=204)
