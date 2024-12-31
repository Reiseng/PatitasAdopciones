from flask import Flask, jsonify, make_response, redirect, render_template, request, url_for
from flask_cors import CORS
from backend.controllers.userlogin import auth_bp, verificar_token
from backend.controllers.users_controller import users_bp
from backend.controllers.company_controller import company_bp
from backend.controllers.events_controller import events_bp, event_bp
from backend.controllers.panel import panel_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(users_bp, url_prefix='/user')
app.register_blueprint(company_bp, url_prefix='/company')
app.register_blueprint(events_bp, url_prefix='/events')
app.register_blueprint(event_bp, url_prefix='/event')
app.register_blueprint(panel_bp, url_prefix='/panel')

@app.route('/')
def index():
    # Verificar si el usuario está loggeado (si tiene un token)
    if request.cookies.get('access_token'):
        # Si está loggeado, mostrar opciones de panel y logout
        return render_template('index_protected.html')  # Este template es para usuarios loggeados
    else:
        # Si no está loggeado, mostrar la opción de login
        return render_template('index.html')  # Este template es para usuarios no loggeados
@app.route('/login')
def login():
    if request.cookies.get('access_token'):
        return redirect(url_for('panel_bp.panel'))
    return render_template('login.html')
@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('access_token', '', max_age=0)  # Eliminar la cookie
    return response

@app.before_request
def override_method():
    print(f"Request Method: {request.method}")  # Ver qué método se recibe
    if request.method == 'POST' and '_method' in request.form:
        method = request.form['_method'].upper()
        if method in ['PUT', 'DELETE']:
            request.environ['REQUEST_METHOD'] = method
            print(f"Method overridden to: {method}")  # Ver el nuevo método
