from flask import Flask, make_response, redirect, render_template, request, url_for
from flask_cors import CORS
from controller.user_controller import user
from controller.event_controller import event, events_templates
from controller.panel_template_controller import panel
from controller.userlogin import auth_bp, verificar_token_directo

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(event, url_prefix='/api/event')
app.register_blueprint(events_templates, url_prefix='/event')
app.register_blueprint(user, url_prefix='/api/user')
app.register_blueprint(panel, url_prefix='/panel')

@app.route('/')
def index():
    token = request.cookies.get('access_token')  # Obtén el token de las cookies
    user = verificar_token_directo(token)  # Decodifica el token
    if user:  # Si el token es válido
        return render_template('index_protected.html', user=user)  # Para usuarios loggeados
    else:
        return render_template('index.html')  # Para usuarios no loggeados
    
@app.route('/login')
def login():
    token = request.cookies.get('access_token')  # Obtén el token de las cookies
    user = verificar_token_directo(token)  # Verifica el token y obtén el usuario
    if user:  # Si el token es válido
        return redirect(url_for('panel_template.Panel', user=user))  # Redirigir al panel con datos de usuario

    # Si el token no es válido o está ausente
    return render_template('login.html', error_message="Por favor, inicia sesión.")

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('access_token', '', max_age=0)  # Eliminar la cookie
    return response

@app.route('/nosotros')
def nosotros():
    token = request.cookies.get('access_token')  # Obtén el token de las cookies
    user = verificar_token_directo(token)  # Verifica el token y obtén el usuario
    if user:  # Si el token es válido
        return render_template('nosotros_protected.html', user=user)
    return render_template('nosotros.html')
@app.route('/donations')
def donations():
    token = request.cookies.get('access_token')  # Obtén el token de las cookies
    user = verificar_token_directo(token)  # Verifica el token y obtén el usuario
    if user:  # Si el token es válido
        return render_template('donations_protected.html', user=user)
    return render_template('donations.html')
@app.route('/contact') 
def contact():
    token = request.cookies.get('access_token')  # Obtén el token de las cookies
    user = verificar_token_directo(token)  # Verifica el token y obtén el usuario
    if user:  # Si el token es válido
        return render_template('contact_protected.html', user=user)
    return render_template('contact.html')

@app.before_request
def override_method():
    print(f"Request Method: {request.method}")  # Ver qué método se recibe
    if request.method == 'POST' and '_method' in request.form:
        method = request.form['_method'].upper()
        if method in ['PUT', 'DELETE']:
            request.environ['REQUEST_METHOD'] = method
            print(f"Method overridden to: {method}")  # Ver el nuevo método
