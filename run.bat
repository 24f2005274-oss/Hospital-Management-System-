@echo off
echo Starting Hospital OS Local Development Environment...

REM Check if venv exists, if not create it
IF NOT EXIST "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run the app
echo Starting application...
set FLASK_APP=app.py
set FLASK_ENV=development
python app.py
pause
