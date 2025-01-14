import uuid
from controller.encrypters.password_encrypter import encrypt_password
from database.db_connection import abrir_conexion, cerrar_conexion

class UserPersistence:
    def __init__(self):
        pass

    def add_user(self, name, email, password, rank):
        hashed_password = encrypt_password(password)
        user_id = str(uuid.uuid4())
        cursor, connection = abrir_conexion()
        try:
            cursor.execute(
                "INSERT INTO users (id, email, name, password, rank) VALUES (%s, %s, %s, %s, %s)",
                (user_id,email, name, hashed_password, rank)
            )
            connection.commit()
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            added_user = cursor.fetchone()
            columns = [col[0] for col in cursor.description]  # Obtener nombres de columnas
            if added_user:
                return dict(zip(columns, added_user ))  # Crear un diccionario con los datos del usuario
            return None  # Si no se encuentra el usuario
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cerrar_conexion(cursor, connection)

    def get_user(self, user_id):
        cursor, connection = abrir_conexion()
        try:
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            columns = [col[0] for col in cursor.description]  # Obtener nombres de columnas
            user = cursor.fetchone()  # Obtener una sola fila
            if user:
                return dict(zip(columns, user))  # Crear un diccionario con los datos del usuario
            return None  # Si no se encuentra el usuario
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cerrar_conexion(cursor, connection)

    def get_all_users(self):
        cursor, connection = abrir_conexion()
        try:
            cursor.execute("SELECT id, name, email, rank FROM users")
            columnas = [col[0] for col in cursor.description]  # Obtener nombres de columnas
            users = [dict(zip(columnas, user)) for user in cursor.fetchall()]  # Crear lista de diccionarios
            connection.commit()
            return users
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cerrar_conexion(cursor, connection)

    def update_user(self, user_id, name=None, email=None, password=None, rank=None):
        cursor, connection = abrir_conexion()
        try:
            # Verificar si el usuario existe
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
            
            if not user:
                return None  # Si no se encuentra el usuario, retornar None

            # Si el usuario existe, proceder a la actualización
            fields = []
            values = []

            if name:
                fields.append("name = %s")
                values.append(name)
            if email:
                fields.append("email = %s")
                values.append(email)
            if password:
                fields.append("password = %s")
                values.append(encrypt_password(password))
            if rank:
                fields.append("rank = %s")
                values.append(rank)

            if fields:
                values.append(user_id)
                query = f"UPDATE users SET {', '.join(fields)} WHERE id = %s"
                cursor.execute(query, tuple(values))
                connection.commit()

            # Obtener el usuario actualizado
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            updated_user = cursor.fetchone()
            return updated_user  # Retornar el usuario actualizado

        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cerrar_conexion(cursor, connection)
            
    def delete_user(self, user_id):
        cursor, connection = abrir_conexion()
        try:
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            deleted_user = cursor.fetchone()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            connection.commit()
            return deleted_user  # Retornar el usuario actualizado
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cerrar_conexion(cursor, connection)