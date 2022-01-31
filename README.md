# e-commerce-app
Ecommerce app using Django, Rest API, Docker and ElasticSearch

### Sort pipfile
    pipfile-sort

### Runserver with Werkzeug (django-extensions)
    ./manage.py runserver_plus
### Run Django shell
    ./manage.py shell
  or better with auto importing models (django-extensions)

    ./manage.py shell_plus

### Installation
    pip install -r requirements.txt

  or

    pipenv install

### Activate of virtual environment
    pipenv shell

### Install new plugins
    pipenv install

### Versioning
    pipenv lock -r > requirements.txt
  and with dependencies tree for reference:

    pipdeptree -f > requirements-graph.txt

### Tests
    pytest -s -v --durations=0

### Collect static files
    ./manage.py collectstatic

  then compile scss files

    ./manage.py compress --force
### Migrations
    ./manage.py migrate
### Update translation files
    ./manage.py makemessages -l fr && ./manage.py compilemessages -l fr

### Show urls (django-extensions)
    ./manage.py show_urls

### Check template errors (django-extensions)
    ./manage.py validate_templates
### Backup and seed DB

##### Save database to db.json
    ./manage.py dumpdata --natural-foreign --exclude=auth.permission --exclude=contenttypes --indent=4 > src/fixtures/db.json
##### Seed database from db.json

    ./manage.py loaddata src/fixtures/db.json

### Drop DB (django-extensions)
    ./manage.py reset_db