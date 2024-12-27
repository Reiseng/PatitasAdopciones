from dotenv import load_dotenv
import os
import psycopg2

# Cargar las variables de entorno
load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port="5432"  # puerto por defecto
    )