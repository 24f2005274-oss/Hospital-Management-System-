from src.core.database import db, BaseModel
from datetime import datetime

class Appointment(BaseModel):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), default='Booked')
    symptoms = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    treatment = db.relationship('Treatment', backref='appointment', uselist=False, cascade='all, delete-orphan')

class Treatment(BaseModel):
    __tablename__ = 'treatments'
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'), nullable=False)
    diagnosis = db.Column(db.Text, nullable=False)
    prescription = db.Column(db.Text)
    notes = db.Column(db.Text)
    visit_type = db.Column(db.String(50))
    tests_done = db.Column(db.Text)
    medicines = db.Column(db.Text)
    treatment_date = db.Column(db.DateTime, default=datetime.utcnow)

class DoctorAvailability(BaseModel):
    __tablename__ = 'doctor_availability'
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    is_available = db.Column(db.Boolean, default=True)

class Ward(BaseModel):
    __tablename__ = 'wards'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ward_type = db.Column(db.String(50)) # ICU, General, Maternity
    capacity = db.Column(db.Integer, nullable=False)

    beds = db.relationship('Bed', backref='ward', lazy=True)

class Bed(BaseModel):
    __tablename__ = 'beds'
    id = db.Column(db.Integer, primary_key=True)
    ward_id = db.Column(db.Integer, db.ForeignKey('wards.id'), nullable=False)
    bed_number = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='AVAILABLE') # AVAILABLE, OCCUPIED, MAINTENANCE
    
    current_encounter_id = db.Column(db.Integer, db.ForeignKey('encounters.id'), nullable=True)
