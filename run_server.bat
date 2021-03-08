@echo off
call venv\Scripts\activate
call python -m pip install -r requirements.txt
call set FLASK_APP=wsgi & set FLASK_DEBUG=True
call cd src & start "Open website" open_localhost.bat & call cd ..
call flask run
