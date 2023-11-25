FROM python:3.11.4-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system dependencies
RUN apt-get update

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install django django-allauth pillow channels channels-redis python-magic python-magic-bin whitenoise gunicorn

COPY . /app

# Use Uvicorn as the entrypoint
ENTRYPOINT ["gunicorn", "BauDoMestre.wsgi", "--timeout", "180"]
