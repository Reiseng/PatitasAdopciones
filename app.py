from flask import Flask, jsonify, render_template
from flask_cors import CORS
from backend.controllers.userlogin import auth_bp, verificar_token
from backend.controllers.users_controller import users_bp
from backend.controllers.company_controller import company_bp
from backend.controllers.events_controller import events_bp, event_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(users_bp, url_prefix='/user')
app.register_blueprint(company_bp, url_prefix='/company')
app.register_blueprint(events_bp, url_prefix='/events')
app.register_blueprint(event_bp, url_prefix='/event')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/panel')
@verificar_token  # Esta ruta está protegida, se requiere autenticación
def panel():
    # Esta ruta solo es accesible si el usuario está loggeado
    return render_template('panel.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)