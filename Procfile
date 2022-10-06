release: python manage.py migrate
web: gunicorn coovicordon.asgi:application -k uvicorn.workers.UvicornWorker
