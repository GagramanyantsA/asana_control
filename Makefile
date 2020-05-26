# DB

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

# DEPLOY

DOCKER_CONTAINERS_DIR=/var/docker_containers/
ASANA_DIR=$(DOCKER_CONTAINERS_DIR)asana_control/
ASANA_CONF_DIR=$(ASANA_DIR)config/

set_env:
	sudo rm -r $(DOCKER_CONTAINERS_DIR) || true
	sudo mkdir -p $(DOCKER_CONTAINERS_DIR) $(ASANA_DIR) $(ASANA_CONF_DIR)
	sudo cp ./config/gunicorn_conf.py $(ASANA_CONF_DIR)
	sudo cp ./config/prod_settings.py $(ASANA_CONF_DIR)


build_docker:
	docker-compose build asana

build:
	make set_env
	make build_docker

docker_none_clear:
	sudo docker rmi $$(docker images --filter "dangling=true" -q --no-trunc)