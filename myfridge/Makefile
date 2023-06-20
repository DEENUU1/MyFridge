.PHONY:

install:
	docker-compose run --rm web pip install -r requirements.txt

start:
	docker-compose up -d 

migrate:
	docker-compose exec web python manage.py migrate 

runserver: 
	docker-compose exec web python manage.py runserver 0.0.0.0:8000

test:
	docker-compose run --rm web pytest

clean:
	docker-compose down 