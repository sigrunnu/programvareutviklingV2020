release: python manage.py migrate
release: python manage.py collectstatic --noinput
web: gunicorn exerciseit.wsgi:application --log-file - --log-level debug