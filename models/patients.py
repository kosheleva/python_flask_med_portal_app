from flask import current_app as app


class Patients(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(50), nullable=False)
    surname = app.db.Column(app.db.String(100), nullable=False)
    phone = app.db.Column(app.db.String(15), nullable=False)
    gender = app.db.Column(app.db.Enum('Женский пол', 'Мужской пол'))
    date_of_birth = app.db.Column(app.db.DateTime)

    def __repr__(self):
        return '<Patients %r> % self.id'

