from flask import jsonify, render_template,Blueprint, request

from backend.controllers.userlogin import verificar_token
from backend.persistence.user_persistence import buscar_usuario_id

panel_bp = Blueprint('panel_bp',__name__)

@panel_bp.route('/')
@verificar_token  # Esta ruta está protegida, se requiere autenticación
def panel():
    user_id = request.usuario['id']  # Obtener el id del usuario del token
    
    # Llamar a la función para obtener el usuario completo (incluyendo el nombre del rango)
    usuario = buscar_usuario_id(user_id)
    
    if usuario is None:
        return "Usuario no encontrado", 404
    
    # Pasar la información del usuario (incluyendo el rango) al template
    return render_template('panel.html', user=usuario)

@panel_bp.route('/profile')
@verificar_token  # Esta ruta está protegida, se requiere autenticación
def profile():
    user_id = request.usuario['id']  # Obtener el id del usuario del token
    
    # Llamar a la función para obtener el usuario
    usuario = buscar_usuario_id(user_id)
    print(usuario)
    if usuario is None:
        return "Usuario no encontrado", 404
    # Pasar la información del usuario al template
    return render_template('profile.html', user=usuario)