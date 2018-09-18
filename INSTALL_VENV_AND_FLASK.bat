REM installing virtualenv on your computer
pip install virtualenv
REM setting up virtualev in venv folder
virtualenv venv
REM activating virtual environment
venv\Scripts\activate
REM installing Flask to run local server
pip install Flask
pip install flask-restful
pip install flask-sqlalchemy psycopg2 flask-migrate flask-bcrypt pyjwt
REM updating setuptools to the latest version
pip install --upgrade pip setuptools
