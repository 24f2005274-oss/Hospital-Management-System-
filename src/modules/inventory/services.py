from src.core.database import db
from src.modules.inventory.models import Medicine, InventoryLedger
from flask import abort

class PharmacyService:
    @staticmethod
    def dispense_medicine(medicine_id, quantity, user_id, reference_id):
        """
        Atomically deducts medicine from inventory. Throws error if insufficient stock.
        """
        medicine = Medicine.query.with_for_update().get(medicine_id)
        if not medicine:
            abort(404, description="Medicine not found")
            
        if medicine.stock_level < quantity:
            abort(400, description=f"Insufficient stock for {medicine.name}. Available: {medicine.stock_level}")
            
        # Deduct stock
        medicine.stock_level -= quantity
        
        # Create Ledger Entry
        ledger = InventoryLedger(
            medicine_id=medicine.id,
            delta=-quantity,
            transaction_type='PRESCRIPTION',
            reference_id=str(reference_id),
            recorded_by=user_id
        )
        
        db.session.add(ledger)
        # Note: db.session.commit() should be called by the parent route/service to maintain the transaction
