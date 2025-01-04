from database.db_connection import abrir_conexion, cerrar_conexion
from model.event import Event

class EventPersistence:
    def __init__(self):
        self.next_id = 1

    def add_event(self, name, date, description, content):
        self.next_id += 1
        cursor, connection = abrir_conexion()
        try:
            cursor.execute(
                "INSERT INTO events (name, date, description, content) VALUES ( %s, %s, %s, %s)",
                ( name, date, description, content)
            )
            connection.commit()
            cursor.execute("SELECT * FROM events WHERE id = %s", (self.next_id,))
            added_event = cursor.fetchone()
            columns = [col[0] for col in cursor.description]  # Obtener nombres de columnas
            if added_event:
                return dict(zip(columns, added_event))  # Crear un diccionario con los datos del usuario
            return None  # Si no se encuentra el usuario
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cerrar_conexion(cursor, connection)
    
    def get_event(self, event_id):
        cursor, connection = abrir_conexion()
        try:
            cursor.execute("SELECT * FROM events WHERE id = %s", (event_id,))
            columns = [col[0] for col in cursor.description]  # Obtener nombres de columnas
            events = cursor.fetchone()  # Obtener una sola fila
            if events:
                return dict(zip(columns, events))  # Crear un diccionario con los datos del usuario
            return None  # Si no se encuentra el usuario
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cerrar_conexion(cursor, connection)
    
    def get_all_events(self):
        cursor, connection = abrir_conexion()
        try:
            cursor.execute("SELECT * FROM events")
            columnas = [col[0] for col in cursor.description]  # Obtener nombres de columnas
            events = [dict(zip(columnas, events)) for events in cursor.fetchall()]  # Crear lista de diccionarios
            connection.commit()
            return events
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cerrar_conexion(cursor, connection)
    
    def update_event(self, event_id, name=None, date=None, description=None, content=None):
        cursor, connection = abrir_conexion()
        try:
            # Verificar si el usuario existe
            cursor.execute("SELECT * FROM events WHERE id = %s", (event_id,))
            event = cursor.fetchone()
            
            if not event:
                return None  # Si no se encuentra el usuario, retornar None

            # Si el usuario existe, proceder a la actualización
            fields = []
            values = []

            if name:
                fields.append("name = %s")
                values.append(name)
            if date:
                fields.append("date = %s")
                values.append(date)
            if description:
                fields.append("description = %s")
                values.append(description)
            if content:
                fields.append("content = %s")
                values.append(content)

            if fields:
                values.append(event_id)
                query = f"UPDATE events SET {', '.join(fields)} WHERE id = %s"
                cursor.execute(query, tuple(values))
                connection.commit()

            # Obtener el usuario actualizado
            cursor.execute("SELECT * FROM events WHERE id = %s", (event_id,))
            updated_user = cursor.fetchone()
            return updated_user  # Retornar el usuario actualizado

        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cerrar_conexion(cursor, connection)

    def delete_event(self, event_id):
        cursor, connection = abrir_conexion()
        try:
            cursor.execute("SELECT * FROM events WHERE id = %s", (event_id,))
            deleted_event = cursor.fetchone()
            cursor.execute("DELETE FROM events WHERE id = %s", (event_id,))
            connection.commit()
            return deleted_event  # Retornar el usuario actualizado
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cerrar_conexion(cursor, connection)