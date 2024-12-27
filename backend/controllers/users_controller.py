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
    if request.usuario.get('id_rango') == "2" or request.usuario.get('id_rango') == "1":
        return jsonify({'message': 'No tienes permisos para realizar esta acción'}), 403
    id_usuario_rango = buscar_usuario_id(id_usuario)
    validacion = verificar_rango(id_usuario_rango[4])
    if validacion:  # Si la validación devuelve algo, es un error
        return validacion
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
        elif len(nuevo_pass) < 8:
            return generar_respuesta_json('La contraseña debe tener al menos 8 caracteres', 403)
        editar_mi_usuario(id_usuario, nuevo_mail, nuevo_nombre, nuevo_pass)
        return generar_respuesta_json('Usuario editado correctamente', 200)
    nuevo_nombre = request.json.get('nombre')
    nuevo_rango = request.json.get('rango')
    # Verificar permisos
    rango_usuario = request.usuario.get('rango')  # Suponiendo que este valor existe en `request`
    validacion = verificar_rango(rango_usuario)
    if validacion:  # Si la validación devuelve algo, es un error
        return validacion
    if rango_usuario > 2:
        return generar_respuesta_json('No tienes permisos para realizar esta acción', 403)
    # Proceder con la edición si pasó la validación
    editar_usuario(id_usuario, nuevo_nombre, nuevo_rango)
    return generar_respuesta_json('Usuario editado correctamente', 200)

# Ruta para agregar un nuevo usuario
@users_bp.route('/', methods=['POST'])
@verificar_token
def add_user():
    nombre = request.json.get('name')
    mail = request.json.get('mail')
    password = request.json.get('password')
    rango = request.json.get('rango')
    rango_usuario = request.usuario.get('rango')  # Suponiendo que este valor existe en `request`
    if len(password) < 8:
        return generar_respuesta_json('La contraseña debe tener al menos 8 caracteres', 403)
    if rango_usuario >= rango:
        return generar_respuesta_json('No puedes crear un usuario con rango superior o igual al tuyo', 403)
    validacion = verificar_rango(rango)
    if validacion:  # Si la validación devuelve algo, es un error
        return validacion
    if rango_usuario > 2:
        return generar_respuesta_json('No tienes permisos para realizar esta acción', 403)
    # Proceder con la creacion si pasó la validación
    agregar_usuario(mail,nombre, password, rango)
    return generar_respuesta_json('Usuario agregado correctamente', 200)

def generar_respuesta_json(mensaje, codigo_estado):
    return jsonify({'message': mensaje}), codigo_estado

# Función verificar_rango utilizando la función genérica
def verificar_rango(id_usuario):
    print(id_usuario)
    if id_usuario == 1:
        return generar_respuesta_json('No puedes hacer eso a un administrador', 403)
    if id_usuario == 2:
        return generar_respuesta_json('No puedes hacer eso con alguien de tu mismo rango', 403) 
    return None  # Indica que la validación fue exitosa
