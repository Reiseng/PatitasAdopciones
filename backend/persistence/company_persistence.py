from backend.database.db_connection import get_db_connection
from backend.model.entity.company_model import CompanyModel
from backend.database.db_connection import abrir_conexion, cerrar_conexion

def buscarEmpresa():
    cursor, connection = abrir_conexion()
    try:
        cursor.execute("""
            SELECT 
                id, 
                nombre, 
                mail, 
                telefono, 
                facebook, 
                instagram, 
                twitter 
            FROM datos_empresa
            WHERE id = 1
        """)
        
        row = cursor.fetchone()
        if row:
            # Crear una instancia del modelo usando los datos de la consulta
            empresa = CompanyModel(
                id=row[0],
                nombre=row[1],
                mail=row[2],
                telefono=row[3],
                facebook=row[4],
                instagram=row[5],
                twitter=row[6]
            )
            return empresa
        else:
            return None
    finally:
        cerrar_conexion(cursor, connection)

def actualizarEmpresa(empresa):
    cursor, connection = abrir_conexion()
    try:
        cursor.execute("""
            UPDATE datos_empresa
            SET
                nombre = %s,
                mail = %s,
                telefono = %s,
                facebook = %s,
                instagram = %s,
                twitter = %s
            WHERE id = 1
        """, (
            empresa.nombre,
            empresa.mail,
            empresa.telefono,
            empresa.facebook,
            empresa.instagram,
            empresa.twitter
        ))
        connection.commit()
    finally:
        cerrar_conexion(cursor, connection)