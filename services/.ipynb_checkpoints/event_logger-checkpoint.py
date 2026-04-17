from database.db import get_connection
from database.models import EventLog
from datetime import datetime

def log_event(event_type, user_id, data=None):
    db = get_connection()

    event = EventLog(
        event_type=event_type,
        user_id=user_id,
        data=data,
    )

    db.add(event)
    db.commit()
    db.close()