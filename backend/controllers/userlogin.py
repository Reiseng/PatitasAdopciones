from flask import Blueprint, jsonify, request
from backend.controllers.encrypters.password_encrypter import check_password
from backend.database.db_connection import get_db_connection
import jwt
import datetime
from dotenv import load_dotenv
from functools import wraps
import os

# Cargar variables de entorno
load_dotenv()

# Clave secreta para los tokens (desde el .env)
SECRET_KEY = os.getenv('SECRET_KEY')

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['POST'])
def login():
    data = request.json
    mail = data.get('mail')
    password = data.get('password')

    # Validar usuario en la base de datos
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, pass, rango FROM usuarios WHERE mail = %s", (mail,))
    usuario = cursor.fetchone()
    cursor.close()
    connection.close()

    if usuario:
        stored_hashed_password = usuario[1]
        if check_password(password, stored_hashed_password):
            # Crear token
            payload = {
                'id': usuario[0],  # ID del usuario
                'rango': usuario[2],  # Rango del usuario
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            return jsonify({'token': token})
        else:
            return jsonify({'message': 'Contraseña incorrecta'}), 401
    else:
        return jsonify({'message': 'Correo electrónico no registrado'}), 404

# Middleware para verificar el token
def verificar_token(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')  # Obtener el token
        if not token:
            return jsonify({'message': 'Token requerido'}), 401
        
        token = token.split(" ")[1]  # Extraer el token después de "Bearer"
        
        try:
            # Decodificar el token
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            request.usuario = decoded_token  # Añadir los datos del token al request
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido'}), 401
        return f(*args, **kwargs)
    return decorator
