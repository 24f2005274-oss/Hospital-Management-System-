from src.core.database import db, BaseModel
from datetime import datetime

class Medicine(BaseModel):
    __tablename__ = 'medicines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    generic_name = db.Column(db.String(150))
    stock_level = db.Column(db.Integer, default=0)
    reorder_level = db.Column(db.Integer, default=50)
    is_controlled = db.Column(db.Boolean, default=False) # e.g. Schedule H1 drugs
    unit_price = db.Column(db.Float, nullable=False, default=0.0)

    ledgers = db.relationship('InventoryLedger', backref='medicine', lazy='dynamic')

class InventoryLedger(BaseModel):
    __tablename__ = 'inventory_ledger'
    id = db.Column(db.Integer, primary_key=True)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'), nullable=False)
    delta = db.Column(db.Integer, nullable=False) # Negative for deduction, Positive for restock
    transaction_type = db.Column(db.String(50), nullable=False) # 'PRESCRIPTION', 'RESTOCK', 'ADJUSTMENT'
    reference_id = db.Column(db.String(100)) # Could link to a prescription ID or PO number
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    recorded_by = db.Column(db.Integer, db.ForeignKey('users.id')) # Which pharmacist/doctor
