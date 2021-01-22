all:
	docker-compose up

build:
	docker-compose build

migrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py migrate
