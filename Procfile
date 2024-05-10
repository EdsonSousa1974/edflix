web: python manage.py migrate && gunicorn edflix.wsgi:application \
    --log-file \
    --env DJANGO_SETTINGS_MODULE=edflix.production_settings \
    --name edflix \
    --bind 0.0.0.0:8000 \
    --timeout 600 \
    --workers 4 \
    --log-level=info \
    --reload -