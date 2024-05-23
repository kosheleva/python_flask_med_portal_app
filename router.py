from flask import current_app as app
from flask_login import login_required
from routes import Auth, Patients


@app.route("/login", methods=['GET', 'POST'])
def login():
    route = Auth(app.db, app.models)
    return route.login()


@app.route("/register", methods=['GET', 'POST'])
def register():
    route = Auth(app.db, app.models)
    return route.register()


@app.get("/logout")
@login_required
def logout():
    route = Auth(app.db, app.models)
    return route.logout()


@app.get("/patients")
@login_required
def patients():
    route = Patients(app.db, app.models)
    return route.get_patients()


@app.route("/patients_add", methods=['GET', 'POST'])
@login_required
def patients_add():
    route = Patients(app.db, app.models)
    return route.add_patients()


@app.post("/patients_add_consultation")
@login_required
def patients_add_consultation():
    route = Patients(app.db, app.models)
    return route.patients_add_consultation()


@app.post("/patients_add_schema")
@login_required
def patients_add_schema():
    route = Patients(app.db, app.models)
    return route.patients_add_schema()