# Web-UI

## Development Environment

Running migrations

```bash
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

Starting django (**Note:** may need to be run a couple of times before successfully starting)

```bash
docker-compose up
```

Clearing database

```bash
docker-compose run web python manage.py flush --no-input
```
