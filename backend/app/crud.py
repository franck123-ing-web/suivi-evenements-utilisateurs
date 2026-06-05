from collections import Counter

from sqlalchemy.orm import Session

from .models import Event
from .schemas import EventCreate
from .schemas import UserSummary


def create_event(
    db: Session,
    event_data: EventCreate
) -> Event:
    """
    Crée un nouvel événement.
    """

    event = Event(
        user_id=event_data.user_id,
        event_type=event_data.event_type.value,
        timestamp=event_data.timestamp,
        event_metadata=event_data.event_metadata
    )

    db.add(event)

    db.commit()

    db.refresh(event)

    return event


def get_events(
    db: Session,
    user_id: str | None = None,
    event_type: str | None = None
) -> list[Event]:
    """
    Retourne les événements filtrés.
    """

    query = db.query(Event)

    if user_id:
        query = query.filter(
            Event.user_id == user_id
        )

    if event_type:
        query = query.filter(
            Event.event_type == event_type
        )

    return query.order_by(
        Event.timestamp.desc()
    ).all()


def get_user_summary(
    db: Session,
    user_id: str
) -> UserSummary | None:
    """
    Retourne le résumé d'activité d'un utilisateur.
    """

    events = (
        db.query(Event)
        .filter(Event.user_id == user_id)
        .order_by(Event.timestamp.asc())
        .all()
    )

    if not events:
        return None

    counter = Counter(
        event.event_type
        for event in events
    )

    return UserSummary(
        user_id=user_id,
        total_events=len(events),
        by_type=dict(counter),
        first_event=events[0].timestamp,
        last_event=events[-1].timestamp
    )