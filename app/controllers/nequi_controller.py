from fastapi import APIRouter, Depends
from app.services import nequi_service

router = APIRouter()

@router.post("/nequi/app/token")
def get_app_token(service: nequi_service.NequiService = Depends()):
    return service.get_app_token()

@router.post("/nequi/user/token")
def get_user_token(service: nequi_service.NequiService = Depends()):
    return service.get_user_token()

@router.get("/nequi/user/info")
def get_user_info(service: nequi_service.NequiService = Depends()):
    return service.get_user_info()

@router.post("/nequi/payment")
def payment(service: nequi_service.NequiService = Depends()):
    return service.payment()