#!/bin/bash
echo "Starting Hospital OS Local Development Environment..."

# Check if venv exists, if not create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the app
echo "Starting application..."
export FLASK_APP=app.py
export FLASK_ENV=development
python3 app.py
