.PHONY: help test run migrate venv

.DEFAULT: help

help:
	@echo "make venv"
	@echo "       prepare development environment, installs all requirements"
	@echo "make test"
	@echo "       run tests (TODO)"
	@echo "make pip_install"
	@echo "       install pip3 and virtualenv"
	@echo "make run"
	@echo "       run project"
	@echo "make migrate"
	@echo "       migrate models into database"
	@echo "make clean"
	@echo "       clean the project"

pip_install:
	sudo apt-get -y install python3-pip
	sudo python3 -m pip install virtualenv

venv: pip_install requirements.txt
	python3 -m virtualenv venv
	. venv/bin/activate; pip3 install -Ur requirements.txt
	touch venv/bin/activate

test: venv
	. venv/bin/activate; nosetests online-hostess/tests

migrate:
	. venv/bin/activate; python3 manage.py db init; python3 manage.py db migrate; python manage.py db upgrade;

run:
	. venv/bin/activate; python3 onlinehostess/run.py

clean:
	rm -rf venv
	find -iname "*.pyc" -delete