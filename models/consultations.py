from flask import current_app as app


class Consultations(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    complaint = app.db.Column(app.db.String(50), nullable=False)
    diagnosis = app.db.Column(app.db.String(100), nullable=False)
    date = app.db.Column(app.db.DateTime, nullable=False)

    patient_id = app.db.Column(app.db.Integer, app.db.ForeignKey('patients.id'), nullable=False)
    doctor_id = app.db.Column(app.db.Integer, app.db.ForeignKey('doctors.id'), nullable=False)

    def __repr__(self):
        return '<Consultations %r> % self.id'

