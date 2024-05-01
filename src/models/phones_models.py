from pydantic import BaseModel
from starlette import status


class DataValidation(BaseModel):
    phone: str
    address: str


class MainException(Exception):
    STATUS_CODE: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    FORMAT: str = "Unknown exception"

    @property
    def exception_response(self):
        return self.FORMAT


class DataAlreadyExist(MainException):
    STATUS_CODE: int = status.HTTP_409_CONFLICT
    FORMAT = "Запись с таким номером уже существует"


class InvalidDataUpdate(MainException):
    STATUS_CODE: int = status.HTTP_404_NOT_FOUND
    FORMAT = "Невозможно обновить несуществующую запись"
