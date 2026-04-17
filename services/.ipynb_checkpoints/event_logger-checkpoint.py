from database.db import get_connection
from database.models import EventLog
from datetime import datetime
from services.event_processor import process_event

def log_event(event_type, user_id, data=None):
    db = get_connection()

    event = EventLog(
        event_type=event_type,
        user_id=user_id,
        data=data,
    )

    db.add(event)
    db.commit()
    
    process_event(event_type,user_id,data)
    
    db.close()