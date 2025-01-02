from model.event import Event

class InMemoryEventRepository:
    def __init__(self):
        self.events = {}
        self.next_id = 1

    def add_event(self, name, date, location, description):
        event = Event(self.next_id, name, date, location, description)
        self.events[self.next_id] = event
        self.next_id += 1
        return event
    
    def get_event(self, event_id):
        return self.events.get(event_id, None)
    
    def get_all_events(self):
        return list(self.events.values())
    
    def update_event(self, event_id, name=None, date=None, location=None, description=None):
        event = self.events.get(event_id)
        if event:
            if name:
                event.name = name
            if date:
                event.date = date
            if location:
                event.location = location
            if description:
                event.description = description
            return event
        return None
    def delete_event(self, event_id):
        return self.events.pop(event_id, None)
    