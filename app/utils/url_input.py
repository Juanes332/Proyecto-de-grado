from pydantic import BaseModel, HttpUrl, field_validator
from typing import Optional


class URLInput(BaseModel):
    url: HttpUrl
    speed: Optional[int] = 4

    @field_validator("url")
    def validate_url(cls, value):
        """
        Valida que la URL tenga esquema HTTPS o HTTP.
        """
        if not value.scheme in ("http", "https"):
            raise ValueError("La URL debe comenzar con http o https")
        return value

    @field_validator("speed")
    def validate_speed(cls, value):
        """
        Valida que la velocidad esté entre 1 (lento) y 5 (muy rápido).
        """
        if value < 1 or value > 5:
            raise ValueError(
                "La velocidad debe estar entre 1 (lento) y 5 (muy rápido).")
        return value
