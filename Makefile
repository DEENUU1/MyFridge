.PHONY build:

build:
	docker-compose -f docker-compose.dev.yml build

.PHONY up:

up:
	docker-compose -f docker-compose.dev.yml up

.PHONY down:

down:
	docker-compose -f docker-compose.dev.yml down

.PHONY makemigrations:
	docker-compose -f docker-compose.dev.yml exec web python manage.py makemigrations

.PHONY migrate:

migrate:
	docker-compose -f docker-compose.dev.yml exec web python manage.py migrate

.PHONY test:

test:
	docker-compose -f docker-compose.dev.yml run --rm web pytest
