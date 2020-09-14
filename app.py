from flask import Flask, render_template, jsonify, request ,flash, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager 
# from form import SignUpForm,LoginForm
# from flask.ext.login import LoginManager


app = Flask(__name__,template_folder = '/home/parisa/myproje/flask/template kamel/template')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://user_f:password@localhost/database_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'THISISSECRETKEY'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

csrf = CSRFProtect(app)
csrf.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import User
from models import Address
from views import my_view
app.register_blueprint(my_view)
         
if __name__ == '__main__':
    app.run(debug = True)