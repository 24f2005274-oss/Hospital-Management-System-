import json
from flask import request
from flask_login import current_user
from src.core.database import db
from src.infrastructure.audit_logs.models import AuditLog

class AuditService:
    @staticmethod
    def log_event(action, table_name, record_id, old_data=None, new_data=None):
        """
        Records a transaction to the audit ledger.
        """
        # Determine IP Address safely
        ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
        
        user_id = current_user.id if current_user and current_user.is_authenticated else None
        
        log = AuditLog(
            user_id=user_id,
            action=action,
            table_name=table_name,
            record_id=str(record_id),
            old_data=old_data,
            new_data=new_data,
            ip_address=ip_address
        )
        
        db.session.add(log)
        # Commit usually handled by the caller transaction
