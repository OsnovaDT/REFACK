docker-compose -f docker-compose.yml run --rm web coverage run --source . manage.py test
docker-compose -f docker-compose.yml run --rm web coverage report
docker-compose -f docker-compose.yml run --rm web coverage html