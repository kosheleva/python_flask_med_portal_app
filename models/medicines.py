from flask import current_app as app


class Medicines(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(150), nullable=False)
    code = app.db.Column(app.db.String(15), nullable=False)

    def __repr__(self):
        return '<Medicines %r> % self.id'

