import enum
import uuid
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    Computed,
    DateTime,
    Enum,
    Index,
    Numeric,
    String,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class ActivityLevel(enum.Enum):
    sedentary = "sedentary"
    light = "light"
    moderate = "moderate"
    active = "active"
    very_active = "very_active"

class Sex(enum.Enum):
    male = "male"
    female = "female"
    other = "other"


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, server_default=text("gen_random_uuid()")
    )
    name: Mapped[str] = mapped_column(String(100))
    surname: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))
    birth_date: Mapped[date]
    weight_kg: Mapped[Decimal] = mapped_column(Numeric(5, 2))
    height_cm: Mapped[Decimal] = mapped_column(Numeric(5, 1))
    activity: Mapped[ActivityLevel] = mapped_column(
        Enum(ActivityLevel, name="activity_level"),
        server_default=ActivityLevel.moderate.value,
    )
    sex: Mapped[Sex] = mapped_column(
        Enum(Sex, name="sex"), server_default=Sex.male.value
    )
    bmi: Mapped[Decimal] = mapped_column(
        Numeric(4, 1),
        Computed("weight_kg / ((height_cm / 100) ^ 2)", persisted=True),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    __table_args__ = (
        CheckConstraint("weight_kg > 0 AND weight_kg < 500", name="weight_range"),
        CheckConstraint("height_cm > 0 AND height_cm < 300", name="height_range"),
    )


Index("users_email_key", func.lower(User.email), unique=True)