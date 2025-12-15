VENV := venv
BIN := $(VENV)/bin
 
venv: ## Make a new virtual environment
	python3 -m venv $(VENV) && pip install -r requirements.txt 

activate:
	source $(BIN)/activate

install: venv ## Make venv and install requirements
	$(BIN)/pip install --upgrade -r requirements.txt

freeze: ## Pin current dependencies
	$(BIN)/pip freeze > requirements.txt

startapp:
	@echo "Running start app : $(app)"
	python manage.py startapp $(app) apps/$(app)

run:
	python manage.py runserver
 
migration:
	@echo "Running makemigrations for app: $(app)"
	python manage.py makemigrations $(app)

migrate: 
	python manage.py migrate

superuser:
	python manage.py createsuperuser

pip-install-dev:
	pip install --upgrade pip pip-tools
	pip-sync requirements.txt requirements-dev.txt

pip-install:
	pip install --upgrade pip pip-tools
	pip-sync requirements.txt

pip-update:
	pip install --upgrade pip pip-tools
	pip-compile requirements.in
	pip-compile requirements-dev.in
	pip-sync requirements.txt requirements-dev.txt

clean:
	rm -rf __pycache__
	rm -rf venv

tailwind-start:
	python manage.py tailwind start