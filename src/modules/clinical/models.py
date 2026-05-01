from src.core.database import db, BaseModel

class Department(BaseModel):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)

    doctors = db.relationship('Doctor', backref='department', lazy=True)

class Doctor(BaseModel):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    specialization = db.Column(db.String(100))
    qualification = db.Column(db.String(200))
    experience_years = db.Column(db.Integer)
    phone = db.Column(db.String(15))
    license_number = db.Column(db.String(50), unique=True)
    bio = db.Column(db.Text)

    appointments = db.relationship('Appointment', backref='doctor', lazy=True)
    availability = db.relationship('DoctorAvailability', backref='doctor', cascade='all, delete-orphan')

class Patient(BaseModel):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    phone = db.Column(db.String(15))
    address = db.Column(db.Text)
    blood_group = db.Column(db.String(5))
    emergency_contact = db.Column(db.String(15))

    appointments = db.relationship('Appointment', backref='patient', lazy=True)
    encounters = db.relationship('Encounter', backref='patient', lazy=True)

class Encounter(BaseModel):
    __tablename__ = 'encounters'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    encounter_type = db.Column(db.String(50)) # OPD, IPD, EMERGENCY
    admission_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    discharge_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), default='ACTIVE') # ACTIVE, DISCHARGED
    
    vitals = db.relationship('VitalsChart', backref='encounter', lazy=True)

class VitalsChart(BaseModel):
    __tablename__ = 'vitals_charting'
    id = db.Column(db.Integer, primary_key=True)
    encounter_id = db.Column(db.Integer, db.ForeignKey('encounters.id'), nullable=False)
    heart_rate = db.Column(db.Integer)
    blood_pressure_systolic = db.Column(db.Integer)
    blood_pressure_diastolic = db.Column(db.Integer)
    temperature = db.Column(db.Float)
    recorded_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
