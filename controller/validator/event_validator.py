from datetime import datetime

class EventValidator:
    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description

    def validate(self):
        # Validación de campos requeridos
        if not self.name or not self.date or not self.description:
            raise ValueError("Name, date, location, and description are required.")
        
        # Validación de longitud del nombre
        if len(self.name) > 50:
            raise ValueError("Name cannot exceed 50 characters.")
        
        # Validación de longitud de la descripción
        if len(self.description) > 200:
            raise ValueError("Description cannot exceed 200 characters.")
        
        # Validación del formato de la fecha (YYYY-MM-DD)
        try:
            datetime.strptime(self.date, "%Y-%m-%d")  # Intenta convertir la fecha
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

