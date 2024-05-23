from flask_dotenv import DotEnv
from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


app = Flask(__name__)

env = DotEnv()
env.init_app(app, env_file='.env', verbose_mode = True)

app.config["SQLALCHEMY_DATABASE_URI"] = app.config['MYSQL_URI']
db = SQLAlchemy(app)
app.db = db


login_manager = LoginManager()
login_manager.init_app(app)


with app.app_context():
    from models import Doctors, Positions, Departments, Patients, Medicines, Consultations, PatientsSchemas


app.models = {
    "doctors": Doctors,
    "positions": Positions,
    "departments": Departments,
    "patients": Patients,
    "medicines": Medicines,
    "consultations": Consultations,
    "PatientsSchemas": PatientsSchemas
}


with app.app_context():
    import router


@login_manager.user_loader
def load_user(user_id):
    return Doctors.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run('127.0.0.1', debug = True)