from flask import Flask, render_template
from flask_login import LoginManager
from src.core.config import Config
from src.core.database import db, migrate
from src.infrastructure.auth.models import User

# Initialize LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app(config_class=Config):
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register Error Handlers
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template('500.html'), 500

    # Register Blueprints
    from src.infrastructure.auth.routes import auth_bp
    from src.modules.clinical.routes import clinical_bp
    from src.modules.operations.routes import operations_bp
    from src.modules.search.routes import search_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(clinical_bp, url_prefix='/clinical')
    app.register_blueprint(operations_bp, url_prefix='/operations')
    app.register_blueprint(search_bp)
    
    # Root Route
    @app.route('/')
    def index():
        # Redirect based on role or to login
        from flask_login import current_user
        from flask import redirect, url_for
        if current_user.is_authenticated:
            # We'll implement role-based redirect in auth later
            return redirect(url_for('clinical.dashboard'))
        return redirect(url_for('auth.login'))

    return app
