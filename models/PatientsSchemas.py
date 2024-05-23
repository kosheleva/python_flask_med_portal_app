from flask import current_app as app


class PatientsSchemas(app.db.Model):
    __tablename__ = 'PatientsSchemas'

    id = app.db.Column(app.db.Integer, primary_key=True)
    description = app.db.Column(app.db.String(), nullable=False)
    start_date = app.db.Column(app.db.DateTime, nullable=False)
    end_date = app.db.Column(app.db.DateTime, nullable=False)

    medicine_id = app.db.Column(app.db.Integer, app.db.ForeignKey('medicines.id'), nullable=False)
    consultation_id = app.db.Column(app.db.Integer, app.db.ForeignKey('consultations.id'), nullable=False)

    def __repr__(self):
        return '<PatientsSchemas %r> % self.id'

