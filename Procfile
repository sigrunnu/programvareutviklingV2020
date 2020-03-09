release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn exerciseit.wsgi:application --log-file - --log-level debug