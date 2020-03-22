release: python manage.py migrate
web: gunicorn exerciseit.wsgi:application --log-file - --log-level debug