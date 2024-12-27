# Funciones para manejar la conexión
from backend.controllers.encrypters.password_encrypter import encrypt_password
from backend.database.db_connection import get_db_connection

def abrir_conexion():
    connection = get_db_connection()
    cursor = connection.cursor()
    return cursor, connection

def cerrar_conexion(cursor, connection):
    cursor.close()
    connection.close()

def buscar_usuario_id(id_usuario):
    cursor, connection = abrir_conexion()
    try:
        # Consulta con JOIN para obtener el nombre del rango
        cursor.execute("""
            SELECT 
                usuarios.id, 
                usuarios.mail, 
                usuarios.nombre, 
                rangos.nombre AS rangos 
            FROM usuarios
            INNER JOIN rangos ON usuarios.rango = rangos.id
            WHERE usuarios.id = %s
        """, (id_usuario,))
        columnas = [col[0] for col in cursor.description]  # Nombres de las columnas
        usuario = cursor.fetchone()
        return dict(zip(columnas, usuario)) if usuario else None
    finally:
        cerrar_conexion(cursor, connection)

def eliminar_usuario(id_usuario):
    cursor, connection = abrir_conexion()
    try:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
        connection.commit()
    finally:
        cerrar_conexion(cursor, connection)

def editar_usuario(id_usuario, nuevo_nombre, nuevo_rango):
    cursor, connection = abrir_conexion()
    try:
        cursor.execute(
            "UPDATE usuarios SET nombre = %s, rango = %s WHERE id = %s",
            (nuevo_nombre, nuevo_rango, id_usuario)
        )
        connection.commit()
    finally:
        cerrar_conexion(cursor, connection)

def agregar_usuario(mail,nombre, password, id_rango):
    hashed_password = encrypt_password(password)
    cursor, connection = abrir_conexion()
    try:
        cursor.execute(
            "INSERT INTO usuarios (mail,nombre, pass, rango) VALUES (%s,%s, %s, %s)",
            (mail, nombre, hashed_password, id_rango)
        )
        connection.commit()
    finally:
        cerrar_conexion(cursor, connection)

def editar_mi_usuario(id_usuario,nuevo_mail ,nuevo_nombre, nuevo_pass):
    cursor, connection = abrir_conexion()
    try:
        cursor.execute(
            "UPDATE usuarios SET mail = %s, nombre = %s, pass = %s WHERE id = %s",
            (nuevo_mail, nuevo_nombre, nuevo_pass, id_usuario)
        )
        connection.commit()
    finally:
        cerrar_conexion(cursor, connection)

def editar_sin_password(id_usuario,nuevo_mail ,nuevo_nombre):
    cursor, connection = abrir_conexion()
    try:
        cursor.execute(
            "UPDATE usuarios SET mail = %s, nombre = %s WHERE id = %s",
            (nuevo_mail, nuevo_nombre, id_usuario)
        )
        connection.commit()
    finally:
        cerrar_conexion(cursor, connection)

def buscar_usuarios_filtro(nombre, rango, id):
    cursor, connection = abrir_conexion()
    try:
        # Base de la consulta
        query = """
            SELECT 
                usuarios.id, 
                usuarios.mail, 
                usuarios.nombre, 
                rangos.nombre AS rango 
            FROM usuarios
            INNER JOIN rangos ON usuarios.rango = rangos.id
        """
        filters = []
        params = []
        
        # Filtros dinámicos
        if nombre:
            filters.append("usuarios.nombre = %s")
            params.append(nombre)
        
        if rango:
            filters.append("rangos.nombre = %s")
            params.append(rango)

        if id:
            filters.append("usuarios.id = %s")
            params.append(id)

        # Agregar filtros si existen
        if filters:
            query += " WHERE " + " AND ".join(filters)
        
        cursor.execute(query, tuple(params))
        usuarios = cursor.fetchall()
        return usuarios
    finally:
        cerrar_conexion(cursor, connection)
