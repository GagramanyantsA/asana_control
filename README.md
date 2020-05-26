# asana_control

After downloading:

1. Postgres setup through Makefile

- (CMD: create_db_role) Create a new role (target password is in the base_settings.py)

- (CMD: create_db) Create target database

- (CMD: migrate_db) Apply migrations to DB

2. Create super user

- python manage.py createsuperuser

3. Building and Running Docker with Django through Makefile

- (CMD: build) Setting environment and building Django with gunicorn

4. Run Django

- docker-compose up asana (OR docker-compose up -d)

Note: To pass your ASANA TOKEN you can specify it in prod_settings.py file or 
      specify it in docker-compose through passing your settings file in DJANGO_SETTINGS_MODULE.

