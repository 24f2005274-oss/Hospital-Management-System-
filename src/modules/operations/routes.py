from flask import Blueprint

operations_bp = Blueprint('operations', __name__)

from flask_login import login_required
from flask import render_template

@operations_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('placeholder.html', title='Operations', icon='ph-stack')

@operations_bp.route('/wards')
@login_required
def wards():
    return render_template('placeholder.html', title='Wards & Beds', icon='ph-bed')

@operations_bp.route('/pharmacy')
@login_required
def pharmacy():
    return render_template('placeholder.html', title='Pharmacy Inventory', icon='ph-pill')

@operations_bp.route('/system')
@login_required
def system():
    return render_template('placeholder.html', title='System Config', icon='ph-gear')
