from flask import Flask
from flask_cors import CORS
from backend.controllers.userlogin import auth_bp
from backend.controllers.users_controller import users_bp
from backend.controllers.company_controller import company_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(users_bp, url_prefix='/user')
app.register_blueprint(company_bp, url_prefix='/company')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)