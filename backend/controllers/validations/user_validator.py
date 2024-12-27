import re
from flask import jsonify

def validate_user_data(data):
    if not data:
        return jsonify({'error': 'Datos de usuario no proporcionados'}), 400
    if 'nombre' not in data or 'mail' not in data or 'password' not in data or 'id_rango' not in data:
        return jsonify({'error': 'Datos de usuario incompletos'}), 400
    if not data['nombre'] or not data['mail'] or not data['password'] or not data['id_rango']:
        return jsonify({'error': 'Datos de usuario incompletos'}), 400
    return None

def validate_user_edit_data(data):
    if not data:
        return jsonify({'error': 'Datos de usuario no proporcionados'}), 400
    if 'nombre' not in data or 'id_rango' not in data:
        return jsonify({'error': 'Datos de usuario incompletos'}), 400
    if not data['nombre'] or not data['id_rango']:
        return jsonify({'error': 'Datos de usuario incompletos'}), 400
    return None

def validate_password(password):
    if not password:
        return jsonify({'error': 'Contraseña no proporcionada'}), 400
    if len(password) < 8:
        return jsonify({'error': 'La contraseña debe tener al menos 8 caracteres'}), 400
    if not any(char.isdigit() for char in password):
        return jsonify({'error': 'La contraseña debe contener al menos un número'}), 400
    if not any(char.isalpha() for char in password):
        return jsonify({'error': 'La contraseña debe contener al menos una letra'}), 400
    if not any(char.isupper() for char in password):
        return jsonify({'error': 'La contraseña debe contener al menos una letra mayúscula'}), 400
    if not any(char.islower() for char in password):
        return jsonify({'error': 'La contraseña debe contener al menos una letra minúscula'}), 400
    if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for char in password):
        return jsonify({'error': 'La contraseña debe contener al menos un carácter especial'}), 400
    return None

def validate_name(nombre):
    if not nombre:
        return jsonify({'error': 'Nombre no proporcionado'}), 400
    if len(nombre) < 3:
        return jsonify({'error': 'El nombre debe tener al menos 3 caracteres'}), 400
    if not nombre.isalpha():
        return jsonify({'error': 'El nombre solo debe contener letras'}), 400
    return None

def validate_mail(mail):
    if not mail:
        return jsonify({'error': 'Correo electrónico no proporcionado'}), 400
    if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
        return jsonify({'error': 'Correo electrónico no válido'}), 400
    return None

def validate_rango(rango):
    if not rango:
        return jsonify({'error': 'Rango no proporcionado'}), 400
    if not isinstance(rango, int):
        return jsonify({'error': 'Rango debe ser un número entero'}), 400
    if rango < 1 or rango > 3:
        return jsonify({'error': 'Rango debe estar entre 1 y 3'}), 400
    return None