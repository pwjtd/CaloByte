from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from models import ActivityLevel, Sex


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    surname: str = Field(min_length=1, max_length=100)
    email: EmailStr
    birth_date: date
    weight_kg: float = Field(gt=0, lt=500)
    height_cm: float = Field(gt=0, lt=300)
    activity: ActivityLevel = ActivityLevel.moderate
    sex: Sex


class UserOut(UserCreate):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    bmi: float
    created_at: datetime