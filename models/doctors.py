from flask import current_app as app
from sqlalchemy.orm import deferred, backref


class Doctors(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(50), nullable=False)
    surname = app.db.Column(app.db.String(100), nullable=False)
    phone = app.db.Column(app.db.String(15), nullable=False)
    email = app.db.Column(app.db.String(100), nullable=False, unique=True)
    password = deferred(app.db.Column(app.db.String, nullable=False))

    department_id = app.db.Column(app.db.Integer, app.db.ForeignKey('departments.id'), nullable=False)
    position_id = app.db.Column(app.db.Integer, app.db.ForeignKey('positions.id'), nullable=False)

    department = app.db.relationship("Departments", backref=backref("department", lazy="dynamic"))


    def __repr__(self):
        return '<Doctors %r> % self.id'
    
    def get_id(self):
        return str(self.id)

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

