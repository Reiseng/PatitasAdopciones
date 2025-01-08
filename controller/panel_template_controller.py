from flask import render_template,Blueprint, request
from controller.user_controller import user_service
from controller.userlogin import verificar_token
panel = Blueprint('panel_template',__name__)

@panel.route('/')
@verificar_token # Esta ruta está protegida, se requiere autenticación
def Panel():
    user_id = request.user['id']
    user = user_service.get_user(user_id)
    if user is None:
        return "Usuario no encontrado", 404
    
    # Pasar la información del usuario (incluyendo el rango) al template
    return render_template('panel.html', user=user)


@panel.route('/profile')
@verificar_token  # Esta ruta está protegida, se requiere autenticación
def Profile():
    user_id = request.user['id']  # Obtener el id del usuario del token
    
    # Llamar a la función para obtener el usuario
    user = user_service.get_user(user_id)
    if user is None:
        return "User not found", 404
    # Pasar la información del usuario al template
    return render_template('profile.html', user=user)

@panel.route('/user')
@verificar_token  # Esta ruta está protegida, se requiere autenticación
def User():
    user_id = request.user['id']  # Obtener el id del usuario del token
    # Llamar a la función para obtener el usuario
    user = user_service.get_user(user_id)
    if user is None:
        return "User not found", 404
    #
    return render_template('user_managment.html', user= user)

@panel.route('/event')
@verificar_token  # Esta ruta está protegida, se requiere autenticación
def Event():
    return render_template('event_managment.html')