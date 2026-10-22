import enum

from pydantic import BaseModel


class Error(BaseModel):
    detail: str


class ErrorCodes(enum.Enum):
    ALREADY_AUTHENTICTAED = "Alredy authenticated"
    UNAUTHORIZED = "Unauthorized"
    EMAIL_NOT_FOUND = "Email not found"
    INVALID_PASSWORD = "Invalid password"
    AUTH_CODE_NOT_REQUESTED = "Auth code not requested"


class DomainError(Exception):
    code: ErrorCodes

    def __init__(self, code: ErrorCodes, message: str | None = None):
        self.code = code
        super().__init__(message)


ERROR_STATUS_MAP = {
    ErrorCodes.UNAUTHORIZED: 401,
    ErrorCodes.EMAIL_NOT_FOUND: 404,
    ErrorCodes.INVALID_PASSWORD: 400,
    ErrorCodes.ALREADY_AUTHENTICTAED: 400,
    ErrorCodes.AUTH_CODE_NOT_REQUESTED: 400,
}
