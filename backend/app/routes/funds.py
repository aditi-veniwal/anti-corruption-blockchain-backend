from fastapi import APIRouter
from app.services import fund_service

router = APIRouter()

@router.get("/allocation/{recipient}")
def get_allocation(recipient: str):
    return {"recipient": recipient, "allocation": fund_service.get_allocation(recipient)}

@router.post("/allocate/{recipient}/{amount}")
def allocate_funds(recipient: str, amount: int):
    return fund_service.allocate_funds(recipient, amount)

@router.post("/mark-complete/{recipient}")
def mark_complete(recipient: str):
    return fund_service.mark_project_complete(recipient)

@router.post("/release/{recipient}")
def release_funds(recipient: str):
    return fund_service.release_funds(recipient)
