from flask import current_app as app


class Departments(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(50), nullable=False)
    name = app.db.Column(app.db.String(50), nullable=False)


    def __repr__(self):
        return '<Departments %r> % self.id'

