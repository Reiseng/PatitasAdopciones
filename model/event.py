class Event:
    def __init__(self, id, name, date, location, description):
        self.id = id
        self.name = name
        self.date = date
        self.location = location
        self.description = description

    def __str__(self):
        return f"Event(id={self.id}, name={self.name}, date={self.date}, location={self.location}, description={self.description})"
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'location': self.location,
            'description': self.description
        }
