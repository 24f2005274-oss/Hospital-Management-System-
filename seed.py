from src.app import create_app
from src.core.database import db
from src.infrastructure.auth.models import Role, User
from src.modules.clinical.models import Department, Doctor, Patient
from src.modules.operations.models import Ward, Bed
from src.modules.inventory.models import Medicine
from datetime import date

app = create_app()

def seed_database():
    with app.app_context():
        print("Cleaning old data...")
        db.drop_all()
        db.create_all()

        print("Seeding Roles...")
        admin_role = Role(name='Admin', description='Superuser access')
        doctor_role = Role(name='Doctor', description='Clinical access')
        db.session.add_all([admin_role, doctor_role])
        db.session.commit()

        print("Seeding Admin User...")
        admin = User(username='admin', email='admin@hos.local', role_id=admin_role.id)
        admin.set_password('admin123')
        db.session.add(admin)

        print("Seeding Departments & Doctors...")
        cardiology = Department(name='Cardiology', description='Heart Institute')
        db.session.add(cardiology)
        db.session.commit()

        doc_user = User(username='dr_smith', email='smith@hos.local', role_id=doctor_role.id)
        doc_user.set_password('doctor123')
        db.session.add(doc_user)
        db.session.commit()

        doctor = Doctor(user_id=doc_user.id, full_name='Dr. John Smith', department_id=cardiology.id, specialization='Cardiologist')
        db.session.add(doctor)

        print("Seeding Wards & Beds...")
        icu = Ward(name='Intensive Care Unit (ICU)', ward_type='ICU', capacity=10)
        db.session.add(icu)
        db.session.commit()
        
        bed1 = Bed(ward_id=icu.id, bed_number='ICU-01', status='AVAILABLE')
        bed2 = Bed(ward_id=icu.id, bed_number='ICU-02', status='OCCUPIED')
        db.session.add_all([bed1, bed2])

        print("Seeding Pharmacy Inventory...")
        para = Medicine(name='Paracetamol 500mg', generic_name='Acetaminophen', stock_level=5000, unit_price=0.50)
        amox = Medicine(name='Amoxicillin 250mg', generic_name='Amoxicillin', stock_level=1200, unit_price=1.20)
        morphine = Medicine(name='Morphine 10mg', generic_name='Morphine Sulfate', stock_level=50, is_controlled=True, unit_price=15.00)
        db.session.add_all([para, amox, morphine])

        db.session.commit()
        print("✅ Database successfully seeded for Enterprise H-OS!")

if __name__ == '__main__':
    seed_database()
