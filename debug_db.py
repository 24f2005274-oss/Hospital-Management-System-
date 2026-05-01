from app import app, db, Appointment, Doctor, Patient
from datetime import date, datetime, time

with app.app_context():
    print("-" * 20)
    print(f"Total Appointments: {Appointment.query.count()}")
    print(f"Future Appointments: {Appointment.query.filter(Appointment.appointment_date >= date.today()).count()}")
    
    appointments = Appointment.query.all()
    if not appointments:
        print("No appointments found.")
    else:
        for a in appointments:
            print(f"ID: {a.id}, Date: {a.appointment_date}, Status: {a.status}")

    # Check if we have doctors and patients to create a dummy appointment
    doc = Doctor.query.first()
    pat = Patient.query.first()
    
    if doc and pat and not appointments:
        print("Creating a dummy appointment for today...")
        new_apt = Appointment(
            patient_id=pat.id,
            doctor_id=doc.id,
            appointment_date=date.today(),
            appointment_time=time(10, 0),
            status='Booked',
            symptoms='Debug check'
        )
        db.session.add(new_apt)
        db.session.commit()
        print("Dummy appointment created.")
    elif not doc:
        print("No doctors found.")
    elif not pat:
        print("No patients found.")
    print("-" * 20)
