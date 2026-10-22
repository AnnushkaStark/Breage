from pydantic import BaseModel


class SystemAlertLogBase(BaseModel):
    error_message: str
    is_sent_to_email: bool
