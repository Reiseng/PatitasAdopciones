from flask import Blueprint, jsonify, request
from backend.persistence.user_persistence import (
    buscar_usuario_id,
    eliminar_usuario,
    buscar_usuarios_filtro,
    editar_usuario,
    agregar_usuario,
    editar_mi_usuario,
    editar_sin_password,
)
from backend.controllers.validations.user_validator import (
    validate_user_data,
    validate_name,
    validate_mail,
    validate_rank,
    validate_password,
)
from backend.controllers.userlogin import verificar_token  # Importar el middleware para verificar token

users_bp = Blueprint('user', __name__)


@users_bp.route('/', methods=['GET'])
@verificar_token
def get_users():
    nombre = request.args.get('nombre')
    rango = request.args.get('rango')
    id = request.args.get('id')
    
    # Construir filtros dinámicos según los parámetros proporcionados
    usuarios = buscar_usuarios_filtro(nombre, rango, id)
    if not usuarios:
        return jsonify({'error': 'No se encontraron usuarios'}), 404
    return jsonify(usuarios)

# Ruta para obtener un usuario por su ID
@users_bp.route('/<int:id_usuario>', methods=['GET'])
@verificar_token
def get_user(id_usuario):
    usuario = buscar_usuario_id(id_usuario)
    return jsonify(usuario)

# Ruta para eliminar un usuario por su ID (solo admin)
@users_bp.route('/<int:id_usuario>', methods=['DELETE'])
@verificar_token
def delete_user(id_usuario):
    eliminar_usuario(id_usuario)
    return jsonify({'message': 'Usuario eliminado correctamente'})

# Ruta para editar un usuario
@users_bp.route('/<int:id_usuario>', methods=['PUT'])
@verificar_token
def edit_user(id_usuario):
    if request.usuario.get('id') == id_usuario:
        nuevo_mail = request.json.get('mail')
        nuevo_nombre = request.json.get('nombre')
        nuevo_pass = request.json.get('password')
        if nuevo_pass == None:
            editar_sin_password(id_usuario,nuevo_mail ,nuevo_nombre)
            return generar_respuesta_json('Usuario editado correctamente', 200)
        elif validate_password(nuevo_pass):
            editar_mi_usuario(id_usuario, nuevo_mail, nuevo_nombre, nuevo_pass)
        return generar_respuesta_json('Usuario editado correctamente', 200)
    nuevo_nombre = request.json.get('nombre')
    nuevo_rango = request.json.get('rango')
    # Proceder con la edición si pasó la validación
    editar_usuario(id_usuario, nuevo_nombre, nuevo_rango)
    return generar_respuesta_json('Usuario editado correctamente', 200)

# Ruta para agregar un nuevo usuario
@users_bp.route('/', methods=['POST'])
#@verificar_token
def add_user():
    data = request.json
   # rango_usuario = request.usuario.get('rango')  # Suponiendo que este valor existe en `request`

    # Validar los datos proporcionados
    error_response = validate_user_data(data)
    if error_response:
        return error_response

    # Validar nombre
    error_response = validate_name(data.get('name'))
    if error_response:
        return error_response

    # Validar correo electrónico
    error_response = validate_mail(data.get('mail'))
    if error_response:
        return error_response

    # Validar contraseña
    error_response = validate_password(data.get('password'))
    if error_response:
        return error_response

    # Validar rango del usuario
    error_response = validate_rank(data.get('rango'))
    if error_response:
        return error_response
    # Proceder con la creación si pasó la validación
    agregar_usuario(data['mail'], data['name'], data['password'], data['rango'])
    return generar_respuesta_json('Usuario agregado correctamente', 200)

def generar_respuesta_json(mensaje, codigo_estado):
    return jsonify({'message': mensaje}), codigo_estado

