.PHONY: install-backend install-frontend install run-backend run-frontend migrate superuser build-frontend test-frontend clean-backend clean-frontend clean startapp makemigrations shell showmigrations sqlmigrate test collectstatic dumpdata loaddata flush check diffsettings freeze pip-install-dev pip-install pip-update

# Backend commands
install-backendmake:
	cd backend && python3.13 -m venv .venv && ./.venv/bin/pip install -r requirements.txt

website-api:
	cd backend && ./.venv/bin/python manage.py runserver

migrate:
	cd backend && ./.venv/bin/python manage.py migrate

superuser:
	cd backend && ./.venv/bin/python manage.py createsuperuser

startapp:
	cd backend && ./.venv/bin/python manage.py startapp $(app) apps/$(app)

makemigrations:
	cd backend && ./.venv/bin/python manage.py makemigrations $(app)

shell:
	cd backend && ./.venv/bin/python manage.py shell

showmigrations:
	cd backend && ./.venv/bin/python manage.py showmigrations

sqlmigrate:
	cd backend && ./.venv/bin/python manage.py sqlmigrate $(app) $(migration)

test:
	cd backend && ./.venv/bin/python manage.py test

collectstatic:
	cd backend && ./.venv/bin/python manage.py collectstatic

dumpdata:
	cd backend && ./.venv/bin/python manage.py dumpdata

loaddata:
	cd backend && ./.venv/bin/python manage.py loaddata $(fixture)

flush:
	cd backend && ./.venv/bin/python manage.py flush

check:
	cd backend && ./.venv/bin/python manage.py check

diffsettings:
	cd backend && ./.venv/bin/python manage.py diffsettings

freeze:
	cd backend && ./.venv/bin/pip freeze > requirements.txt

pip-install-dev:
	cd backend && ./.venv/bin/pip install --upgrade pip pip-tools && ./.venv/bin/pip-sync requirements.txt requirements-dev.txt

pip-install:
	cd backend && ./.venv/bin/pip install --upgrade pip pip-tools && ./.venv/bin/pip-sync requirements.txt

pip-update:
	cd backend && ./.venv/bin/pip install --upgrade pip pip-tools && ./.venv/bin/pip-compile requirements.in && ./.venv/bin/pip-compile requirements-dev.in && ./.venv/bin/pip-sync requirements.txt requirements-dev.txt

clean-backend:
	cd backend && rm -rf .venv __pycache__

# Frontend commands
install-frontend:
	export PATH="$(HOME)/.local/node22/bin:$$PATH" && cd frontend && yarn

website-dev:
	export PATH="$(HOME)/.local/node22/bin:$$PATH" && cd frontend && yarn dev

build-frontend:
	export PATH="$(HOME)/.local/node22/bin:$$PATH" && cd frontend && yarn build

preview-frontend:
	export PATH="$(HOME)/.local/node22/bin:$$PATH" && cd frontend && yarn preview

test-frontend:
	export PATH="$(HOME)/.local/node22/bin:$$PATH" && cd frontend && yarn test

lint-frontend:
	export PATH="$(HOME)/.local/node22/bin:$$PATH" && cd frontend && yarn lint

check-frontend:
	export PATH="$(HOME)/.local/node22/bin:$$PATH" && cd frontend && yarn check

clean-frontend:
	cd frontend && rm -rf node_modules yarn.lock

# Combined commands
install: install-backend install-frontend

clean: clean-backend clean-frontend