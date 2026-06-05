from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import JSON

from .database import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        String(100),
        nullable=False,
        index=True
    )

    event_type = Column(
        String(50),
        nullable=False,
        index=True
    )

    timestamp = Column(
        DateTime,
        nullable=False,
        index=True
    )

    event_metadata = Column(
    JSON,
    nullable=True
)