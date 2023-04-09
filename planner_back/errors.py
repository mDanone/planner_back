from typing import Any

from fastapi.exceptions import HTTPException


class BaseHttpException(HTTPException):
    status_code: int = 500
    message: str

    def __init__(
        self, message: str | None = None, headers: dict[str, Any] | None = None
    ) -> None:
        if message is not None:
            self.message = message
        super().__init__(
            status_code=self.status_code, detail=self.message, headers=headers
        )


class NotFound(BaseHttpException):
    status_code: int = 404
    message: str = "Entity not found"
