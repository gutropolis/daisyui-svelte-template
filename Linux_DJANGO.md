# Running Django on Ubuntu

These steps assume Ubuntu and Python 3.

## 1. Create a Virtual Environment

```bash
cd /home/gs/Project/daisyui-svelte-template/backend
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install Dependencies

```bash
pip3 install django graphene-django
```

Add any additional packages your project requires.

## 3. Configure Environment Variables (Optional)

If your project needs custom settings:

```bash
export DJANGO_SETTINGS_MODULE=config.settings
```

## 4. Run Database Migrations

```bash
python3 manage.py migrate
```

## 5. Start the Development Server

```bash
python3 manage.py runserver 0.0.0.0:8000
```

The server will be available at http://127.0.0.1:8000/ by default.

## 6. Create a Superuser (Optional)

```bash
python3 manage.py createsuperuser
```

Follow the prompts to set credentials.

## 7. Stop the Server

Press `Ctrl+C` in the terminal running `runserver`.

## 8. Reactivate the Virtual Environment Later

```bash
cd /home/gs/Project/daisyui-svelte-template/backend
source .venv/bin/activate
```

Run `deactivate` to exit when finished.

## Common Django Management Commands

| Command                                           | Purpose                                                              |
| ------------------------------------------------- | -------------------------------------------------------------------- |
| `python3 manage.py runserver`                     | Start the development server (defaults to `http://127.0.0.1:8000/`). |
| `python3 manage.py migrate`                       | Apply database migrations to keep schema up to date.                 |
| `python3 manage.py makemigrations`                | Generate migration files from model changes.                         |
| `python3 manage.py createsuperuser`               | Create an admin user for logging into Django admin.                  |
| `python3 manage.py shell`                         | Open an interactive Django-aware Python shell.                       |
| `python3 manage.py showmigrations`                | List migrations and show which ones have run.                        |
| `python3 manage.py sqlmigrate <app> <migration>`  | Preview SQL generated for a migration.                               |
| `python3 manage.py test`                          | Discover and run automated tests.                                    |
| `python3 manage.py startapp <name>`               | Scaffold a new Django app inside the project.                        |
| `python3 manage.py startapp account apps/account` |
| `python3 manage.py collectstatic`                 | Gather static assets into `STATIC_ROOT` for deployment.              |
| `python3 manage.py dumpdata`                      | Export database contents to JSON (fixtures).                         |
| `python3 manage.py loaddata <fixture>.json`       | Import fixture data into the database.                               |
| `python3 manage.py flush`                         | Reset the database (clears data, keeps schema).                      |
| `python3 manage.py check`                         | Run system checks for potential configuration issues.                |
| `python3 manage.py diffsettings`                  | Compare current settings with Django defaults.                       |

> Tip: run `python3 manage.py help` to see every available command. Most commands accept `--help` for more details, e.g. `python3 manage.py runserver --help`.
