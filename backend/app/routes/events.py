from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from ..database import get_db

from ..schemas import EventCreate
from ..schemas import EventResponse
from ..schemas import UserSummary

from ..crud import create_event
from ..crud import get_events
from ..crud import get_user_summary

router = APIRouter()

@router.post(
    "/events",
    response_model=EventResponse,
    status_code=201
)
def create_new_event(
    event: EventCreate,
    db: Session = Depends(get_db)
):
    return create_event(
        db=db,
        event_data=event
    )

@router.get("/events", response_model=list[EventResponse])
def list_events(
    user_id: str | None = None,
    event_type: str | None = None,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    return get_events(
        db=db,
        user_id=user_id,
        event_type=event_type,
        skip=skip,
        limit=limit
    )

@router.get(
    "/users/{user_id}/summary",
    response_model=UserSummary
)
def user_summary(
    user_id: str,
    db: Session = Depends(get_db)
):
    summary = get_user_summary(
        db=db,
        user_id=user_id
    )

    if summary is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur introuvable"
        )

    return summary