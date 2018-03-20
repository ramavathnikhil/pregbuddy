web: gunicorn pregbuddy.wsgi --log-file -
release: python manage.py makemigrations api
release: python manage.py migrate
release: python manage.py migrate --run-syncdb