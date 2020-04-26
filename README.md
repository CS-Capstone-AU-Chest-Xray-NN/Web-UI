# Web-UI

![WebUI](https://github.com/CS-Capstone-AU-Chest-Xray-NN/Web-UI/blob/master/webui.png?raw=true)

## Training Model

Train the [Neural Network](https://github.com/CS-Capstone-AU-Chest-Xray-NN/Chest-Xray-Diagnostic-Neural-Network) and move the model and weights to `webui/cnn/model/`

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

Flush database

```bash
docker-compose run web python manage.py flush --no-input
```

Clear migrations

```bash
docker-compose run web python manage.py migrate cnn zero
```

## Deploying

Generate a new `SECRET_KEY` using `key.sh`

Copy `.env.dev` to `.env`. Change `DEBUG` to `0` and edit `SECRET_KEY`

In `docker-compose.yml` change `services.web.env_file` from `.env.dev` to `.env`

Run `docker-compose up --build`

Run `docker-compose run web python manage.py collectstatic`

Run `docker-compose run web python manage.py migrate`

Run `docker-compose up -d`
