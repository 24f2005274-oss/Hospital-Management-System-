from functools import wraps
from flask import abort, flash, redirect, url_for
from flask_login import current_user

class AuthService:
    @staticmethod
    def role_required(*roles):
        """
        RBAC Middleware Decorator
        Usage: @AuthService.role_required('Admin', 'Doctor')
        """
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                if not current_user.is_authenticated:
                    flash('Please log in to access this page.', 'warning')
                    return redirect(url_for('auth.login'))
                
                # Assume current_user.role is the relationship mapped to Role model
                if current_user.role.name not in roles:
                    abort(403) # Forbidden
                return f(*args, **kwargs)
            return decorated_function
        return decorator
