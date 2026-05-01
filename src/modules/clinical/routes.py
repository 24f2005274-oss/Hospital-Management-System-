from flask import Blueprint, render_template
from flask_login import login_required

clinical_bp = Blueprint('clinical', __name__)

@clinical_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('doctor/cockpit.html')

@clinical_bp.route('/patients')
@login_required
def patients():
    return render_template('placeholder.html', title='Patient Fleet', icon='ph-users')

@clinical_bp.route('/admit', methods=['GET', 'POST'])
@login_required
def admit():
    return render_template('doctor/admit.html')
