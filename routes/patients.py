from flask import render_template, request, redirect
from flask_login import current_user
from datetime import date
from sqlalchemy import text
import json


class Patients():


    def __init__(self, db, models):
        self.db = db
        self.models = models


    def get_patients(self):
        patients = self.db.session.execute(
            text('''
                WITH
                    consultations_with_schemas AS (
                        SELECT 
                        c.id as consultation_id,
                        JSON_ARRAYAGG(
                            JSON_OBJECT(
                                'consultation_id', c.id, 
                                'complaint', c.complaint, 
                                'diagnosis', c.diagnosis, 
                                'c_date', c.date,    
                                'schema_id', ps.id,  
                                'medicine_code', m.code,
                                'medicine_name', m.name, 
                                'description', ps.description, 
                                'start_date', ps.start_date, 
                                'end_date', ps.end_date
                            )
                        ) as consultation_schemas
                        FROM medportal.consultations c
                        LEFT JOIN medportal.PatientsSchemas ps ON ps.consultation_id=c.id
                        LEFT JOIN medportal.Medicines m ON m.id=ps.medicine_id
                        GROUP BY c.id
                    )
                SELECT 
                    p.id,
                    JSON_OBJECT(
                        'name', p.name, 
                        'surname', p.surname,  
                        'phone', p.phone,
                        'gender', p.gender, 
                        'date_of_birth', p.date_of_birth, 
                        'age', YEAR(CURDATE()) - YEAR(p.date_of_birth)
                    ) as patient_info,
                    JSON_ARRAYAGG(cws.consultation_schemas) as consultations FROM medportal.patients p 
                LEFT JOIN consultations c ON p.id=c.patient_id
                LEFT JOIN consultations_with_schemas cws ON cws.consultation_id=c.id 
                GROUP BY p.id;
            ''')).all()

        result = []

        # @todo: find better way to parse json string
        for p in patients:
            result.append({
                "patient_id": p[0],
                "patient_info": json.loads(p[1]),
                "consultations": json.loads(p[2])
            })

        medicines = self.models['medicines'].query.order_by(self.models['medicines'].name).all()

        return render_template('patients.html', patients=result, medicines=medicines)


    def add_patients(self):
        if request.method == 'POST':
            name = request.form['name']
            surname = request.form['surname']
            phone = request.form['phone']
            gender = request.form['gender']
            date_of_birth = request.form['date_of_birth']

            empty_fields = []

            for field in request.form:
                if not request.form[field]:
                    empty_fields.append(field)

            if len(empty_fields):
                return render_template('patients_add.html', empty_fields=empty_fields)

            try:
                new_patient = self.models['patients'](
                    name=name,
                    surname=surname,
                    phone=phone,
                    gender=gender,
                    date_of_birth=date_of_birth
                )

                self.db.session.add(new_patient)
                self.db.session.commit()
            except Exception as e:
                # @todo: add logger
                print(e)
                return render_template('error.html')

            return redirect("/patients")
        else:
            return render_template('patients_add.html')


    def patients_add_consultation(self):
        complaint = request.form['complaint']
        diagnosis = request.form['diagnosis']
        patient_id = request.form['patient_id']

        try:
            new_consultation = self.models['consultations'](
                complaint=complaint,
                diagnosis=diagnosis,
                patient_id=int(patient_id),
                doctor_id=int(current_user.id),
                date=date.today()
            )

            self.db.session.add(new_consultation)
            self.db.session.commit()
        except Exception as e:
            print(e)
            return render_template('error.html')

        return redirect("/patients")


    def patients_add_schema(self):
        medicine_id = request.form['medicine_id']
        description = request.form['description']
        consultation_id = request.form['consultation_id']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        print(medicine_id, consultation_id)

        try:
            new_schema = self.models['PatientsSchemas'](
                medicine_id=int(medicine_id),
                description=description,
                consultation_id=int(consultation_id),
                start_date=start_date,
                end_date=end_date
            )

            self.db.session.add(new_schema)
            self.db.session.commit()
        except Exception as e:
            print(e)
            return render_template('error.html')

        return redirect("/patients")