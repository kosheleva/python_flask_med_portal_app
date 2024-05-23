from flask import render_template, request, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user

class Auth():


    def __init__(self, db, models):
        self.db = db
        self.models = models


    def register(self):
        positions = self.models['positions'].query.order_by(self.models['positions'].name).all()
        departments = self.models['departments'].query.order_by(self.models['departments'].name).all()

        if request.method == 'POST':
            name = request.form['name']
            surname = request.form['surname']
            phone = request.form['phone']
            email = request.form['email']
            password = request.form['password']
            position_id = request.form['position_id']
            department_id = request.form['department_id']

            empty_fields = []

            for field in request.form:
                if not request.form[field]:
                    empty_fields.append(field)

            if len(empty_fields):
                return render_template('register.html', positions=positions, departments=departments, empty_fields=empty_fields)


            hashed_password = generate_password_hash(password, method='pbkdf2:sha256:600000')
            try:
                new_user = self.models['doctors'](
                    name=name,
                    surname=surname,
                    phone=phone,
                    email=email,
                    password=hashed_password,
                    position_id=position_id,
                    department_id=department_id
                )

                self.db.session.add(new_user)
                self.db.session.commit()

                login_user(new_user)
                return redirect("/patients")
            except Exception as e:
                print(e)
                return render_template('error.html')

            return redirect("/patients")
        else:
            return render_template('register.html', positions=positions, departments=departments)


    def login(self):
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = self.models['doctors'].query.filter_by(email=email).first()

            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect("/patients")
                else:
                    return render_template('error.html')
            else:
                return redirect("/register")
        else:
            return render_template('login.html')


    def logout(self):
        logout_user()
        return redirect("/login")
