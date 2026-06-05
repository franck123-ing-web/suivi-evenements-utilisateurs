from datetime import datetime
from enum import Enum

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class EventType(str, Enum):
    connexion = "connexion"
    transaction = "transaction"
    signalement = "signalement"


class EventCreate(BaseModel):
    user_id: str = Field(
        min_length=1,
        max_length=100
    )

    event_type: EventType

    timestamp: datetime

    event_metadata: dict | None = None


class EventResponse(BaseModel):
    id: int

    user_id: str

    event_type: EventType

    timestamp: datetime

    event_metadata: dict | None = None

    model_config = ConfigDict(
        from_attributes=True
    )


class UserSummary(BaseModel):
    user_id: str

    total_events: int

    by_type: dict[str, int]

    first_event: datetime | None

    last_event: datetime | None