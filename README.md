# asana_control

After downloading:

1. Postgres setup through Makefile

- (CMD: create_db_role) Create a new role (target password is in the base_settings.py)

- (CMD: create_db) Create target database

- (CMD: migrate_db) Apply migrations to DB

2. Building and Running Docker with Django through Makefile

- (CMD: build) Setting environment and building Django with gunicorn

3. Run Django

- docker-compose up asana

