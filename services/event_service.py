from persistence.eventDao import EventPersistence
class EventService:
    def __init__(self):
        self.event_repository = EventPersistence()

    def create_event(self, name, date, description, content):
        # Lógica de negocio para crear un evento, como validaciones
        if not name or not description or not date or not content:
            raise ValueError("Name, description, date, location, and are required.")
        event = self.event_repository.add_event(name, date, description, content)
        return event
    
    def get_event(self, event_id):
        event = self.event_repository.get_event(event_id)
        if not event:
            raise ValueError(f"Event with ID {event_id} not found.")
        return event
    
    def get_all_events(self):
        return self.event_repository.get_all_events()
    
    def update_event(self, event_id, name=None, date=None, description=None,  content= None):
        event = self.event_repository.update_event(event_id, name, date, description, content)
        if not event:
            raise ValueError(f"Event with ID {event_id} not found.")
        return event
    
    def delete_event(self, event_id):
        event = self.event_repository.delete_event(event_id)
        if not event:
            raise ValueError(f"Event with ID {event_id} not found.")
        return event