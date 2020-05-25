DB_NAME=AsanaDB
DB_USER=AsanaUser

create_db_role:
	sudo su - postgres -c "createuser -DRSP $(DB_USER)"

drop_db_role:
	sudo su - postgres -c "dropuser $(DB_USER)"

drop_db:
	sudo su - postgres -c "dropdb $(DB_NAME)" || true

create_db:
	sudo su - postgres -c "createdb -O $(DB_USER) $(DB_NAME)"

recreate_db:
	make drop_db
	make create_db

migrate_db:
	python manage.py migrate

migrations_db:
	python manage.py makemigrations

super_user_db:
	python manage.py createsuperuser

recreate_db_with_migrations:
	make recreate_db
	make migrate_db