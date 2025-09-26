from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services import fund_service

router = APIRouter()

@router.get("/allocation/{recipient}")
def get_allocation(recipient: str):
    result = fund_service.get_allocation_service(recipient)
    return JSONResponse(content=result)

@router.post("/allocate/{recipient}/{amount}")
def allocate_funds(recipient: str, amount: int):
    result = fund_service.allocate_funds_service(recipient, amount)
    return JSONResponse(content=result)

@router.post("/mark-complete/{recipient}")
def mark_complete(recipient: str):
    result = fund_service.mark_complete_service(recipient)
    return JSONResponse(content=result)

@router.post("/release/{recipient}")
def release_funds(recipient: str):
    result = fund_service.release_funds_service(recipient)
    return JSONResponse(content=result)
