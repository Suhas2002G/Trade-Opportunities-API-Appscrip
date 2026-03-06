from pydantic import BaseModel, field_validator
import re

class SectorRequest(BaseModel):
    sector: str

    @field_validator("sector")
    def validate_sector(cls, value):
        if not re.match("^[a-zA-Z ]+$", value):
            raise ValueError("Sector must contain only letters")
        return value.lower()