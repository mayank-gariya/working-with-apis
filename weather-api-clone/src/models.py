from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import Optional

class WeatherRecord(BaseModel):
    city: str = Field(..., min_length=1)
    country: Optional[str] = "Unknown"
    temperature: float = Field(..., description="Temperature in Celsius")
    windspeed: float = Field(..., ge=0, description="Windspeed cannot be negative")
    unit: str = "Celsius"
    total_taken: float
    date_of_request: date

    @field_validator('temperature')
    @classmethod
    def validate_temp(cls, v):
        if v < -90 or v > 60:
            raise ValueError('Temperature is outside realistic Earth limits')
        return v

    def to_json_dict(self):
        return self.model_dump(mode='json')