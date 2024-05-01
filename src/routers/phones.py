from fastapi import APIRouter, Depends

from models import DataValidation
from services import get_phones_service, PhonesService


def phones_service():
    return get_phones_service()


router = APIRouter(prefix="/phones", tags=["LCOM-Phones"])


@router.get("/check_data")
async def get_data(
    phone: str,
    service: PhonesService = Depends(phones_service),
):
    return await service.check_data(phone)


@router.post("/write_data")
async def post_data(
    data: DataValidation,
    forced: bool = False,
    service: PhonesService = Depends(phones_service),
):
    return await service.add_data(data, forced)


@router.put("/write_data")
async def update_data(
    data: DataValidation,
    service: PhonesService = Depends(phones_service),
):
    return await service.update_data(data)
