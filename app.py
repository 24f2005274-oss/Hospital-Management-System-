from src.app import create_app
from src.core.database import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Initialize database tables
        db.create_all()
    
    app.run(debug=True, port=5000)
