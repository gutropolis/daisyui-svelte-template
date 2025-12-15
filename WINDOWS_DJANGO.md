# Running Django on Windows

These steps assume Windows PowerShell and Python 3.13 from the Microsoft Store.

## 1. Create a Virtual Environment

```powershell
cd E:\project\daisyui-svelte-template\backend
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 2. Install Dependencies

```powershell
pip install django graphene-django
```

Add any additional packages your project requires.

## 3. Configure Environment Variables (Optional)

If your project needs custom settings:

```powershell
$env:DJANGO_SETTINGS_MODULE = "config.settings"
```

## 4. Run Database Migrations

```powershell
python manage.py migrate
```

## 5. Start the Development Server

```powershell
python manage.py runserver 0.0.0.0:8000
```

The server will be available at http://127.0.0.1:8000/ by default.

## 6. Create a Superuser (Optional)

```powershell
python manage.py createsuperuser
```

Follow the prompts to set credentials.

## 7. Stop the Server

Press `Ctrl+C` in the terminal running `runserver`.

## 8. Reactivate the Virtual Environment Later

```powershell
cd E:\project\daisyui-svelte-template\backend
.venv\Scripts\Activate.ps1
```

Run `deactivate` to exit when finished.

## Common Django Management Commands

| Command                                          | Purpose                                                              |
| ------------------------------------------------ | -------------------------------------------------------------------- |
| `python manage.py runserver`                     | Start the development server (defaults to `http://127.0.0.1:8000/`). |
| `python manage.py migrate`                       | Apply database migrations to keep schema up to date.                 |
| `python manage.py makemigrations`                | Generate migration files from model changes.                         |
| `python manage.py createsuperuser`               | Create an admin user for logging into Django admin.                  |
| `python manage.py shell`                         | Open an interactive Django-aware Python shell.                       |
| `python manage.py showmigrations`                | List migrations and show which ones have run.                        |
| `python manage.py sqlmigrate <app> <migration>`  | Preview SQL generated for a migration.                               |
| `python manage.py test`                          | Discover and run automated tests.                                    |
| `python manage.py startapp <name>`               | Scaffold a new Django app inside the project.                        |
| `python manage.py startapp account apps/account` |
| `python manage.py collectstatic`                 | Gather static assets into `STATIC_ROOT` for deployment.              |
| `python manage.py dumpdata`                      | Export database contents to JSON (fixtures).                         |
| `python manage.py loaddata <fixture>.json`       | Import fixture data into the database.                               |
| `python manage.py flush`                         | Reset the database (clears data, keeps schema).                      |
| `python manage.py check`                         | Run system checks for potential configuration issues.                |
| `python manage.py diffsettings`                  | Compare current settings with Django defaults.                       |

> Tip: run `python manage.py help` to see every available command. Most commands accept `--help` for more details, e.g. `python manage.py runserver --help`.
