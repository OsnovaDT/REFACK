[![Django CI/CD Workflow](https://github.com/OsnovaDT/REFACK/actions/workflows/main.yaml/badge.svg)](https://github.com/OsnovaDT/REFACK/actions/workflows/main.yaml)
[![coverage percentage](https://codecov.io/gh/OsnovaDT/REFACK/branch/master/graph/badge.svg?token=6GOUES7M7E)](https://codecov.io/gh/OsnovaDT/REFACK)
# REFACK
![REFACK](./static_readme/app_work.gif)

## What is REFACK?
REFACK is a web linter for Python. It checks your code on different rules:
- All functions have **snake_case** naming style;
- All classes have **CapWords** naming style;
- All functions and classes have **docstring**;
- If a function returns boolean, its name should starts with «**is_**» prefix;
- If a function returns not boolean, its name should starts with «**get_**» prefix;
- All functions have **type hints**;
- All functions arguments have **type hints**.

## Requirements
Python 3.10, Django.

See requirements.txt for the Python modules.

## Deploy
Create **.env** file in root of your project with these environment variables:
```env
SECRET_KEY="<your_secret_key>"
```

Run the project
```bash
sudo docker-compose up --build
```

Make and run migrations
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

## Tests
### Coverage
[![coverage tree](https://codecov.io/gh/OsnovaDT/REFACK/branch/master/graphs/tree.svg?token=6GOUES7M7E)](https://codecov.io/gh/OsnovaDT/REFACK)

### Running
```bash
# Run all tests
docker-compose exec web python manage.py test

# Run tagged tests
docker-compose exec web python manage.py test --tag=<tag>
```

### Tags
**App «account»**
- account_config
- account_forms
- account_urls
- account_views

**App «refactoring»**
- refactoring_admin
- refactoring_config
- refactoring_models
- refactoring_urls
- refactoring_services
    - refactoring_services_code_items
    - refactoring_services_code_parser
    - refactoring_services_files_download
    - refactoring_services_rules_checker
    - refactoring_services_utils

## CI/CD Workflow

Workflow will passing successfully if:
- Code style meets conditions of Flake8
- All tests passed successfully
- Tests coverage >= 90%