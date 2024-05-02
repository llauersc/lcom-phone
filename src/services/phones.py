import inject

from models import DataValidation
from models.phones_models import DataAlreadyExist, InvalidDataUpdate
from repositories import PhonesRepository

service = None


@inject.autoparams()
def get_service(repo: PhonesRepository):
    global service

    if service is None:
        service = PhonesService(repo)
    return service


class PhonesService:
    @inject.autoparams()
    def __init__(self, repo: PhonesRepository):
        self.repo = repo

    async def add_data(self, data: DataValidation, forced):
        """ Можно было бы использовать и для апдейта и для создания, но решено логику разделить """
        if forced or not await self.repo.get_data(data.phone):
            return await self.repo.set_data(data.phone, data.address)
        raise DataAlreadyExist("Запись с таким номером уже существует")

    async def check_data(self, phone: str):
        return await self.repo.get_data(phone)

    async def update_data(self, data: DataValidation):
        if await self.repo.get_data(data.phone):
            return await self.repo.set_data(data.phone, data.address)
        raise InvalidDataUpdate("Невозможно обновить несуществующую запись")
