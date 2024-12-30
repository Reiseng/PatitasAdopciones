from flask import Blueprint, jsonify, make_response, redirect, request, url_for
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
def authenticate():
    if request.is_json:  # Si el contenido es JSON
        data = request.json
        mail = data.get('mail')
        password = data.get('password')
    else:  # Si el contenido es form-data (desde el formulario)
        mail = request.form.get('mail')
        password = request.form.get('password')

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

            # Crear la respuesta
            response = make_response(redirect(url_for('protected')))  # Redirigir al usuario a la página protegida

            # Guardar el token en las cookies
            secure_cookie = os.getenv('FLASK_ENV') == 'production'
            response.set_cookie('access_token', token, httponly=True, secure=secure_cookie, samesite='Strict', max_age=7200)
            return response
        else:
            return jsonify({'message': 'Contraseña incorrecta'}), 401
    else:
        return jsonify({'message': 'Correo electrónico no registrado'}), 404


@auth_bp.route('/logout', methods=['POST'])
def logout():
    response = jsonify({'message': 'Cierre de sesión exitoso'})
    response.set_cookie('access_token', '', max_age=0)  # Eliminar la cookie
    return response

# Middleware para verificar el token
def verificar_token(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.cookies.get('access_token')  # Obtener el token de las cookies
        if not token:
            response = make_response(redirect(url_for('login')))
            return response
        try:
            # Decodificar el token
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            request.usuario = decoded_token  # Añadir los datos del token al request
        except jwt.ExpiredSignatureError:
            return response
        except jwt.InvalidTokenError:
            return response
        return f(*args, **kwargs)
    return decorator